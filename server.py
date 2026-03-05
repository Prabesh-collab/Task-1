import socket

# Define host and port
HOST = '127.0.0.1'  # Localhost
PORT = 8080

# Create a raw TCP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server is listening on {HOST}:{PORT}...")
    
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}\n")
        
        # Receive the raw data (ASCII bytes)
        data = conn.recv(1024)
        
        # Display the raw bytes (Hex-style representation)
        print("--- RAW BYTES RECEIVED ---")
        print(data)
        
        # Display the decoded ASCII text
        print("\n--- DECODED ASCII TEXT ---")
        print(data.decode('ascii'))

        # Send an ASCII response back to the client
        response = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nHello from ASCII world!"
        conn.sendall(response.encode('ascii'))