# Press the green button in the gutter to run the script.
import socket


def broadcast(round, v):
    pass


class Node(object):
    def __init__(self, i, address):
        self.i = i
        self.address = address
        print(i)
        address = 12345 + i
        print(address)


def initialize_nodes(total_nodes, failed_nodes):
    i = 1
    nodes = []
    starting_port = 12345
    while i < total_nodes:
        nodes.append(Node(i, starting_port + i))
        i = i + 1
    return nodes


def connect_nodes(nodes):
    s = socket.socket()
    n = 5
    connections = []
    for obj in nodes:
        port = obj.address
        s.bind(('', port))
        s.listen(n)
        n = n + 1


if __name__ == '__main__':
    # parameters:
    total_nodes = 7  # number of processors
    failed_nodes = 1  # number of failures
    nodes = initialize_nodes(total_nodes, failed_nodes)
    connect_nodes(nodes)

    round = 1
    decided = False
    v = True  # binary input value (attack or defence in byzantine generals problem)
    # while True:
    #     broadcast(round, v)  # notification
