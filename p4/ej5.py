def validate_service_name(name):

    errors = []

    starts_lower = True
    correct_length = True
    az_09_hypen_only = True
    not_consecutive_hypen = True
    not_end_hypen = True

    if not name[0].islower():
        if starts_lower:
            errors.append("Name must start with a lowercase letter")
            starts_lower = False


    for i in range(len(name) - 1):
        if name[i] == "-":
            if name[i + 1] == "-":
                if not_consecutive_hypen:
                    errors.append("Name cannot contain consecutive hypens")
                    not_consecutive_hypen = False

        if not name[i].islower() and not name[i].isnumeric():
            if not name[i] == "-":
                if az_09_hypen_only:
                    errors.append("Name must only contain lowercase, alphanumeric, or hypen characters")
                    az_09_hypen_only = False

    if name[len(name) - 1] == "-":
        if not_end_hypen:
            errors.append("Name cannot end with a hypen")
            not_end_hypen = False

    if len(name) < 3 or len(name) > 30:
        if correct_length:
            errors.append("Length must be between 3 and 30 characters")
            correct_length = False

    return errors

test_name = input("Service Name: ")

print(validate_service_name(test_name))
