import boto3

s3 = boto3.client('s3')  # boto3 will use environment variables automatically

s3.upload_file('chart.png', 'tester-1-bucket123', 'chart')
print("Upload successful.")
