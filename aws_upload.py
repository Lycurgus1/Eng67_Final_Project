
import boto3
import os



def upload_to_aws():

    ACCESS_KEY = os.environ["AWS_ACCESS_KEY"]
    SECRET_KEY = os.environ["AWS_SECRET_KEY"]

    s3_client = boto3.client(
            's3',
            aws_access_key_id=ACCESS_KEY,
            aws_secret_access_key=SECRET_KEY
        )

    s3_client.upload_file('Downloads/ItJobsWatchTop30.csv', 'eng-67-shahrukh-devops', 'ItJobsWatchTop30Automation3.csv')
    print("Your file has been successfully uploaded to an AWS bucket!")

