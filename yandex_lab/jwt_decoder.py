import jwt

# This script tries different secret keys to generate a new JWT token with a custom payload.
try:
    user = input("Enter the user for payload: ").lower().strip()
    is_developer = input("User's developer(True or False): ").capitalize().strip()

    new_payload = {
        'developer': True,
        'user': user
    }

    secrets = ['secret', 'admin', '123456', 'flask', 'developer', 'session']
    for secret in secrets:
        try:
            new_token = jwt.encode(new_payload, secret, algorithm = 'HS256')
            print(f"New token with secret '{secret}': {new_token}")
        except Exception as exception:
            print(f"Error with secret '{secret}': {exception}")
except ValueError:
    print("Please, check entered value!")
except Exception as exception:
    print(f"Error! {exception}")