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
        v4 = int(request.form["inp4"])
        v5 = int(request.form["inp5"])
        v6 = int(request.form["inp6"])
        v7 = int(request.form["inp7"])
        v8 = int(request.form["inp8"])
        v9 = int(request.form["inp9"])
        v10 = int(request.form["inp10"])
        v11 = int(request.form["inp11"])


        y_pred = model.predict([[v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11]])
        y_pred = round(y_pred[0], 2)

    return render_template('result.html', result=y_pred)

if __name__ == '__main__':
    app.run(debug=True)