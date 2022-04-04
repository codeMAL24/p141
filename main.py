from flask import Flask , jsonify , request
import csv 

all_articles = []
with open('articles.csv' , encoding='utf-8') as f:
    r = csv.reader(f)
    data = list(r)
    all_articles = data[1:]

liked_articles = []
not_liked_articles = [] 

app = Flask(__name__) 
@app.route("/")   

def homepage():
    return "Welcome"

@app.route('/get-articles') 
def getmovie():
    return jsonify({
        "data" : all_articles[0],
        "status" : "success!"
    })   

@app.route('/liked-articles',methods = ["POST"])

def likedmovie():
    global all_articles
    movie = all_articles[0]
   
    liked_articles.append(movie)
    all_articles.pop(0)
    return jsonify({
        "status" : "success!"
    }),200

@app.route('/unliked-articles',methods = ["POST"])

def unlikedmovie():
    global all_articles
    movie = all_articles[0]
 
    not_liked_articles.append(movie)
    all_articles.pop(0)
    return jsonify({
        "status" : "success!"
    }),200

if __name__ == "__main__":
    app.run(debug = True)  