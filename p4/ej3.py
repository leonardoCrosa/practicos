def starts_with_letter(value):
    if len(value) > 0:
        return value[0].islower()
    else:
        return False

test = input("Enter a String: ")
print(starts_with_letter(test))
