services = [
    "payments-api",
    "catalog api",
    "auth-service",
    "broken service",
]

for svc in services:
    if " " in svc:
        print(f"Invalid: {svc}")
