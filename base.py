import base64


data = input("Enter encoded text: ")
decoded_text = base64.b64decode(data).decode('utf-8')
print(decoded_text)