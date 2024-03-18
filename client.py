import socket

# HOST AND PORT
HOST= "127.0.0.1"
PORT= 9090

def send_file(client: socket.socket)-> None:
    with open('Python.png', 'rb') as f:
        client.send('ReceivedImage.png\n'.encode('UTF-8'))
        data= f.read()
        file_length= len(data)
        client.send(f'{file_length}\n'.encode('UTF-8'))
        client.sendall(data)

def connect_to_server()-> None:
    try:
        client= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((HOST, PORT))
        send_file(client=client)
    except:
        pass
    finally:
        client.close()

def main()-> None:
    connect_to_server()

if __name__=="__main__":
    main()

