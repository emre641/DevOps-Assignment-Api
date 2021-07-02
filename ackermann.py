from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")
        
@app.route('/result',methods =["GET","POST"])
def ackermann():
    if request.method == "POST":
         x = request.form.get("number1")
         y = request.form.get("number2")
        return render_template("numberAckermann.html",ack_cal(x,y))




def ack_cal(x,y):
    if x == 0:
        print(y+1)
        return y + 1
    
    elif x > 0 and y == 0:
        print("Ackermann(", x-1,",",1,")")
        return ackermann(x - 1, 1)

    elif x > 0 and y > 0:
        print("Ackermann(",x-1,",","Ackermann(",x,",",y - 1,")",")")
        return ackermann(x - 1, ackermann(x, y -1))

#point1 = int(input("Lütfen birinci sayıyı giriniz..."))        
#point2 = int(input("Lütfen ikinci sayıyı giriniz..."))

#ackermann(point1, point2)


if __name__ == "__main__":
    app.run(debug=True)