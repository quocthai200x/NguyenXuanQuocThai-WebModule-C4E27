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

@app.route('/poem')
def poem():
    return render_template('poem.html',poems =poems)


@app.route('/poem/<int:index>')
def detail(index):
    poem_detail = poems[index]
    return render_template('poem_detail.html',poem_detail=poem_detail, index = index + 1)

                             

if __name__ == '__main__':
    app.run(debug=True)
