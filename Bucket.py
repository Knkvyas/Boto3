import boto3
import botocore, botostubs
import configparser

s3 = boto3.resource('s3')
location = {'LocationConstraint': 'ap-southeast-1'}
s3.create_bucket(Bucket='Name-Bucket', CreateBucketConfiguration=location)
s3.Object('Name-Bucket', 'abcd.txt').upload_file(Filename='path/abcd.txt')


#path is the location of your file.
#abcd.txt is file you want to uplaod
