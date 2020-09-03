from config_manager import itjobswatch_home_page_url
from src.itjobswatch_html_readers.itjobswatch_home_page_top_30 import ItJobsWatchHomePageTop30
from src.csv_generators.top_30_csv_generator import * # importing file that will create our csv file from the specified url

import os
from aws_upload import upload_to_aws # importing the function that will upload file to aws


# the below functions will be run when we run our python main.py in the shell
if __name__ == '__main__':
    # This function will run an API scrape that will grab the top 30 IT jobs and place it in a Downloads folder within our project in a CSV format
    top_30 = ItJobsWatchHomePageTop30(itjobswatch_home_page_url())
    Top30CSVGenerator().generate_top_30_csv(top_30.get_top_30_table_elements_into_array(), os.path.expanduser('Downloads/'), 'ItJobsWatchTop30.csv', top_30.get_table_headers_array())

    # this function will take our csv file that will be stored in our downloads folder and push it to our s3 bucket, the details are specified below
    upload_to_aws()

