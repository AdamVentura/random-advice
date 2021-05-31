import praw
from flask import Flask, render_template, request
from authentication import authenticate
from get_tips import GetTips


# Create instance of app
app = Flask(__name__)    

# Call method to authenticate reddit scraper
reddit = authenticate()
# Call method to get list of tips
tips = GetTips(reddit)
# initialize count
count = 0

# Main route
@app.route("/", methods = ["GET", "POST"])
def generateTip():
    # Get global count
    global count 
    # If user clicks button, increment the count and render new template
    if request.method == "POST":
        count += 1
        return render_template('index.html', tips = tips, count = count)
    return render_template('index.html', tips = tips, count = 0)