from flask import Flask, render_template, redirect, url_for, request, session, flash, g
from functools import wraps
import csv

app = Flask(__name__)


@app.route("/")
def base():
    return render_template("homepage.html")


@app.route("/data", methods=['GET'])
def data():
    # /usr/src/app/Downloads
    with open('static/data/ItJobsWatchTop30.csv') as csv_file:
        data = csv.reader(csv_file, delimiter=',')
        jobs = []
        for row in data:
            jobs.append({
                "role": row[0],
                "rank": row[1],
                "rank_move": row[2],
                "median_salary": row[3],
                "hist_ads": row[4],
                "live_ads": row[5],
            })

    return render_template("datapage.html", jobs=jobs)


if __name__ == '__main__':
    app.run(debug=True)