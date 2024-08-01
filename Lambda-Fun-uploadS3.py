import json
import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = 'vdubey-stsci'
    file_name = 'ec2_report.json'
    
    s3.put_object(
        Bucket=bucket_name,
        Key=file_name,
        Body=json.dumps(event),
        ContentType='application/json'
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('EC2 Report Uploaded')
    }
