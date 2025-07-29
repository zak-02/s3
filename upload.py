import boto3
import os

# Get credentials from environment variables (optional, boto3 does this automatically)
aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')

# You can either pass them explicitly (not recommended unless debugging)
# or let boto3 pick them up automatically from the environment

# Cleanest way (automatically picks up from environment variables)
#s3 = boto3.client('s3')

# Upload the file
#s3.upload_file('chart.png', 'tester-1-bucket123', 'chart')

print(aws_access_key_id, aws_secret_access_key)
