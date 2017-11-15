from flask import Flask, session, redirect, url_for, escape, request, render_template, jsonify
from datetime import date
from data.DataFetcher import getData
from utilities.Utilities import validate_data,format_request


app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def main():
    if request.method == 'POST':
        data={}
        hotels=request.form.getlist('hotels')
        bdate = date(int(request.form['expiry-year']), int(request.form['expiry-month']),int(request.form['expiry-date']))
        data["rooms"] = request.form['room']
        data["quantity"] = request.form['quantity']
        data["duration"] = request.form['duration']
        data["bdate"]=bdate
        if not len(validate_data(data)):
            data['hotels']=hotels
            reqstr = format_request(data)
            return jsonify(getData(reqstr))
        else:
            return jsonify(validate_data(data))
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run()
