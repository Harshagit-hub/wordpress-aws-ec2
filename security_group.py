import boto3

ec2 = boto3.client("ec2", region_name="REGION")

vpc_id = "YOUR_VPC_ID"
security_group_id = "YOUR_SECURITY_GROUP_ID"

# def create_security_group():

#     data = ec2.create_security_group(
#         GroupName="WordPress-SG",
#         Description="Security group for WordPress EC2",
#         VpcId=vpc_id
#     )

#     security_group_id = data["GroupId"]

#     print("Security Group Created:", security_group_id)


# create_security_group()
def add_security_group_rules():

    ec2.authorize_security_group_ingress(
        GroupId=security_group_id,
        IpPermissions=[
            {
                "IpProtocol": "tcp",
                "FromPort": 22,
                "ToPort": 22,
                "IpRanges": [
                    {"CidrIp": "0.0.0.0/0"}
                ]
            },
            {
                "IpProtocol": "tcp",
                "FromPort": 80,
                "ToPort": 80,
                "IpRanges": [
                    {"CidrIp": "0.0.0.0/0"}
                ]
            }
        ]
    )

    print("SSH port 22 allowed")
    print("HTTP port 80 allowed")


add_security_group_rules()
