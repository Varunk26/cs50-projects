import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    portfolio = []
    index = []
    totalstock = 0.0
    x = 0


    #Extract portfolio for logged in user(session - user id)
    portfolio = db.execute("SELECT * FROM owns WHERE owns_userid = ?", session["user_id"])

    y = len(portfolio)

    #Creat a dictionary for each stock and it's respective symbol, price and total
    for x in range(0,y):
        stockdata = {}
        p_stock = portfolio[x]["symbol"]
        p_shares = portfolio[x]["shares"]
        stocklookup = lookup(p_stock)
        p_price = stocklookup["price"]
        p_total = p_shares * p_price
        stockdata.update({"stock":p_stock})
        stockdata.update({"price":p_price})
        stockdata.update({"shares":p_shares})
        stockdata.update({"total":p_total})

        #append each dictionary of stock elements to a list called index
        index.append(stockdata)
        stockdata.clear

        #calculate total stock value
        totalstock = totalstock + p_total

    cash = db.execute("SELECT cash AS c FROM users WHERE id = ?", session["user_id"])

    p_cash = cash[0]["c"]

    grandtotal = float(p_cash) + totalstock

    return render_template("index.html", grandtotal=grandtotal, totalstock=totalstock, cash=p_cash, index=index)



@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    # User reached route via POSt
    if request.method == "POST":

        # Ensure symbol is entered
        if not request.form.get("symbol"):
            return apology("Enter symbol", 403)

        symbol = request.form.get("symbol")
        shares = request.form.get("shares")
        sharelookup = lookup(symbol)

        #Ensure symbol is valid
        if sharelookup is None:
            return apology("Enter Valid Symbol", 403)

        rows = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
        balance = rows[0]["cash"]
        total = float(shares) * (sharelookup["price"])





        #Ensure shares is a positive integer
        if int(shares) <= 0:
            return apology("Enter Valid Integer", 403)

        #Ensure sufficient balance
        if balance < total:
            return apology("insufficient balance", 403)

        #Insert transaction into buys table
        db.execute("INSERT INTO buys (stockname, shares, priceusd, totalusd, buys_userid) VALUES (?, ?, ?, ?, ?)", symbol, shares, sharelookup["price"], total, session["user_id"])

        #Update cash in users table
        setbalance = balance - total
        db.execute("UPDATE users SET cash = (?) WHERE id = (?)", setbalance, session["user_id"])

        #Update owns table
        checksymbol = db.execute("SELECT COUNT(*) AS m FROM owns WHERE symbol = ? AND owns_userid = ?", symbol, session["user_id"])

        if checksymbol[0]["m"] != 0:
            db.execute("UPDATE owns SET shares = shares + ? WHERE symbol = ?", shares, symbol)
        else:
            db.execute("INSERT INTO owns (stockname, shares, owns_userid, symbol) VALUES (?, ?, ?, ?)", sharelookup["name"], shares, session["user_id"], sharelookup["symbol"])


        return redirect("/")

    else:
        return render_template("buy.html")



@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    return apology("TODO")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    #User reached route via POST
    if request.method == "POST":
        quote = request.form.get("quote")
        quoted = lookup(quote)

        #Check if quoted has returned None
        if quoted == None:
            return apology("Invalid stock symbol", 403)
        else:
            return render_template("quoted.html", quoted=quoted)

    #User reached route via GET
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # Forget any user_id
    session.clear()

    # User reached route via POST
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Ensure password matches confirmation
        elif (request.form.get("password") != request.form.get("confirmation_password")):
            return apology("password does not match", 403)

        # Check if user name exists in database
        insertusername = request.form.get("username")
        insertpassword = request.form.get("password")
        insertpassword = generate_password_hash(insertpassword)
        usernamecheck = db.execute("SELECT COUNT(*) AS n FROM users WHERE username = ?", insertusername)


        if usernamecheck[0]["n"] != 0:
            return apology("user name exists, try different username", 403)
        # Insert username and password into table
        else:
            newid = db.execute("INSERT into users (username, hash) VALUES(?, ?)", insertusername, insertpassword)
            sessions["user_id"] = newid
        return redirect("/")

    # User reached route via GET
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    # User reached route via POSt
    if request.method == "POST":

        # Ensure symbol is entered
        if not request.form.get("symbol"):
            return apology("Enter symbol", 403)




        #Initialize neccessery variables
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")
        sharelookup = lookup(symbol)

        #Ensure symbol is valid
        if sharelookup is None:
            return apology("Enter Valid Symbol")


        rows = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
        balance = rows[0]["cash"]
        total = float(shares) * (sharelookup["price"])



        #Ensure input is a positive integer
        if int(shares) <= 0:
            return apology("Enter Valid Integer", 403)

        #Check if stock exists in owns table
        checkstock = db.execute("SELECT * FROM owns WHERE (owns_userid = ? AND symbol = ?)", session["user_id"], sharelookup["symbol"])

        if len(checkstock) > 0:
            if checkstock[0]['shares'] < int(shares):
                return apology("Insufficient stocks", 403)

            else:
                #Insert transaction into sells table
                db.execute("INSERT INTO sells (stockname, shares, priceusd, totalusd, sells_userid) VALUES (?, ?, ?, ?, ?)", symbol, shares, sharelookup["price"], total, session["user_id"])

                #Update cash in users table
                setbalance = balance + total
                db.execute("UPDATE users SET cash = (?) WHERE id = (?)", setbalance, session["user_id"])

                #Update owns table

                db.execute("UPDATE owns SET shares = shares - ? WHERE symbol = ?", shares, symbol)

        else:
            return apology("stock does not exist", 403)

        return redirect("/")

    else:
        return render_template("sell.html")

