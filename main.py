import vpc
import subnet
import route
import ec2

print("1. Check VPC")
print("2. Check Subnet")
print("3. Create InternetGateway")
print("4. Create Public Route Table")
print("5. Create Private Route Table")
print("6. Associate Public Subnets")
print("7. Associate Private Subnets")
print("8. Launch EC2")

choice = input("Enter your choice: ")

if choice == "1":
    vpc.check_vpc()

elif choice == "2":
    subnet.check_subnet()
elif choice == "3":
    route.create_gateway()
elif choice == "4":
    route.create_public_route_table()
elif choice == "5":
    route.create_private_route_table()
elif choice == "6":
    route.associate_public_subnets()
elif choice == "7":
    route.associate_private_subnets()
elif choice == "8":
    ec2.launch_ec2()

else:
    print("Invalid choice")
