# Data Persistency using S3 buckets


```commandline
sudo apt install awscli
```

- Allows us to put in our access and secret keys
```commandline
aws configure
```

- This lists evrehything inside the specified bucket
```commandline
aws s3 ls s3://eng-67-shahrukh-devops
```


```commandline
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Stmt1599125517479",
            "Effect": "Allow",
            "Principal": "",
            "Action": "s3:",
            "Resource": [
                # giving bucket level permissions --> so we can list what's in the bucket
                "arn:aws:s3:::eng-67-shahrukh-devops",
                # giving object level permissions --> we can edit the contents of a bucket (e.g. uplaod a file)
                "arn:aws:s3:::eng-67-shahrukh-devops/*"
            ]
        }
    ]
}
```

- Download python on our backend which will run the app which scraps the URL of the top 30 jobs and 
- using that script that runs every 3 hours it will constantly rerun

We had an issue where the flask application couldn't find the downloads folder which would contain the CSV that our front end would read from
- We overcame this by placing as downloads folder into the flask application, thus the app could read from it and then load the CSV successfully
