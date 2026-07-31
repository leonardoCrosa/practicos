http_code = 203
return_message = ""

if 200 <= http_code < 300:
    return_message = "success"
elif 300 <= http_code < 400:
    return_message = "redirect"
elif 400 <= http_code < 500:
    return_message = "client error"
elif 500 <= http_code < 600:
    return_message = "server error"
else:
    return_message = "invalid status code"

print(return_message)

