from flask import Flask, render_template,redirect,request
import pymysql as py
app=Flask(__name__)
@app.route("/")
def  show():
    try:
        db=py.Connect(host="localhost", user="root", password="",dbname="gohan")
        cur=db.cursor()
        sq="select * from customer"
        cur.execute(sq)
        data=cur.fetchall()
    except Exception as e:
        print("Error: {e}")
    return render_template("pageone.html")
@app.route("/about us")
def aboutus():
    return render_template("aboutus.html")
@app.route("/submit")
def submit():
    return redirect("/")
@app.route("/enter",methods=["POST"])
def enter():
    name=request.form["name"]
    mail=request.form["Email_id"]
    try:
        db=py.Connect(host='localhost',user='root',password='',database='requestdata')
        cur=db.cursor()
        sq2="insert complaints ('name', 'Email_id') values('{}','{}')".format(name,mail)
        cur.execute(sq2)
        db.commit()
    except Exception as e:
        print('Failed to update',e)
    return redirect('/submit')
app.run(debug=True)
