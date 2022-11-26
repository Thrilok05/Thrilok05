from flask import Flask, request, render_template
import pymysql as psq

a=tuple()
app=Flask(__name__)

@app.route("/")
def first():
    return render_template("login.html")


@app.route("/", methods=["POST",'GET'])
def login():
    if request.method =="POST":
        name=request.form['usrnm']
        password=request.form['password']
        a=(name,password)
        db=psq.connect(host="localhost", user="root", password="", db="project")
        cur=db.cursor()
        qry="select mail, password from login"
        cur.execute(qry)
        nm=cur.fetchall()
        db.commit()
        db.close()
        for iden in nm:
            if name==iden[0] and password==iden[1]:
                return render_template("main.html",name=name,password=password)
            else:
                continue
            break
        return render_template("login.html", err=nm)
    else:
        return 'couldn/t login'


@app.route("/main", methods=["POST","GET"])
def main():
    if request.method=="POST":
        return render_template("main.html")


@app.route("/signup")
def signup():
    return render_template("signup.html")
'''
       

    

     # return render_template("main.html")



#@app.route("/main")
#def reroute():
'''
  









if __name__ == "__main__":
    app.run(debug=True)

