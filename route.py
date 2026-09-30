import boto3

ec2 = boto3.client("ec2", region_name="REGION")

vpc_id = "YOUR_VPC_ID"
igw_id = "YOUR_IGW_ID"
public_route_table_id = "YOUR_PUBLIC_ROUTE_TABLE_ID"
private_route_table_id = "YOUR_PRIVATE_ROUTE_TABLE_ID"
Security_group_id  = "YOUR_SECURITY_GROUP_ID"
def create_gateway():

    data = ec2.create_internet_gateway()

    igw_id = data["InternetGateway"]["InternetGatewayId"]

    ec2.attach_internet_gateway(
        InternetGatewayId=igw_id,
        VpcId=vpc_id
    )

    print("Internet Gateway Created:", igw_id)
def create_public_route_table():

    data = ec2.create_route_table(
        VpcId=vpc_id
    )

    route_table_id = data["RouteTable"]["RouteTableId"]

    ec2.create_route(
        RouteTableId=route_table_id,
        DestinationCidrBlock="0.0.0.0/0",
        GatewayId=igw_id
    )

    print("Public Route Table Created:", route_table_id)


def create_private_route_table():

    data = ec2.create_route_table(
        VpcId=vpc_id
    )

    route_table_id = data["RouteTable"]["RouteTableId"]

    print("Private Route Table Created:", route_table_id)
def associate_public_subnets():

    data = ec2.describe_subnets(
        Filters=[
            {
                "Name": "vpc-id",
                "Values": [vpc_id]
            }
        ]
    )

    for subnet in data["Subnets"]:

        cidr = subnet["CidrBlock"]

        if cidr in ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]:

            ec2.associate_route_table(
                RouteTableId=public_route_table_id,
                SubnetId=subnet["SubnetId"]
            )

            print("Public subnet associated:", subnet["SubnetId"])


def associate_private_subnets():

    data = ec2.describe_subnets(
        Filters=[
            {
                "Name": "vpc-id",
                "Values": [vpc_id]
            }
        ]
    )

    for subnet in data["Subnets"]:

        cidr = subnet["CidrBlock"]

        if cidr in ["10.0.4.0/24", "10.0.5.0/24", "10.0.6.0/24"]:

            ec2.associate_route_table(
                RouteTableId= private_route_table_id,
                SubnetId=subnet["SubnetId"]
            )

            print("Private subnet associated:", subnet["SubnetId"])
