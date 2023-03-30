import os

response = os.environ.get("RESPONSE")

if response.strip() == "HTTP/1.1 200 OK":
    print("Test ok")
else:
    print("Test failed")