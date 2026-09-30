import boto3

ec2 = boto3.client("ec2", region_name="REGION")

ami_id = "YOUR_AMI_ID"
subnet_id = "YOUR_SUBNET_ID"
security_group_id = "YOUR SECURITY_GROUP_ID"
key_name = "wordpress-key"


def launch_ec2():

    data = ec2.run_instances(
        ImageId=ami_id,
        InstanceType="t3.micro",
        MinCount=1,
        MaxCount=1,
        SubnetId=subnet_id,
        SecurityGroupIds=[security_group_id],
        KeyName=key_name,
        TagSpecifications=[
            {
                "ResourceType": "instance",
                "Tags": [
                    {
                        "Key": "Name",
                        "Value": "WordPress-Server"
                    }
                ]
            }
        ]
    )

    instance_id = data["Instances"][0]["InstanceId"]

    print("EC2 Created:", instance_id)
    print("Name: WordPress-Server")


