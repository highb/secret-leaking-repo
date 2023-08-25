#!/usr/bin/env python3

# This very important program POSTs a JSON payload with secret data to a
# server. It is very important that the secret data is not leaked, so the
# program encrypts the data with a password before sending it. The password
# is stored in the environment variable PASSWORD, which is read via the secret.env
# file. DO NOT CHECK THIS FILE INTO VERSION CONTROL.

import os
import sys
import json
import requests
import hashlib
import base64

# Read the password from the environment variable
with open("secret.env") as f:
    password = f.read().strip()

# Read the secret data from the file
with open("secret.json") as f:
    secret_data = f.read().strip()

# Encrypt the secret data with the password
password = password.encode("utf-8")
secret_data = secret_data.encode("utf-8")
encrypted_secret_data = hashlib.sha256(password + secret_data).digest()
encrypted_secret_data = base64.b64encode(encrypted_secret_data).decode("utf-8")

# POST the encrypted data to the server

# This is the URL of the server
url = "https://example.com/api"

# This is the JSON payload that will be sent to the server
payload = {
    "data": encrypted_secret_data
}

# Send the request
r = requests.post(url, json=payload)

# Check the response status code
if r.status_code != 200:
    print("Error: the server returned status code", r.status_code)
    sys.exit(1)

# Print the response
print(r.text)
