import boto3
import botocore, botostubs
import configparser

ec2 = boto3.resource('ec2', region_name="ap-southeast-1")

instances = ec2.create_instances(
    ImageId='ami-09a4a9ce71ff3f20b',
    MinCount=1,
    MaxCount=3,
    InstanceType='t2.micro',
    KeyName='kanak'

)

# print region in which instance is created
my_session = boto3.session.Session()
my_region = my_session.region_name
print(my_region)
list = []
for ins in instances:
    ins.start()
    ins.wait_until_running()
    list.append(ins)
    print(ins.public_ip_address, ins.instance_type)
