from crypt import methods
from flask import Flask,jsonify
import csv

from matplotlib.animation import MovieWriter
all_movies=[]
like_movies=[]
not_like_movies=[]
didnot_watch_movie=[]
with open('movies.csv',encoding='utf-8')as f : 
    reader=csv.reader(f)
    data=list(reader)
    all_movies=data[1:]

app=Flask(__name__)

@app.route('/getmovies')
def getmovie():
    return jsonify({
        'data':all_movies
    })

@app.route('/likemovies',methods=['POST'])
def likemovie():
    movie=all_movies
    all_movies=all_movies[1:]
    like_movies.append(movie)
    return jsonify({
        'status':'success'
    })

@app.route('/unlikemovies',methods=['POST'])
def unlikemovie():
    movie=all_movies
    all_movies=all_movies[1:]
    not_like_movies.append(movie)
    return jsonify({
        'status':'success'
    })

@app.route('/didnotwatchmovies',methods=['POST'])
def didnotwatchmovie():
    movie=all_movies
    all_movies=all_movies[1:]
    didnot_watch_movie.append(movie)
    return jsonify({
        'status':'success'
    })

if __name__=='__main__':
    app.run()

