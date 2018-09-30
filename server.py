import socket, sys, os, time


def main():
    os.system("clear")
    print("SERVER SOCKET")
    print("*************")

    # Creat a server socket, addressing family and connection type 
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Getting the Ip, Port
    local_host = socket.gethostname()
    print("Local machine: " + local_host)
    ip = socket.gethostbyname(local_host)
    print("IP: "+ ip)
    port = 4000
    #-------------------------
    # binding sthe socket to ip, port 
    server_socket.bind((ip, port))
    time.sleep(1)
    print("server socket binded to IP: " + ip + " Port: " + str(port))
    # setting the socket to listening mode and accepting 2 connection
    # at time 
    server_socket.listen(2)
    time.sleep(1)
    print("Waiting for client to connect")

    '''getting 2 types of data;
        address = a list, addressing information
        connection = a list, transmission data itself 
    ''' 
    connection, address = server_socket.accept()
    print("Server connected to IP" + address[0] + "Port: " + str(address[1]))

    running = True
    while running:
        print()
        # Creating a command line
        command = input("Commandline: ")
        if command == "quit":
            print("Server going down in 2 seconds!")
            time.sleep(2)
            running = False
            connection.close()
            server_socket.close()
            sys.exit()
        # some data checking 
        if len(str.encode(command)) > 0:
            # decoding the commands to str before sending 
            connection.send(str.encode(command))
            # waiting for feedback from the client 
            client_response = str(connection.recv(1024), "utf-8")
            time.sleep(0.50)
            print("-------------------------------------------------")
            print("Response: " + "\n", client_response)
            print()

if __name__ == "__main__":
    main()

    
