from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def indexfac():
    return render_template("indexfac.html")

@app.route('/result',methods =["GET","POST"])
def factorial():
    if request.method == "POST":
        number1 = request.form.get("number1")
        number1 = int(input("İstediğiniz Sayıyı Giriniz... : "))
        factorial = 1
        if number1 < 0:
            print("Negatif sayılarda faktoriyel hesaplanma yapılmaz!!!")
        elif number1 == 0:
            print("0! = 1'dir." )    
        else:
            for i in range(1, number1 + 1):
                factorial = factorial * i
            return render_template("number.html",factorial = factorial )
    else:
        return render_template("number.html")


if __name__ == "__main__":
    app.run(debug=True)