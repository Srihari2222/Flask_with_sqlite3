from flask import *

app = Flask(__name__,template_folder='templates',static_folder='static')


@app.route("/", methods=['GET','POST'])
def home():
    if request.method=='POST':
        select=request.form['page']
        return redirect(url_for(f'{select}'))
    return render_template("home.html")
database={"kataresrihari@gmail.com":["9849403317","Srihari","Katare"]}

@app.route("/signup", methods=['GET','POST'])
def signup():
    if request.method=='POST':
        fname = request.form['fname']
        lname=request.form['lname']
        email=request.form['email']
        pwd1 = request.form['password1']
        pwd2 = request.form['password2']
        if pwd1 != pwd2:
            return render_template("signup.html", pwd="Please Enter Correct Password")
        else:
            if email not in database:
                database[email]=[pwd1,fname,lname]
            return redirect(url_for("signup_success",sss=email))
    return render_template("signup.html")


@app.route("/login",methods=['GET','POST'])
def login():
    if request.method=='POST':
        email = request.form['email']
        pas = request.form['password']
        if email not in database:
            return render_template("login.html",pwd="Please Enter Valid Email")
        elif pas!=database[email][0]:
            return render_template("login.html",pwd="Please Enter Correct Password")
        return redirect(url_for("login_success",pas=email))
    return render_template("login.html")
@app.route("/loginsuccess<pas>",methods=['GET','POST'])
def login_success(pas):
    if request.method=='GET':
        temp = database[pas]
        return render_template("loginsuccess.html",name=temp[1])
    if request.method=='POST':
        return redirect(url_for("profile",usr=pas))
    return render_template("loginsuccess.html")
@app.route("/signupsuccess<sss>", methods=['GET', 'POST'])
def signup_success(sss):
    if request.method=='GET':
        temp=database[sss]
        return render_template("signupsuccess.html",name=temp[1])
    if request.method=='POST':
        return redirect(url_for("profile",usr=sss))
    return render_template("signupsuccess.html")
@app.route("/profile<usr>",methods=['GET','POST'])
def profile(usr):
    temp=database[usr]
    if request.method=='GET':
        return render_template("profile.html",fname=temp[1],lname=temp[2],email=temp[1],password=temp[0])
    if request.method=='POST':
        return redirect(url_for("home"))
    return render_template("profile.html")
@app.route("/username/<name>/<int:number>")
def hello(name,number):
    return f"Hello {name} and {number}"
if __name__=="__main__":
    app.run(debug=True,port=3000)