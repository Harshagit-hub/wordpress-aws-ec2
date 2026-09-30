import boto3

ec2 = boto3.client("ec2", region_name="REGION")

vpc_id = "YOUR_VPC_ID"


def create_subnet():

    subnets = [
        ("10.0.1.0/24", "ap-south-1a"),
        ("10.0.2.0/24", "ap-south-1b"),
        ("10.0.3.0/24", "ap-south-1c"),
        ("10.0.4.0/24", "ap-south-1a"),
        ("10.0.5.0/24", "ap-south-1b"),
        ("10.0.6.0/24", "ap-south-1c")
    ]

    for cidr, az in subnets:
        data = ec2.create_subnet(
            VpcId=vpc_id,
            CidrBlock=cidr,
            AvailabilityZone=az
        )

        print("Subnet Created:", data["Subnet"]["SubnetId"])


def check_subnet():

    data = ec2.describe_subnets(
        Filters=[
            {
                "Name": "vpc-id",
                "Values": [vpc_id]
            }
        ]
    )

    for subnet in data["Subnets"]:
        print("Subnet ID:", subnet["SubnetId"])
        print("CIDR:", subnet["CidrBlock"])
        print("State:", subnet["State"])
        print("AZ:", subnet["AvailabilityZone"])
        print()
def enable_public_ip():

    subnet_id = "YOUR_SUBNET_ID"

    ec2.modify_subnet_attribute(
        SubnetId=subnet_id,
        MapPublicIpOnLaunch={
            "Value": True
        }
    )

    print("Auto-assign Public IP enabled")
enable_public_ip()
