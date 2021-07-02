

from typing import get_args
from flask import Flask, render_template, request
from werkzeug.formparser import parse_form_data

app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")
        
@app.route('/result',methods =["GET","POST"])
def fibonacci():
    if request.method == "POST":
        number1 = request.form.get('number1')
        
        def fib(number1):
            point1 = 0
            point2 = 1

            print(point1)
            print(point2)

            for i in range(number1 - 2):
                point3 = point2 + point1
        
                print(point3)

                point1 = point2
                point2 = point3

        #number1 = int(input("Bir n değeri giriniz..."))

        #print("Girdiğiniz n değerine kadar Fibonacci dizisinin sonucu : ")

        #fib(number1) 
        
        
        return render_template("number.html", parse_form_data(fib(number1)))
    else:
        return render_template("number.html")   



if __name__ == "__main__":
    app.run(debug=True)







