def normalize_name(value):

    first_char_found = False

    i = 0

    while i < len(value) - 1:

        if value[i] == " " and not first_char_found:
            value = value[:i] + value[i + 1:]

        elif value[i] != " " and value[i + 1] == " " and i + 1 == len(value) - 1:
            value = value[:i + 1]

        elif value[i] == " " and value[i + 1] == " " and i + 1 == len(value) - 1 and first_char_found:
            value = value[:i]

        elif value[i] == " " and value[i + 1] == " " and first_char_found:
            value = value[:i] + value[i + 1:]

        elif value[i] == " " and value[i + 1] != " " and first_char_found:
            value = value[:i] + "-" + value[i + 1:]

        else:
            i += 1
            first_char_found = True

    value = value.lower()

    return value

test = input("Enter service name: ")

print(normalize_name(test))

