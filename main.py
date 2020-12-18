# Press the green button in the gutter to run the script.



def broadcast(round, v):
    pass


class Node(object):
    def __init__(self, i, address):
        self.i = i
        self.address = address
        print(i)
        address = 12345+i
        print(address)



def initializeNodes(total_nodes, failed_nodes):
    i = 1
    nodes = []
    starting_port = 12345
    while i < total_nodes:
        nodes.append(Node(i, starting_port+i))

        i = i + 1

    # print(nodes[])


if __name__ == '__main__':
    # parameters:
    total_nodes = 7  # number of processors
    failed_nodes = 1  # number of failures
    initializeNodes(total_nodes, failed_nodes)

    round = 1
    decided = False
    v = True  # binary input value (attack or defence in byzantine generals problem)
    # while True:
    #     broadcast(round, v)  # notification
