from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    id = session["user_id"]
    portfolio = db.execute("SELECT * FROM Portfolio WHERE id=:id",id=id)
    # print(portfolio)
    if portfolio == []:
        return render_template("default.html")
    rows = db.execute("SELECT cash FROM users WHERE id=:id",id=id)
    cash = float(rows[0]["cash"])
    # print(id)
    # print(portfolio)
    # print(rows)
    # print(cash)
    # print(portfolio[0])
    sum = 0
    i = 0
    for i in portfolio:
        quote = lookup(i['symbol'])
        # print(quote)
        if quote == None:
            return redirect("/")
        share = float(i['shares'])
        price = float(quote["price"])
        total = price * share
        sum = sum + total
    sum = sum + cash
    sum = round(sum,2)
    return render_template("index.html",portfolio=portfolio,cash=cash,sum=sum)
    # return apology("TODO")


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        # Ensure symbol was submitted
        if not request.form.get("symbol"):
            return apology("must provide symbol", 403)
        elif not request.form.get("shares"):
            return apology("must provide shares", 403)
        quote = lookup(request.form.get("symbol"))
        if quote == None:
            return apology("Stock not found!", 403)
        # Query database for user
        rows = db.execute("SELECT cash FROM users WHERE id = :id",id= session["user_id"])
        cash = float(rows[0]["cash"])
        new_shares = float(request.form.get("shares"))
        price = float(quote["price"])
        total = new_shares * price
        # print(rows[0]["cash"])
        # print(new_shares)
        # print(price)
        # print(total)
        if cash >= total:
            symbol = request.form.get("symbol")
            name = quote["name"]
            db.execute("INSERT INTO History (type,stocksymbol,stockshares,price,total,id) VALUES (:type,:stocksymbol,:stockshares,:price,:total,:id)",type="Bought",stocksymbol= symbol,stockshares= new_shares, price= price,total=total, id= session["user_id"])
            db.execute("UPDATE users SET cash = :diff WHERE id= :id",diff = float(rows[0]["cash"]) - total,id= session["user_id"])
            rows = db.execute("SELECT symbol FROM Portfolio WHERE symbol = :symbol AND id= :id",symbol= symbol,id= session["user_id"])
            # print (rows)
            if rows == []:
                db.execute("INSERT INTO Portfolio (id,symbol,name,shares,price,total) VALUES (:id,:symbol,:name,:shares,:price,:total)",id= session["user_id"],symbol= symbol,name= name,shares= new_shares, price= price,total=total)
            else:
                rows = db.execute("SELECT * FROM Portfolio WHERE symbol = :symbol AND id= :id",symbol= symbol,id= session["user_id"])
                # print(rows)
                db.execute("UPDATE Portfolio SET shares = :diff WHERE id= :id AND symbol= :symbol",diff = rows[0]["shares"] + new_shares,id= session["user_id"],symbol= symbol)
                db.execute("UPDATE Portfolio SET price = :diff WHERE id= :id AND symbol= :symbol",diff = price,id= session["user_id"],symbol= symbol)
                db.execute("UPDATE Portfolio SET total = :diff WHERE id= :id AND symbol= :symbol",diff = rows[0]["total"] + total,id= session["user_id"],symbol= symbol)

        else:
            return apology("Not enough cash",400)
        # Redirect user to home page
        return redirect("/")
    else:
        return render_template("buy.html")
    #return apology("TODO")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    _id = session["user_id"]
    history = db.execute("SELECT * FROM History WHERE id=:_id",_id=_id)
    #print(history)
    return render_template("history.html",history=history)
    #return apology("TODO")

@app.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    if request.method == "POST":
        return render_template("passchange.html")
    else:
        _id = session["user_id"]
        user = db.execute("SELECT * FROM users WHERE id=:_id",_id=_id)
        name = user[0]['username']
        cash = user[0]['cash']
        return render_template("profile.html",name=name,cash=cash)
    # return apology("TODO")

