from flask import Flask, render_template, request


app = Flask(__name__)

import pickle

model = pickle.load(open(r"D:\IBM\model\model.pkl", 'rb'))


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/result.html', methods=['POST'])
def target():
    a = request.form['10']
    b = request.form['12']
    c = request.form['col']
    d = request.form['se']
    e = request.form['c']
    f = request.form['r']
    input = [[int(a), int(b), int(c), int(d), int(e), int(f)]]
    output = model.predict(input)
    output*=100
    print(output)

    return render_template("target.html", y= str(output[0][0]))


if __name__ == "__main__":
    app.run(debug=True)
