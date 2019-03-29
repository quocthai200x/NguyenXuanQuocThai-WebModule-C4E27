from flask import Flask, render_template , redirect
from service import Services
from bson.objectid import ObjectId

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('homepage.html')



@app.route('/all-service')
def all_service():
      all_service = Services.find()
      return  render_template('all-service.html', all_people = all_service)

@app.route('/all-service/detail/<id>')
def detail(id):
    detail_person = Services.find_one({"_id":ObjectId(id)})
    # print(detail_person)
    return render_template('detail_person.html',detail_person = detail_person)

@app.route('/all-service/<g>')
def gender(g):
    services = Services.find({"Gender":g})
    return render_template('all-service.html',all_people = services)

@app.route('/all-service/delete/<id>')
def delete(id):
    delete_person = Services.find_one({'_id':ObjectId(id)})
    Services.delete_one(delete_person)
    return redirect('/all-service')



if __name__ == '__main__':
  app.run(debug=True)
 