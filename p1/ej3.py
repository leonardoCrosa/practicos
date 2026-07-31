hourly_cost = float(input("Insert hourly cost of the resource: "))
monthly_hours = float(input("Insert monthly hours of usage for the resource: "))
monthly_cost = hourly_cost*monthly_hours
print(f"Estimated monthly cost: {monthly_cost}")
