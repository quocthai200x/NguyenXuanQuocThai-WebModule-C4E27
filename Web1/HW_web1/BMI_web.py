from flask import Flask,render_template

app = Flask(__name__)

@app.route('/bmi1/<int:weight>/<int:height>')
def BMI_1(weight,height):
    height1 = height/100
    BMI = weight/(height1*height1)
    if BMI < 16 :
       BMI = 'your BMI :'+str('%.2f'% BMI)+' -> you are severely underweight'
    elif 16 <= BMI < 18.5 :
        BMI = 'your BMI :'+str('%.2f'%BMI)+' -> you are underweight'
    elif 18.5 <= BMI <25 :
        BMI = 'your BMI :'+str('%.2f'%BMI) +' -> you are normal'

    elif 25 <= BMI <30 :
        BMI = 'your BMI :'+str('%.2f'%BMI)+' -> you are overweight'
    else : 
        BMI = 'your BMI :'+str('%.2f'%BMI)+' -> you are obese'
    return render_template('BMI.html',BMI = BMI)




@app.route('/bmi2/<int:weight>/<int:height>')
def BMI_2(weight,height):
    height1 = height/100
    BMI = weight/(height1*height1)
    if BMI < 16 :
       return 'your BMI :'+str('%.2f'% BMI)+' -> you are severely underweight.'
    elif 16 <= BMI < 18.5 :
        return 'your BMI :'+str('%.2f'%BMI)+' -> you are underweight.'
    elif 18.5 <= BMI <25 :
        return 'your BMI :'+str('%.2f'%BMI) +' -> you are normal.'
        
    elif 25 <= BMI <30 :
        return 'your BMI :'+str('%.2f'%BMI)+' -> you are overweight.'
    else : 
        return 'your BMI :'+str('%.2f'%BMI)+' -> you are obese.'
    

if __name__ == '__main__':
  app.run(debug=True)