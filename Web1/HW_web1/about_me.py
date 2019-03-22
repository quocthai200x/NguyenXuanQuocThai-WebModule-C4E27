from flask import Flask,render_template,redirect
import os
app = Flask(__name__)
@app.route('/')
def index():
    return 'đây là web về t :)'
@app.route('/about-me')
def about_me():
    about_me = {
        'name':'Thái', 
        'work':'fresh man', 
        'school':'HUST',
        'hobbies':'play game for sure'
    }
    return render_template('aboutme.html',about_me = about_me)

@app.route('/school')
def school():
    return redirect("http://techkids.vn")

if __name__ == '__main__':
  app.run(debug=True)
