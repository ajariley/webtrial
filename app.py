import flask
from flask import render_template


#this is to create an instance(__name__): Tells Flask where to look for files and resources.
app = flask.Flask(__name__)


#create a route deractor in url index.html is a route
#This line tells Flask, “When someone visits the /html URL, run the following function.”
@app.route('/html') 
def html_tutorial():
    return render_template('html_tutorial.html')


@app.route('/user/<name>') 
def user(name):
    first_name = "Everley"
    stuff = "This is <strong>Bold</strong> words"
    return render_template('user.html',user_name = name,stuff = stuff)#the second name comes from the path


#create an error page
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

#create  server Errorpage
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"),404




if __name__ == '__main__':
    app.run(debug=True)
