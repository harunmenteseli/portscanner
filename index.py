import socket

def port_scanner(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    try:
        s.connect((ip, port))
        print(f' {port} port is open.')
        s.close()
    except:
        print(f'{port} port is closed.')

ip = input("Enter IP Address: ")
start_port = int(input("Enter end port: "))
end_port = int(input("Enter end port: "))

for port in range(start_port, end_port + 1):
    port_scanner(ip, port)
