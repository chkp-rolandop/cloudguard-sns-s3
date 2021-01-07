import boto3

print('Loading function')

def lambda_handler(event, context):
    #s3prefix is the prefix will be used in the filename
    s3prefix = 'CloudGuardAlerts-'
    
    #ext is the extension for the filename
    ext = '.json'
    
    #s3_bucket is the name of the s3 bucket to write the files to 
    #THIS VALUE MUST BE CHANGED
    s3_bucket = 'your-s3-bucket'
    
    #Pulling timestamp and message from SNS message
    timestamp = event['Records'][0]['Sns']['Timestamp']
    message = event['Records'][0]['Sns']['Message']
    
    #Building Filename
    filename = s3prefix + timestamp + ext

    #Writing message to s3 bucket using filename created
    try:
        s3 = boto3.client('s3')
        s3.put_object(Bucket=s3_bucket, Key=filename, Body=message)
        return 'Event stored'
    except:
        raise
