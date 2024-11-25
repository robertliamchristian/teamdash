from flask import Flask, render_template
import timbers 
import mets  
import blazers

app = Flask(__name__)

@app.route('/')
def index():
    timbers_posts = timbers.timbers_bsky_feed()
    mets_posts = mets.mets_bsky_feed()
    blazers_posts = blazers.blazers_bsky_feed()

    return render_template('index.html', timbers_posts=timbers_posts, mets_posts=mets_posts, blazers_posts=blazers_posts)

if __name__ == '__main__':
    app.run(debug=True)
