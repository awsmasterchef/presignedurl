import json
import boto3
import botocore

s3 = boto3.client('s3'
                  ,endpoint_url='https://s3.us-east-2.amazonaws.com',
                  region_name='us-east-2')


def lambda_handler(event, context):
    bucket_name = 'awsmasterchef-resources'
    object_key = 'fastapi.png'
    
    try:
        # Generate a pre-signed URL that is valid for 1 hour
        url = s3.generate_presigned_url(
            ClientMethod='get_object',
            Params={'Bucket': bucket_name, 'Key': object_key},
            ExpiresIn=20  # Set the expiration time in seconds (e.g., 3600 seconds = 1 hour)
        )
        # print("Pre-signed URL:", url)
        return {
            'statusCode': 200,
            'body': url
        }
    except botocore.exceptions.ClientError as e:
        print("Error generating pre-signed URL:", e)
