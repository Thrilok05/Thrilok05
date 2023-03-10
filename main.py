from flask import Flask, request, render_template
import pymysql
import datetime

app = Flask(__name__)


# Open MySQL connection
connection = pymysql.connect(host='localhost',user= 'root',password="",database="project")

# Create table if it doesn't exist
with connection.cursor() as cursor:
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS data (
            id INT NOT NULL AUTO_INCREMENT,
            data JSON NOT NULL,
            created_at DATETIME NOT NULL,
            PRIMARY KEY (id)
        )
    """)
connection.commit()

@app.route('/', methods=['POST'])
def create_data():
    if request.method=='POST':
        method='POST'
        return
    
    data = {'NAME':'Thrilok','PLACE':'Bangalore'}
    created_at = datetime.datetime.now()

    # Insert data into MySQL
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO data (data, created_at) VALUES (%s, %s)", (data, created_at))
    connection.commit()

    return render_template("index.html",data=data,method=method)

@app.route('/', methods=['GET'])
def get_data():
    # Retrieve all data from MySQL
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM data")
        data = cursor.fetchall()

    # Convert JSON string to Python object
    for row in data:
        row['data'] = data

    return render_template("index.html",data=data)


@app.route('/home',methods=['GET','POST'])
def home():
    return render_template("home.html")

@app.route('/about',methods=['GET','POST'])
def about():
    return render_template("about.html")

@app.route('/contact',methods=['GET','POST'])
def contact():
    return render_template("contact.html")








@app.route('/login')
def login():
    #name=request.form['usrnm']
    #password=request.form['password']
    #a=(name,password)
    db=pymysql.connect(host="localhost", user="root", password="", db="project")
    cur=db.cursor()
    qry="select mail, password from login"
    cur.execute(qry)
    nm=cur.fetchall()
    error="SORRY !! couldn't find the credentials"
    db.commit()
    db.close()
    #for iden in nm:
        #if name==iden[0] and password==iden[1]:
            #return render_template("login.html")
    return render_template("login.html")


@app.route("/main", methods=["POST","GET"])
def main():
    if request.method=="POST":
        return render_template("main.html")


@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/signup/", methods=["POST","GET"])
def create():
    name=request.form['usrnm']
    password=request.form['password']
    db=pymysql.connect(host="localhost", user="root", password="", db="project")
    cur=db.cursor()
    qry="INSERT INTO `login`(`mail`, `password`) VALUES ('%s','%s');"
    val=name,password
    cur.execute("INSERT INTO `login`(`mail`, `password`) VALUES ('{}','{}');".format(name,password))
    nm=cur.fetchall()
    db.commit()
    db.close()
    return render_template("acc.html", name=name, password=password)

  





if __name__ == '__main__':
    app.run(debug=True)
