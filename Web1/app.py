from flask import Flask,render_template
app = Flask(__name__)



@app.route('/')
def index():
    return 'web ủa t'

@app.route('/say-yeah/<name>')
def sayyeah(name):

    return name 

@app.route('/sum/<int:a>/<int:b>')
def sum(a,b):
    return str(a + b)

@app.route('/poem')
def poem():
    poems = [
        {
            'title':'Thơ con cóc',
            'content':'abc',
            'author':'pop',
            'gender': 'female'
        },
        {
            'title':'Thơ con cho',
            'content':'hihihihii',
            'author':'Thai',
            'gender':'male'
        }
    ]

    return render_template('poem.html',poems =poems)
                             

if __name__ == '__main__':
  app.run(debug=True)
