# from src.cmd_user_interface import CmdUserInterface
from src.csv_generators.top_30_csv_generator import * # importing file that will create our csv file from the specified url
import boto3
from botocore.exceptions import NoCredentialsError
import os
from aws_upload import upload_to_aws # importing the function that will upload file to aws

# the below functions will be run when we run our python main.py in the shell
if __name__ == '__main__':
    # CmdUserInterface()
    top_30 = ItJobsWatchHomePageTop30(itjobswatch_home_page_url())
    Top30CSVGenerator().generate_top_30_csv(top_30.get_top_30_table_elements_into_array(), os.path.expanduser('Downloads/'), 'ItJobsWatchTop30.csv', top_30.get_table_headers_array())

    # this function will take our csv file that will be stored in our downloads folder and push it to our s3 bucket, the details are specified below
    upload_to_aws('Downloads/ItJobsWatchTop30.csv', 'eng-67-shahrukh-devops', 'ItJobsWatchTop30.csv')

