import socket
import tqdm
import ssl

# HOST AND PORT
HOST= "127.0.0.1"
PORT= 9090

def read_data(client: socket.socket)-> bytes:
    msg= b''
    done= False

    while not done:
        data= client.recv(1)
        if not data or data== b'\n':
            done= True
        else:
            msg+= data
    
    return msg

def receive_file(client: socket.socket)-> None:
    file_name= read_data(client).decode('UTF-8')

    file_length= read_data(client).decode('UTF-8')

    pbar= tqdm.tqdm(total= int(file_length))

    data= b''

    for i in range(int(file_length)):
        msg= client.recv(1)
        if msg:
            data+= msg
            pbar.update(1)
        else:
            raise Exception('Unable To Read File')
    
    with open(f'../images/{file_name}', 'wb') as f:
        f.write(data)

def start_server()-> None:
    try:
        context= ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        
        context.load_cert_chain(certfile= "certificate.pem", keyfile="key.pem")

        server= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        server.bind((HOST, PORT))

        server.listen()

        ssl_server= context.wrap_socket(sock= server, server_side= True)

        print(f'*** SERVER STARTED ***')

        client, _= ssl_server.accept()

        receive_file(client)

        client.send('File Received'.encode('UTF-8'))

    except Exception as e: 
        print(f'Exception: {e}')
    finally:
        ssl_server.close()
        server.close()     

def main():
    start_server()

if __name__=="__main__":
    main()