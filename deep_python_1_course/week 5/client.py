import operator
import re
import socket
import time


class ClientError(Exception):
    pass


class Client:
    def __init__(self, ip, port, timeout=None):
        self.connection = socket.create_connection((ip, port), timeout)

    def put(self, key, value, timestamp=None):
        timestamp = timestamp or str(int(time.time()))
        request = f'put {key} {value} {timestamp}\n'
        self.send_request(request)

    def get(self, key):
        request = f'get {key}\n'
        data = self.send_request(request)
        return self.parse_data(data)

    def send_request(self, request):
        connection = self.connection
        connection.sendall(request.encode())
        respond = connection.recv(4096).decode()
        
        if not (respond[0:2] == ('ok')):
            raise ClientError
        if not (respond[-2:] == ('\n\n')):
            raise ClientError
            
        if respond == 'error\nwrong command\n\n':
            raise ClientError
        return respond[3:-1]

    @staticmethod
    def parse_data(data):
        if not data:
            return dict()
        pattern = r'(\S+)\s(\S+)\s(\S+)\n'
        result = re.findall(pattern, data)
        if (len(result) == 0):
            raise ClientError
        result_formatted = ((key, float(value), int(timestamp)) for key, value, timestamp in result)
        result_sorted = sorted(result_formatted, key=operator.itemgetter(2))
        
#         print('result_sorted: ',result_sorted)
#         if (result_sorted == ''):
#             raise ClientError
        result_dict = dict()
        for key, value, timestamp in result_sorted:
            result_dict.setdefault(key, []).append((timestamp, value))
        return result_dict

    def close(self):
        self.connection.close()
