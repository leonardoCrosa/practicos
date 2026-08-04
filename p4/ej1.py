def describe_service(name, owner, environment):
    return f"Service {name} is owned by {owner} and runs in {environment}"

print(describe_service("payments-api", "payments-team", "dev"))
