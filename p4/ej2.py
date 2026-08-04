def has_valid_length(value, minimum, maximum):
    if minimum <= len(value) <= maximum:
        return True
    else:
        return False

print(has_valid_length("te", 3, 30))
