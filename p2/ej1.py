env = input("Define Environment: ")

if env == "dev" or env == "prod" or env == "staging":
    print("Valid Environment")
else:
    print("Invalid Environment")
