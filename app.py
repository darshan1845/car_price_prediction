from flask import Flask, render_template, request
import pickle
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        v1 = int(request.form["inp1"])
        v2 = float(request.form["inp2"])
        v3 = int(request.form["inp3"])
        v4 = request.form["inp4"]
        v5 = int(request.form["inp5"])
        v6 = request.form["inp6"]
        v7 = request.form["inp7"]
        v8 = request.form["inp8"]
        v9 = request.form["inp9"]
        v10 = int(request.form["inp10"])
        v11 = request.form["inp11"]

        # Fuel type
        if v4 == 'Diesel':
            v4 = 0
        elif v4 == 'Electric':
            v4 = 1
        else:
            v4 = 2

        # Brand
        if v6 == "BMW":
            v6 = 0
        elif v6 == "Chevrolet":
            v6 = 1
        elif v6 == "Ford":
            v6 = 2
        elif v6 == "Honda":
            v6 = 3
        elif v6 == "Hyundai":
            v6 = 4
        elif v6 == "Kia":
            v6 = 5
        elif v6 == "Nissan":
            v6 = 6
        elif v6 == "Tesla":
            v6 = 7
        elif v6 == "Toyota":
            v6 = 8
        else :
            v6 = 9

        # Transmission type
        if v7 == "Automatic":
            v7 = 0
        else:
            v7 = 1

        #Colour
        if v8 == "Black":
            v8 = 0
        elif v8 == "Blue":
            v8 = 1
        elif v8 == "Gray":
            v8 = 2
        elif v8 == "Red":
            v8 = 3
        elif v8 == "Silver":
            v8 = 4
        else:
            v8 = 5

        #Service history
        if v9 == "Full":
            v9 = 0
        elif v9 == "No_History":
            v9 = 1
        else:
            v9 = 2

        #Insurance
        if v11 == "No":
            v11 = 0
        else:
            v11 = 1

        y_pred = model.predict([[v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11]])
        y_pred = round(y_pred[0], 2)

    return render_template('result.html', result=y_pred)

if __name__ == '__main__':
    app.run(debug=True)