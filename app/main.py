import socket  # noqa: F401



def main():
    
    print("starting connection...")

    
    server_socket = socket.create_server(("localhost", 4221))

    print("you are almost there..")
    communication_socket,address = server_socket.accept()
    print(f"connectd by {address}")
    

    while True:
          try:
            request = communication_socket.recv(1024).decode()
            print(f"Request received: {request}")

            response_body = "<html><body><h1>Basic HTTP Server</h1></body></html>"
            response = (
                         "HTTP/1.1 200 OK\r\n"
                        "Content-Type: text/html\r\n"
                         f"Content-Length: {len(response_body)}\r\n"
                         "\r\n"
                        f"{response_body}"
                        )


            communication_socket.sendall(response.encode())
          except Exception as e:
              print(f"Error :{e}")
              break
    communication_socket.close()
              
    
        

if __name__ == "__main__":
    main()
