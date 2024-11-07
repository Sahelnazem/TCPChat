import socket

def start_server():
    # Define server's IP and port
    host = '127.0.0.1'
    port = 5001
    
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the socket to the address and port
    server_socket.bind((host, port))
    # Start listening for connections
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")
    
    # Accept a client connection
    conn, addr = server_socket.accept()
    print(f"Connection established with: {addr}")
    
    try:
        while True:
            # Receive message from the client
            message = conn.recv(1024).decode()
            if not message:
                break
            print("Client:", message)
            
            # Send a reply to the client
            reply = input("Server: ")
            conn.send(reply.encode())
    except KeyboardInterrupt:
        print("Server interrupted.")
    finally:
        # Close the connection
        conn.close()
        server_socket.close()
        print("Server closed.")

if __name__ == '__main__':
    start_server()