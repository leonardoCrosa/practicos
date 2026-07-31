env = input("Define Environment: ")
replica_number = int(input("Define Replica Number: "))

if env == "dev" and replica_number >= 1:
    print("Valid Configuration")
elif env == "staging" and replica_number >= 2:
    print("Valid Configuration")
elif env == "prod" and replica_number >= 3:
    print("Valid Configuration")
else:
    print("Invalid Configuration")
