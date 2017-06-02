from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname':'rechie'}
    posts = [
            {
                'author':{'nickname':'john'},
                'body':'Beautiful day in Portland!'
            },
            {
                'author':{'nickname':'john'},
                'body':'The Avengers movie was so cool!'
            }
    ]
    return render_template("index.html", 
            title = 'Home', 
            user=user, 
            posts = posts)

