from flask import *
from service import Services
from bson.objectid import ObjectId

app = Flask(__name__)
app.config['SECRET_KEY'] = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'


@app.route('/')
def homepage():
    return render_template('homepage.html')


@app.route('/all-service')
def all_service():
      if 'logged' in session :
            if session['logged']:
                  all_service = Services.find()
                  return render_template('all-service.html', all_people=all_service)
            else :
                  return redirect('/login')
      else :
            return redirect('/login')


@app.route('/all-service/detail/<id>')
def detail(id):
    detail_person = Services.find_one({"_id": ObjectId(id)})
    # print(detail_person)
    return render_template('detail_person.html', detail_person=detail_person)


@app.route('/all-service/<g>')
def gender(g):
    services = Services.find({"Gender": g})
    return render_template('all-service.html', all_people=services)


@app.route('/all-service/delete/<id>')
def delete(id):
    delete_person = Services.find_one({'_id': ObjectId(id)})
    Services.delete_one(delete_person)
    return redirect('/all-service')


@app.route('/all-service/update/<id>', methods=['GET', 'POST'])
def update(id):
    update_person = Services.find_one({'_id': ObjectId(id)})
    if request.method == "GET":
        return render_template('update_service.html', update_person=update_person)
    elif request.method == "POST":
        form = request.form
        print(form)
        service_name = form['input_name']
        service_age = form['input_age']
        service_Gender = form['input_Gender']
        service_available = form['input_available']
        service_height = form['input_height']
        service_address = form['input_address']
        new_value = {
            '$set': {
                'name': service_name,
                'Tuổi': service_age,
                'Gender': service_Gender,
                'available': service_available,
                'Height': service_height,
                'address': service_address
            }
        }
        Services.update_one(update_person, new_value)
        return redirect('/all-service/detail/{}'.format(id))


@app.route('/login', methods=["GET", "POST"])
def login():
      if session['logged'] == True :
            return redirect('/all-service')
      else :
            if request.method == 'GET':
                  return render_template('login.html')
            elif request.method == 'POST':
                  username = "admin"
                  password = "admin"
                  form = request.form
                  input_username = form['input_username']
                  input_password = form['input_password']
                  if input_username == username and input_password == password:
                        session["logged"] = True
                        return redirect('/all-service')
                  else:
                        return redirect('/login')

@app.route('/logout')
def logout():
      if 'logged' in session :
            session['logged'] = False
      return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)
