counter = 1
word = ""

while word != "success" and counter <= 3:
    word = input("Write the word \"success\": ")
    if word == "success":
        print("Operation completed")
    elif word != "success":
        print(f"Attempt {counter} of 3: failed")
        counter += 1

