from flask import Flask,render_template,request,redirect
from scrappers.manganelo import manganelo

app = Flask(__name__)

@app.route('/home')
@app.route("/")
def home():
    return redirect("/search/Black Clover")#render_template("index.html")

@app.route("/login")
def login(): 
  return render_template("login.html")

@app.route('/manga')
def manga():
    id = request.args.get("id")
    name = request.args.get("name")
    img = request.args.get("img")
    data = manganelo.getChapters(id)
    return render_template("manga.html",name=name,data = data, img=img )

@app.route("/search/<string:query>")
def search(query): 
  data = manganelo.search(query)
  return render_template("search.html", q = data)

@app.route("/chapter")
def chapters():
  link = request.args.get("link")
  data = manganelo.getManga(link)
  return render_template("chapters.html", data= data)

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=8000)
    