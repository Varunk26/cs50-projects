import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash


db = SQL("sqlite:///finance.db")

user_id = 1

symbol = 'ABCD'

checkstock = db.execute("SELECT * FROM owns WHERE owns_userid = ? AND symbol = ?", user_id, symbol)


if len(checkstock) > 0:
    print(checkstock[0]['shares'])
else:
    print("stock no")



