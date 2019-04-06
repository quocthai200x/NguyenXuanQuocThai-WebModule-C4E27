from flask import *
from bike import bike_collection
app = Flask(__name__)

@app.route('/new_bike',methods = ['GET','POST'])
def bike_rental_service():
    if request.method == "GET":
        return render_template('bike-rental-service.html')
    elif request.method == "POST" :
        form = request.form
        print(form)
        bike_model = form['input_model']
        bike_fee = form['input_fee']
        bike_image = form['input_image']
        bike_year = form['input_year']
        add_bike =
            {
            'model':bike_model,
            'fee':bike_fee,
            'image':bike_image,
            'year':bike_year
            }
        bike_collection.insert_one(add_bike)
        return 'CONGRATULATIONs'



if __name__ == '__main__':
    app.run(debug=True)