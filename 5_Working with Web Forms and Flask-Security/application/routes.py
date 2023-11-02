from application import app, db
from flask import render_template, request, json, Response, redirect, flash, url_for
from application.models import User, Course, Enrollment
from application.forms import LoginForm, RegisterForm

'''courseData = [{"courseID":"1111","title":"PHP 111", "description":"Intro to PHP", "credits" : "3", "term":"Fall, Spring"},
                  {"courseID":"2222","title":"Java 1", "description":"Intro to Java Programming", "credits" : "4", "term":"Spring"}, 
                  {"courseID":"3333","title":"Adv PHP 201", "description":"Advanced PHP Programming", "credits" : "3", "term":"Fall"},
                  {"courseID":"4444","title":"Angular 1", "description":"Intro to Angular", "credits" : "3", "term":"Fall, Spring"},
                  {"courseID":"5555","title":"Java 2", "description":"Advanced Java Programming", "credits" : "4", "term":"Fall"}]
'''



@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html", index = True)

@app.route("/login", methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User.objects(email=email).first()
        if user and user.get_password(password):
            flash(f"{user.first_name},You are successfully logged in!", "success")
            return redirect("/index")
        else:
            flash("Sorry, Something went wrong.", "danger")
    return render_template("login.html", title="Login", form=form, login = True)

@app.route("/courses/", methods = ['GET', 'POST'])
@app.route("/courses/<term>", methods = ['GET', 'POST'])
def courses(term=None):
    if(term == None):
        term = "Spring 2019"

    classes = Course.objects.all()
    print(classes)

    return render_template("courses.html", courseData = classes, courses = True, term=term)
    # We should change courseData=courseData part!
    # Now we are collecting the data from DB





@app.route("/register", methods = ['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user_id = User.objects.count()
        user_id += 1

        email = form.email.data
        password = form.password.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        
        user = User(user_id = user_id, email=email, first_name=first_name, last_name=last_name)
        user.set_password(password) #Hashed
        user.save()
        flash("You are successfully registered!","success")
        return redirect(url_for('index'))
    return render_template("register.html", title="Register", form=form, register = True)
    #If validation failed, return back to the register form.


@app.route("/enrollment", methods=["GET", "POST"])
def enrollment():
    id = ""
    title = ""
    term = ""
    if (request.method == "POST"):
        id = request.form.get('courseID')
        print(request.args)
        title = request.form.get('title')
        term = request.form.get('term')   
    else:
        id = request.args.get('courseID')
        print(request.args)
        title = request.args.get('title')
        term = request.args.get('term')    
    return render_template("enrollment.html", enrollment = True, data={"id":id, "title":title, "term": term})

@app.route("/api/")
@app.route("/api/<idx>")
def api(idx=None):
    if(idx == None):
        jdata = courseData
    else:
        jdata = courseData[int(idx)]
    return Response(json.dumps(jdata), mimetype="application/json")



@app.route("/user")
def user():
    #User(user_id=1, first_name="Hyeyoung", last_name="Kim", email="hyeyokim@cisco.com").save()
    #User(user_id=2, first_name="Lucia", last_name="Kim", email="hyeyokim@cisco.com").save()
    users = User.objects.all()
    return render_template("users.html", users=users)