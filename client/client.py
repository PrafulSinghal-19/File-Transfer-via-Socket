import socket
import ssl

# HOST AND PORT
HOST= "127.0.0.1"
PORT= 9090

def send_file(client: socket.socket)-> None:
    with open('../images/Python.png', 'rb') as f:
        client.send('ReceivedImage.png\n'.encode('UTF-8'))
        data= f.read()
        file_length= len(data)
        client.send(f'{file_length}\n'.encode('UTF-8'))
        client.sendall(data)

def connect_to_server()-> None:
    try:
        context= ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        
        context.load_verify_locations("certificate.pem")

        client= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        client= context.wrap_socket(sock= client, server_hostname=HOST) 

        client.connect((HOST, PORT))

        send_file(client=client)

        client.recv(1024)

    except Exception as e:
        pass
    finally:
        client.close()

def main()-> None:
    connect_to_server()

if __name__=="__main__":
    main()

