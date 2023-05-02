import socket

class UDP:
    def __init__(self, ip):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.addr = (ip, 38899)

    def call(self, message):
        self.sock.sendto(bytes(message), self.addr)
        data, _ = self.sock.recvfrom(1024)
        return data