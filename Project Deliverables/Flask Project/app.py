from flask import Flask, render_template, request
import requests
# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "JBX6vwRnxH6V4GWtAvMTh35BEf-Up0FQ_A5GV4XWj3Cs"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]
header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}
app = Flask(__name__)
@app.route('/')
def home():
    return render_template("index.html")
@app.route('/target.html', methods=['POST'])
def target():
    a = request.form['10']
    b = request.form['12']
    c = request.form['col']
    d = request.form['se']
    e = request.form['c']
    f = request.form['r']
    input = [[int(a), int(b), int(c), int(d), int(e), int(f)]]
    payload_scoring = {
        "input_data": [{"fields": [['f0', 'f1', 'f2', 'f3', 'f4', 'f5']], "values": input}]}
    response_scoring = requests.post(
        'https://us-south.ml.cloud.ibm.com/ml/v4/deployments/06ad8c07-52a3-476a-8055-23d78822b834/predictions?version=2022-11-17',
        json=payload_scoring,
        headers={'Authorization': 'Bearer ' + mltoken})
    print("Scoring response")
    print(response_scoring.json())
    pred = response_scoring.json()
    output = pred['predictions'][0]['values'][0][0]
    print(output)
    return render_template("Result.html", y= str(output))
if __name__ == "__main__":
    app.run(debug=True)
