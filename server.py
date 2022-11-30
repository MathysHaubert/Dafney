import socket


def server_program():
    # get the hostname
    host = "0.0.0.0" #socket.gethostname()
    port = 55032  # initiate port no above 1024
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    print("En attente d'une connection...")
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if data == "ping":
            msg = "pong"
            conn.send(msg.encode())  # send data to the client
            print("Connexion seems to be ok !")
        print("from connected user: " + str(data))
        if not data: break;

    conn.close()  # close the connection
    server_socket.close()
    

if __name__ == '__main__':
    server_program()
