import socket

# Form a UDP connection with client
def main():
    # Create a UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to an address and port
    server_address = ('localhost', 8888)
    server_socket.bind(server_address)
    print("Server is listening on port 8888...")

    while True:
        try:
            # Wait for a message from the client
            message, client_address = server_socket.recvfrom(1024)
            print(f"Received message from client: {message.decode()}")

            # Funny response to concatenate with the original message
            funnyBit = " - I'm going to break your legs now!"

            # Send full response back to the client
            response = message.decode()
            response += funnyBit
            server_socket.sendto(response.encode(), client_address)
        
        except Exception as e:
            print(f"Server error: {e}")
            break
        
        server_socket.close()
if __name__ == "__main__":
    main()