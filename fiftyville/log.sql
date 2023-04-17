-- Keep a log of any SQL queries you execute as you solve the mystery.
.schema -- Overview of the database
.table -- Overview of all tables
.schema crime_scene_reports


SELECT * FROM crime_scene_reports -- To get an overview of the table
SELECT * FROM crime_scene_reports
    WHERE street = 'Humphrey Street' -- Data specific to date of crime, July 2021, 28th.
        AND year = 2021
        AND day = 28
        AND month = 7;

SELECT description FROM crime_scene reports WHERE street = 'Humphrey Street'
    AND year = 2021
    AND day = 28
    AND month = 7;

--Description of relevant crime scene reports (| Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery. Interviews were conducted today with three witnesses who were present at the time – each of their interview transcripts mentions the bakery. Littering took place at 16:36. No known witnesses)

.schema

.schema interviews -- Get a configuration of interviews

SELECT * FROM interviews -- To get an overview of the interviews on date of crime
    WHERE year = 2021
        AND month = 7
        AND day = 28;

SELECT name, transcript FROM interviews -- To get an overview of the interviews on date of crime
    WHERE year = 2021
        AND month = 7
        AND day = 28;

--|  name   |                                                                                                                                                     transcript                                                                                                                                                      |
--+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
--| Jose    | “Ah,” said he, “I forgot that I had not seen you for some weeks. It is a little souvenir from the King of Bohemia in return for my assistance in the case of the Irene Adler papers.”                                                                                                                               |
--| Eugene  | “I suppose,” said Holmes, “that when Mr. Windibank came back from France he was very annoyed at your having gone to the ball.”                                                                                                                                                                                      |
--| Barbara | “You had my note?” he asked with a deep harsh voice and a strongly marked German accent. “I told you that I would call.” He looked from one to the other of us, as if uncertain which to address.                                                                                                                   |
--| Ruth(Bakery security logs)    | Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away. If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.                                                          |
--| Eugene(atm_transactions, bank accounts)  | I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.                                                                                                 |
--| Raymond(phone calls, flights) | As the thief swas leaving the bakery, they called someone who talked to them for less than a minute. In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow. The thief then asked the person on the other end of the phone to purchase the flight ticket. |
--| Lily    | Our neighboring courthouse has a very annoying rooster that crows loudly at 6am every day. My sons Robert and Patrick took the rooster to a city far, far away, so it may never bother us again. My sons have successfully arrived in Paris.

.table -- check additional tables to explore based on evidence

.schema bakery_security_logs

SELECT * FROM bakery_security_logs; -- Check bakery security logs against the information form ruth - " within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away. If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame."

SELECT * FROM bakery_security_logs
    WHERE year = 2021
        AND day = 28
        AND month = 7
        AND hour = 10
        AND minute > 15
        AND minute < 25;

--+-----+------+-------+-----+------+--------+----------+---------------+
--| id  | year | month | day | hour | minute | activity | license_plate |
--+-----+------+-------+-----+------+--------+----------+---------------+
--| 260 | 2021 | 7     | 28  | 10   | 16     | exit     | 5P2BI95       |
--| 261 | 2021 | 7     | 28  | 10   | 18     | exit     | 94KL13X       |
--| 262 | 2021 | 7     | 28  | 10   | 18     | exit     | 6P58WS2       |
--| 263 | 2021 | 7     | 28  | 10   | 19     | exit     | 4328GD8       |
--| 264 | 2021 | 7     | 28  | 10   | 20     | exit     | G412CB7       |
--| 265 | 2021 | 7     | 28  | 10   | 21     | exit     | L93JTIZ       |
--| 266 | 2021 | 7     | 28  | 10   | 23     | exit     | 322W7JE       |
--| 267 | 2021 | 7     | 28  | 10   | 23     | exit     | 0NTHK55

--Eugene(atm_transactions, bank accounts)  | I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.                                                                                                 |

.schema atm_transactions -- get the table schema for atm_transaction

SELECT DISTINCT(atm_location) FROM atm_transactions; -- Get the different locations of atm

SELECT * FROM atm_transactions
    WHERE year = 2021
        AND month = 7
        AND day = 28
        AND atm_location = 'Leggett Street'
        AND transaction_type = 'withdraw';

