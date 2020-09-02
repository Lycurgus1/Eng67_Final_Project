import boto3
from botocore.exceptions import NoCredentialsError
import os


def upload_to_aws(local_file, bucket, s3_file):
    aws_access_key = os.environ["AWS_ACCESS_KEY"]
    aws_secret_key = os.environ["AWS_SECRET_KEY"]
    s3 = boto3.client('s3',aws_access_key,
                      aws_secret_key)

    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False