import socket

# Form a UDP connection with server
def main():
    # Create a UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Server address and port
    server_address = ('localhost', 8888)

    try:
        # Send a message to the server
        message = input("Enter a message to send to the server: ")
        print(f"Sending message to server: {message}")
        client_socket.sendto(message.encode(), server_address)

        # Receive a response from the server
        response, _ = client_socket.recvfrom(1024)
        print(f"Received response from server: {response.decode()}")
    
    except Exception as e:
        print(f"Client error: {e}")

if __name__ == "__main__":
    main()