import socket  # noqa: F401


def main():
    
    print("Logs from your program will appear here!")

    
    server_socket = socket.create_server(("localhost", 4221))

    print("Tcp server listening on port 4221")

    communication_socket,address = server_socket.accept()

    print(f"connectd by {address}")

    while True:
        data = communication_socket.recv(1024)
        if not data:
            break
        print(f"received data:{data.decode()}")

        communication_socket.sendall(data)

    communication_socket.close()
    print("Connection closed")

if __name__ == "__main__":
    main()
