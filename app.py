from flask import Flask, render_template
import timbers  # Importing the module that fetches the Bluesky feed for Timbers
import mets  # Importing the module that fetches the Bluesky feed for Mets
import blazers

app = Flask(__name__)

@app.route('/')
def index():
    # Fetch the Timbers feed
    timbers_posts = timbers.timbers_bsky_feed()
    mets_posts = mets.mets_bsky_feed()
    blazers_posts = blazers.blazers_bsky_feed()

    # Pass both Timbers and Mets posts to the HTML template
    return render_template('index.html', timbers_posts=timbers_posts, mets_posts=mets_posts, blazers_posts=blazers_posts)

if __name__ == '__main__':
    app.run(debug=True)
