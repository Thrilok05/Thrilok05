from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def main():
    return render_template('sidemain.html')

@app.route("/", methods=["POST"])
def form():
     service=request.form["service"]
     name=request.form.get["name"]
     return render_template('sidemain.html', service=service,name=name)



if __name__ == '__main__':
    app.run(debug=True)