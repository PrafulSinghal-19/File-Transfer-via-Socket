import socket
import tqdm
import time

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
        time.sleep(0.001)
        msg= client.recv(1)
        if msg:
            data+= msg
            pbar.update(1)
        else:
            raise Exception('Unable To Read File')
    
    with open(file_name, 'wb') as f:
        f.write(data)

def start_server()-> None:
    try:
        server= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((HOST, PORT))
        server.listen()

        client, _= server.accept()

        receive_file(client)
    except Exception as e: 
        print(e)
    finally:
        server.close()     

def main():
    start_server()

if __name__=="__main__":
    main()