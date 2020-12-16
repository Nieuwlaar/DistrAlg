class Message:
    def __init__(self, message, sending_process, clock):
        self.message = message
        self.sending_process = sending_process
        self.clock = clock