@app.route("/passchange", methods=["GET", "POST"])
@login_required
def change():
    """Show profile of user"""
    _id = session["user_id"]
    user = db.execute("SELECT * FROM users WHERE id=:_id",_id=_id)

    if not request.form.get("oldpass"):
        return apology("Missing Old password!", 403)

    # Ensure password was submitted
    if not request.form.get("password"):
        return apology("Missing password!", 403)

    # Ensure confirmation password was submitted
    if not request.form.get("confirmation_password"):
        return apology("Missing confirmation passoword!", 403)

    if len(user) != 1 or not check_password_hash(user[0]["hash"], request.form.get("oldpass")):
            return apology("invalid old password", 403)

    # Ensure password and confirmation passwords are the same
    if request.form.get("password") != request.form.get("confirmation_password"):
        return apology("your passwords are not matched",403)

    password = request.form.get("password")
    hashed = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
    db.execute("UPDATE users SET hash =:updatedhash",updatedhash= hashed)
    return redirect("/")
    # return apology("TODO")


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
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

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
    if request.method == "POST":
        if not request.form.get("stockname"):
            return apology("Missing stock name!", 403)
        quote = lookup(request.form.get("stockname"))
        if quote == None:
            return apology("Stock not found!", 403)
        else:
            # print(quote)
            name = quote["name"]
            price = usd(quote["price"])
            symbol = quote["symbol"]
            return render_template("stock.html",name=name,price=price,symbol=symbol)
    else:
        return render_template("quote.html")
    #return apology("TODO")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("Missing username!", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("Missing password!", 403)

        # Ensure confirmation password was submitted
        elif not request.form.get("confirmation_password"):
            return apology("Missing confirmation passoword!", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username does not exist
        if rows != []:
            return apology("username is already registered",403)

        # Ensure password and confirmation passwords are the same
        if request.form.get("password") != request.form.get("confirmation_password"):
            return apology("your passwords are not matched",403)

        # Insert Date in Database
        password = request.form.get("password")
        hash = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
        db.execute("INSERT INTO users (username,hash) VALUES (:username,:hash)",username=request.form.get("username"),hash=hash)

        # Remember which user has logged in
        new = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))
        session["user_id"] = new[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")
    # return apology("TODO")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure symbol was submitted
        if not request.form.get("symbol"):
            return apology("Missing symbol!", 403)

        # Ensure shares was submitted
        elif not request.form.get("shares"):
            return apology("Missing shares!", 403)

        id = session["user_id"]
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")
        # print(symbol)
        # print(shares)
        portfolio = db.execute("SELECT * FROM Portfolio WHERE id=:id AND symbol=:symbol",id=id,symbol=symbol)
        # print(portfolio)
        cash = db.execute("SELECT cash FROM users WHERE id=:id",id=id)
        diff = int(portfolio[0]["shares"]) - int(shares)
        # print(diff)
        if diff < 0:
            return apology("You don't have enough stocks",400)
        elif diff == 0:
            quote = lookup(symbol)
            #print(quote)
            price = float(quote["price"])
            total = price * float(shares)
            #print(cash)
            money = cash[0]['cash']
            #print(money)
            summ = money + total
            #print(summ)
            db.execute("UPDATE users SET cash =:updatedcash",updatedcash= float(summ))
            db.execute("DELETE FROM Portfolio WHERE id= :id AND symbol= :symbol",id=id,symbol= symbol)
            db.execute("INSERT INTO History (type,stocksymbol,stockshares,price,total,id) VALUES (:type,:stocksymbol,:stockshares,:price,:total,:id)",type="Sold",stocksymbol=symbol,stockshares=shares,price=price,total=total,id=id)
        else:
            quote = lookup(symbol)
            price = float(quote["price"])
            total = price * float(shares)
            updatedtotal = price * float(diff)
            money = cash[0]['cash']
            summ = money + total
            db.execute("UPDATE users SET cash =:updatedcash",updatedcash= float(summ))
            db.execute("UPDATE Portfolio SET shares=:updatedshares WHERE id= :id AND symbol= :symbol",updatedshares=diff,id=id,symbol= symbol)
            db.execute("UPDATE Portfolio SET price=:updatedprice WHERE id= :id AND symbol= :symbol",updatedprice=price,id=id,symbol= symbol)
            db.execute("UPDATE Portfolio SET total=:updatedtotal WHERE id= :id AND symbol= :symbol",updatedtotal=updatedtotal,id=id,symbol= symbol)
            db.execute("INSERT INTO History (type,stocksymbol,stockshares,price,total,id) VALUES (:type,:stocksymbol,:stockshares,:price,:total,:id)",type="Sold",stocksymbol=symbol,stockshares=shares,price=price,total=total,id=id)
        return redirect("/")
    else:
        id = session["user_id"]
        portfolio = db.execute("SELECT * FROM Portfolio WHERE id=:id",id=id)
        return render_template("sell.html",portfolio=portfolio)
    # return apology("TODO")


def errorhandler(e):
    """Handle error"""
    return apology(e.name, e.code)


# listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
