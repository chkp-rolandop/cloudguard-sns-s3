import boto3

print('Loading function')

def lambda_handler(event, context):
    s3prefix = 'CloudGuardAlerts-'
    ext = '.json'
    s3_bucket = 'cg-seim-bucket'
    
    timestamp = event['Records'][0]['Sns']['Timestamp']
    message = event['Records'][0]['Sns']['Message']
    
    filename = s3prefix + timestamp + ext

    try:
        s3 = boto3.client('s3')
        s3.put_object(Bucket=s3_bucket, Key=filename, Body=message)
        return 'Event stored'
    except:
        raise
