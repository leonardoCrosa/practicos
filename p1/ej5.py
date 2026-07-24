service_name = "Test App"
owner_team = "Platform Team"
env = "Prod"
replica_number = 4
monitoring_enabled = False

print(f"Service Name: {service_name}. Variable Type: {type(service_name)}")
print(f"Owner Team: {owner_team}. Variable Type: {type(owner_team)}")
print(f"Environment: {env}. Variable Type: {type(env)}")
print(f"Replicas: {replica_number}. Variable Type: {type(replica_number)}")
if monitoring_enabled:
    print(f"Monitoring: Yes. Variable Type: {type(monitoring_enabled)}")
else:
    print(f"Monitoring: No. Variable Type: {type(monitoring_enabled)}")
