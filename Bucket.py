import boto3
import botocore, botostubs
import configparser

import boto3

s3 = boto3.resource('s3')
location = {'LocationConstraint': 'ap-southeast-1'}
s3.create_bucket(Bucket='kanak-bucket1', CreateBucketConfiguration=location)
s3.Object('kanak-bucket1', 'abcd.txt').upload_file(Filename='/home/kanak_vyas/Documents/kanak-hu2020/Boto3/abcd.txt')
