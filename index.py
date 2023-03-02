import socket

def port_scanner(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    try:
        s.connect((ip, port))
        print(f' {port} numaralı port açık.')
        s.close()
    except:
        print(f'{port} numaralı port kapalı.')

ip = input("Enter IP address: ")
start_port = int(input("Başlangıç portunu gir: "))
end_port = int(input("Bitiş portunu gir: "))

for port in range(start_port, end_port + 1):
    port_scanner(ip, port)
