status_codes = [200, 201, 404, 502, 503]

for code in status_codes:
    if code >= 500:
        print(f"First server error: {code}")
        break
