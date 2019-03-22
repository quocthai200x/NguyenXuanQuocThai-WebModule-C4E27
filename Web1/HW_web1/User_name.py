from flask import Flask, render_template

app = Flask(__name__)


@app.route('/user/<username>')
def users(username):
    users = {
        'thai': {
            'name': 'Thái',
            'gender': 'Nam',
            'age': 19,
            'hobbies': 'play game mạnh vl ',
            'story':'Unknown'
        },
        'quan': {
            'name': 'quân cờ hó :D',
            'gender': 'Both',
            'age': 'may be a baby , sometime an  adult',
            'hobbies': 'trêu người :) ',
            'story':'Unknown'
        },
        'nam':{
            'name':'Nam',
            'gender':'Nam',
            'age':19,
            'hobbies':'Anime for sure',
            'story':'vì tên là Nam nên có rất nhiều tai tiếng trên mạng :v'
        }

    }

    if not username in users:
        return 'User not found'

    else:
        user = users[username]
        return render_template('username.html', user=user)


if __name__ == '__main__':
    app.run(debug=True)
