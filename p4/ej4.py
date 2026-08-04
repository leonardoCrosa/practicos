def contains_only_allowed_characters(value):
    for char in value:
        if not char.islower():
            if not char.isnumeric():
                if not char == "-":
                    return "The service name contains characters that are not allowed"
    return "Service name allowed"

test = input("Enter Service Name (Only \"a-z\" \"0-9\" and \"-\" allowed): ")

print(contains_only_allowed_characters(test))