--+-----+----------------+------+-------+-----+----------------+------------------+--------+
--| id  | account_number | year | month | day |  atm_location  | transaction_type | amount |
--+-----+----------------+------+-------+-----+----------------+------------------+--------+
--| 246 | 28500762       | 2021 | 7     | 28  | Leggett Street | withdraw         | 48     |
--| 264 | 28296815       | 2021 | 7     | 28  | Leggett Street | withdraw         | 20     |
--| 266 | 76054385       | 2021 | 7     | 28  | Leggett Street | withdraw         | 60     |
--| 267 | 49610011       | 2021 | 7     | 28  | Leggett Street | withdraw         | 50     |
--| 269 | 16153065       | 2021 | 7     | 28  | Leggett Street | withdraw         | 80     |
--| 288 | 25506511       | 2021 | 7     | 28  | Leggett Street | withdraw         | 20     |
--| 313 | 81061156       | 2021 | 7     | 28  | Leggett Street | withdraw         | 30     |
--| 336 | 26013199       | 2021 | 7     | 28  | Leggett Street | withdraw         | 35     |

--Raymond(phone calls, flights) | As the thief swas leaving the bakery, they called someone who talked to them for less than a minute. In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow. The thief then asked the person on the other end of the phone to purchase the flight ticket. |

SELECT * FROM phone_calls
    WHERE year = 2021
        AND day = 28
        AND month = 7
        AND duration < 60;

--| id  |     caller     |    receiver    | year | month | day | duration |
--+-----+----------------+----------------+------+-------+-----+----------+
--| 221 | (130) 555-0289 | (996) 555-8899 | 2021 | 7     | 28  | 51       |
--| 224 | (499) 555-9472 | (892) 555-8872 | 2021 | 7     | 28  | 36       |
--| 233 | (367) 555-5533 | (375) 555-8161 | 2021 | 7     | 28  | 45       |
--| 251 | (499) 555-9472 | (717) 555-1342 | 2021 | 7     | 28  | 50       |
--| 254 | (286) 555-6063 | (676) 555-6554 | 2021 | 7     | 28  | 43       |
--| 255 | (770) 555-1861 | (725) 555-3243 | 2021 | 7     | 28  | 49       |
--| 261 | (031) 555-6622 | (910) 555-3251 | 2021 | 7     | 28  | 38       |
--| 279 | (826) 555-1652 | (066) 555-9701 | 2021 | 7     | 28  | 55       |
--| 281 | (338) 555-6650 | (704) 555-2131 | 2021 | 7     | 28  | 54       |

SELECT * FROM flights
    WHERE year = 2021
        AND month = 7
        AND day = 29
        ORDER BY hour LIMIT 5;

--+----+-------------------+------------------------+------+-------+-----+------+--------+
--| id | origin_airport_id | destination_airport_id | year | month | day | hour | minute |
--+----+-------------------+------------------------+------+-------+-----+------+--------+
--| 18 | 8                 | 6                      | 2021 | 7     | 29  | 16   | 0      |
--| 23 | 8                 | 11                     | 2021 | 7     | 29  | 12   | 15     |
--| 36 | 8                 | 4                      | 2021 | 7     | 29  | 8    | 20     |
--| 43 | 8                 | 1                      | 2021 | 7     | 29  | 9    | 30     |
--| 53 | 8                 | 9                      | 2021 | 7     | 29  | 15   | 20     |

--8 people, passport_number checked. TODO: phone_number & license plate, person_id
SELECT name FROM people
    WHERE passport_number IN (SELECT passport_number FROM passengers WHERE flight_id IN
(SELECT id FROM flights WHERE origin_airport_id = 8 AND year = 2021 AND month = 7 AND day = 29 AND hour = 8 AND minute = 20))
        AND phone_number IN (SELECT caller FROM phone_calls WHERE year = 2021 AND day = 28 AND month = 7 AND duration < 60)
        AND license_plate IN (SELECT license_plate FROM bakery_security_logs WHERE year = 2021 AND day = 28 AND month = 7 AND hour = 10 AND minute > 15 AND minute < 25)
        AND id IN (SELECT person_id FROM bank_accounts WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE year = 2021 AND month = 7 AND day = 28
        AND atm_location = 'Leggett Street'
        AND transaction_type = 'withdraw'))

--|  name  |
---+--------+
--BRUCE

SELECT full_name FROM airports -- CITY
    WHERE id IN (SELECT destination_airport_id FROM flights
    WHERE origin_airport_id = 8
        AND year = 2021 AND month = 7 AND day = 29 AND hour = 8 AND minute = 20)

--     full_name     |
--+-------------------+
--| LaGuardia Airport |

-- HEnce NEw York City

--ACCOmplice
SELECT name FROM people
    WHERE phone_number = (SELECT receiver FROM phone_calls
    WHERE caller = (SELECT phone_number FROM people WHERE name = 'Bruce')
        AND year = 2021
        AND day = 28
        AND month = 7
        AND duration < 60)