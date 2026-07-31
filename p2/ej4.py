service_name = "example app"
validation = "Invalid service name:"
is_valid = True

if len(service_name) < 3:
    validation += "\n - Name must contain at least 3 characters."
    is_valid = False
elif len(service_name) > 30:
    validation += "\n - Name must not exceed 30 characters."
    is_valid = False

if " " in service_name:
    validation += "\n - Name cannot contain spaces."
    is_valid = False

if is_valid:
    validation = "Service name is valid."

print(validation)
