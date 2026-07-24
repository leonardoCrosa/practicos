primary_region = "us-east-1"
secondary_region = "us-west-2"

primary_region = primary_region + secondary_region
secondary_region = primary_region[0:len(primary_region)-len(secondary_region)]
primary_region = primary_region[len(secondary_region):len(primary_region)]

print(f"Primary: {primary_region}")
print(f"Secondary: {secondary_region}")


