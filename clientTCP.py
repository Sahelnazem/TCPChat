import socket

def start_client():
    # Define server's IP and port
    host = '127.0.0.1'
    port = 5001
    
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect to the server
    client_socket.connect((host, port))
    print(f"Connected to server at {host}:{port}")
    
    try:
        while True:
            # Send a message to the server
            message = input("Client: ")
            client_socket.send(message.encode())
            
            # Receive a reply from the server
            reply = client_socket.recv(1024).decode()
            if not reply:
                break
            print("Server:", reply)
    except KeyboardInterrupt:
        print("Client interrupted.")
    finally:
        # Close the connection
        client_socket.close()
        print("Client closed.")

if __name__ == '__main__':
    start_client()

