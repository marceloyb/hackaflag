import socket
from teste import calcCarga

host = "142.93.73.149"
port = 10869



def receive(s):
    data = s.recv(8192)
    data = data.decode()
    return data

def send(s, payload):
    if type(payload) is int:
        s.send(str(payload).encode())
    else:
        s.sendall(payload.encode())

def chall(s):
    vetor = []
    data = receive(s)
    data = data.split("Cargas",1)
    data = data[1].split(" ", 1)
    data = data[1].split("\n", 1)
    data = data[0]
    for i in data:
        if i.isdigit():
            vetor.append(int(i))
    print("Vetor:", vetor)
    carga = calcCarga(vetor)
    return carga
    # print(carga)

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    data = receive(s)
    start = "start"
    send(s, start)

    data = receive(s)
    
    for i in range(25):
        carga = chall(s)
        send(s, carga)
        data = receive(s)
        print(data)



if __name__ == '__main__':
    main()
    

