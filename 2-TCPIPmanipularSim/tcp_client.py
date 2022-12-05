import socket
import struct
import time
# from utils import int2bin


class TcpClient(object):

    def __init__(self, ip, port):
        self.ip_ = ip
        self.port_ = port
        self.sock_ = None

    def send(self, data_bin):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.ip_, self.port_))

        # data_len = len(data_bin)
        # data_len_bin = int2bin(data_len)
        # data_bin = data_len_bin + data_bin

        sock.sendall(data_bin)

        sock.close()

        return data_bin

    def recv_response_(self, sock):
        pack_size = sock.recv(4)
        pack_size = struct.unpack(">I", pack_size)[0]
        # fetch data package
        data_bin = self.recv_all_(sock, pack_size)

        return data_bin

    def recv_all_(self, sock, msg_length):
        data = b""
        size_left = msg_length

        while len(data) < msg_length:
            recv_data = sock.recv(size_left)
            size_left -= len(recv_data)
            data += recv_data

        return data


if __name__ == "__main__":
    client = TcpClient(ip="192.168.100.128", port=30003)
    # num = 0
    comm = b"def P2():\n    while (True):\nspeedj([0.1,0.1,0.1,0.1,0.1,0.1],0.1,2)\n    end\nend\n"
    while True:
        client.send(comm)
        time.sleep(0.5)
        # num += 1
