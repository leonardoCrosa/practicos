team = "platform"
is_admin = True
mfa_enabled = False

if team == "platform" or is_admin == True and mfa_enabled == True:
    print("Production access granted")
else:
    print("Production access denied")
