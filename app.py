from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route("/") #Root 주소
def hello():
    return "<h1>서버를 띄웠다.</h1>"
    
@app.route("/html_tag") #주소/html_tag  <url을 구분>
def html_tag():
    return """
    <h1>첫번 째 줄!!!!</h1>
    <h2>두번 째 줄!!!!</h2>
    """
    
@app.route("/html_file")    #html_file 요청이 있으면 html_file을 보내준다
def html_file():
    return render_template("html_file.html")
    
@app.route("/welcome/<string:name>")
def welcome(name):
    return render_template("welcome.html",people = name)
    
@app.route("/cube/<int:num>")
def cube(num):
    return render_template("cube.html",cub = num**3)
    
@app.route("/lunch")
def lunch():
    menu = ['양식','중식','한식','일식']
    choice = random.choice(menu)
    return render_template("lunch.html",lc = choice)
    
@app.route("/lotto")
def lotto():
    num = list(range(1,46))
    a = random.sample(num,6)
    sort_pick = sorted(a)
    return render_template("lotto.html",a = sort_pick)
    
@app.route("/naver")
def naver():
    return render_template("naver.html")
    
@app.route("/google")
def google():
    return render_template("google.html")
    