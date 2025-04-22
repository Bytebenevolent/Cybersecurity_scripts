import socket


def main():
    target_host = input("Enter host: ")
    target_port = int(input("Enter port: "))

    try:
        # Creating TCP socket.
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(5)

        print(f"Connecting to {target_host}:{target_port}...")
        client.connect((target_host, target_port))

       # Form a correct HTTP GET request.
        request = f"GET / HTTP/1.1\r\nHost: {target_host}\r\nConnection: close\r\n\r\n"
        client.send(request.encode())

        # Receiving a response(in a loop while the data is available).
        response = b''
        while True:
            try:
                chunk = client.recv(4096)
                if not chunk:
                    break
                response += chunk
            except socket.timeout:
                print("Timeout while receiving data.")
                break

        print("\n--- Response ---\n")
        print(response.decode('utf-8', errors = 'replace'))

    except socket.timeout:
        print("Connection timed out.")
    except ConnectionRefusedError:
        print("Connection refused. Make sure the server is running.")
    except socket.gaierror:
        print("Invalid host.")
    except Exception as exception:
        print(f"Error: {exception}")
    finally:
        client.close()
        print("\nConnection closed.")


if __name__ == "__main__":
    main()
