hcost = float(input("Insert hourly cost of the resource: "))
hours = float(input("Insert monthly hours of usage for the resource: "))
mcost = hcost*hours
print(f"Estimated monthly cost: {mcost}")
