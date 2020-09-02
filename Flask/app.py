from flask import Flask, render_template, redirect, url_for, request, session, flash, g
from functools import wraps
import csv

from boto3.session import Session
import boto3


PORT=5000

app = Flask(__name__)


@app.route("/")
def base():
        
    ACCESS_KEY = 'ABC'
    SECRET_KEY = 'XYZ'

    session = Session(aws_access_key_id=ACCESS_KEY,
                aws_secret_access_key=SECRET_KEY)
    s3 = session.resource('s3')
    your_bucket = s3.Bucket('bucket_name')

    for s3_file in your_bucket.objects.all():
        print(s3_file.key) # prints the contents of bucket

    s3 = boto3.client ('s3')

    s3.download_file('your_bucket','k.png','/Users/username/Desktop/k.png')
    return render_template("homepage.html")


@app.route("/data", methods=['GET'])
def data():
    
    with open('/usr/src/app/Flask/static/data/ItJobsWatchTop30.csv') as csv_file:
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
    app.run(debug=True, host="0.0.0.0", port=PORT)