from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# ===== DATABASE CONNECTION =====
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Bhanu@123",
    database="petcare"
)

cursor = conn.cursor()
print("Database connected ✅")

# ================= HOME =================
@app.route("/")
def homePage():
    return render_template("Home.html")

# ================= LOGIN =================
@app.route("/login", methods=['POST'])
def loginform():
    userEmail = request.form.get("email")
    userpassword = request.form.get("password")

    sql = "SELECT * FROM sign_up WHERE email=%s"
    cursor.execute(sql, (userEmail,))
    user = cursor.fetchone()

    if user:
        stored_password = user[3]  # id, name, email, password

        if check_password_hash(stored_password, userpassword):
            return redirect(url_for('vaccination'))
        else:
            return "Wrong Password ❌"
    else:
        return "User Not Found ❌"

# ================= SIGNUP =================
@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/signup", methods=['POST'])
def submitForm():
    userName = request.form.get("name")
    userEmail = request.form.get("email")
    userpassword = request.form.get("password")

    hashed_password = generate_password_hash(userpassword)

    sql = "INSERT INTO sign_up(name, email, password) VALUES(%s, %s, %s)"
    cursor.execute(sql, (userName, userEmail, hashed_password))
    conn.commit()

    return redirect(url_for('homePage'))

# ================= SHOP =================
@app.route("/shophm")
def shop():
    products = [
        {"name": "Product 1", "price": 200, "image": "p1.jpg"},
        {"name": "Product 2", "price": 500, "image": "p2.jpg"},
        {"name": "Product 3", "price": 900, "image": "p3.jpg"},
    ]
    return render_template("shophm.html", products=products)

# ================= OTHER PAGES =================
@app.route("/vaccination")
def vaccination():
    return render_template("vacination.html")

@app.route("/about")
def aboutus():
    return render_template("about.html")


@app.route("/vacihnation")
def vacihnation():
    return render_template("vacihnation.html")

@app.route("/vacinationschedule")
def vacinationschedule():
    return render_template("vacinationschedule.html")
@app.route("/consultvet")
def counsultvet():
    return render_template("consultvet.html")

@app.route("/shopbybreed")
def shopbreed():
    return render_template("shopbybreed.html")



# ================= RUN =================
if __name__ == "__main__":
    app.run(debug=True)