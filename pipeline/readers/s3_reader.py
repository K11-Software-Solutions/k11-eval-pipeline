import boto3
def read_s3(bucket, key): return boto3.client('s3').get_object(Bucket=bucket, Key=key)['Body']
