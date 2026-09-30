import boto3

ec2 = boto3.client("ec2", region_name="REGION")

def create_vpc():
    vpc = ec2.create_vpc(CidrBlock="0.0.0.0/0")
    vpcid = vpc["Vpc"]["VpcId"]
    print("vpc_created:", vpcid)
# create_vpc()
vpc_id = "YOUR_VPC_ID"
def check_vpc():
    data = ec2.describe_vpcs()

    for vpc in data["Vpcs"]:
        print("VPC ID:", vpc["VpcId"]) 
        print("CIDR:", vpc["CidrBlock"])
        print("State:", vpc["State"])
ec2.create_tags(
    Resources=[vpc_id],
    Tags=[
        {
            "Key": "Name",
            "Value": "My-VPC"
        }
    ]
)

print("VPC name added successfully")
