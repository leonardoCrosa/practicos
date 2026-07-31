http_code = 404
return_message = ""

if http_code >= 200 and http_code < 300:
    return_message = "success"
elif http_code >= 300 and http_code < 400:
    return_message = "redirect"
elif http_code >= 400 and http_code < 500:
    return_message = "client error"
elif http_code >= 500 and http_code < 600:
    return_message = "server error"
else: return_message = "invalid status code"

print(return_message)

