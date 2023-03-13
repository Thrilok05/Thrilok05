from flask import Flask, request, render_template
import pymysql as pql


app = Flask(__name__)
connection = pql.connect(host='localhost',user='root',password='',database='project',)

cur=connection.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS data (id INT NOT NULL AUTO_INCREMENT,name varchar(16) NOT NULL,Email varchar(30) NOT NULL,PRIMARY KEY (id))")
connection.commit()


@app.route("/", methods=["POST"])
def main():
    
    return render_template('sidemain.html')

@app.route("/home",methods=["post","get"])
def remain():
    if request.method=="post":
        name=request.form["name"]
        email=request.form["email"]
        with connection:
            with connection.cursor() as cursor:
                qry="INSERT INTO data(name,email) values(%s,%s)"
                cursor.execute(qry,(name,email))
    else:
        name=request.form.get("name")
        email=request.form.get("email")
        qry="INSERT INTO data(name,email) values(%s,%s)"
        cursor.execute(qry,(name,email))
    connection.commit()
          
    return f"name: {name}\nemail: {email}"

if __name__ == '__main__':
    app.run(debug=True)
