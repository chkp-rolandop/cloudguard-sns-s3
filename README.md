# cloudguard-sns-s3

This is a lambda function made to transfer SNS messages to s3.  

## Usage:

Update the relevant fields in the IAM role and python file. Your Trigger for the lambda should be set to an SNS Topic.

### lambda-sns-to-s3.py

Modify the following variables:

s3prefix (optional)

s3_bucket (required):  This is the name of your s3 bucket

### IAMRole.json

This is a sample execution role for your lambda function.

Modify the following fields and remove the brackets []:

\[your-s3-bucket-arn\]

\[your-s3-bucket-arn\]

\[your-logs-arn\]


Example:

        {
            "Effect": "Allow",
            "Action": [
                "s3:PutObject"
            ],
            "Resource": [
                "[your-s3-bucket-arn]/*"
            ]
        }
        
   Would change to:
 
         {
            "Effect": "Allow",
            "Action": [
                "s3:PutObject"
            ],
            "Resource": [
                "arn:aws:s3:::my-s3-bucket/*"
            ]
        }
