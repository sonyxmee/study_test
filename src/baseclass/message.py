class Message:
    def __init__(self, message, cost):
        self.message = message
        self.cost = cost

    def __str__(self):
        return f'Message: {self.message}. Cost: {self.cost}'


def get_list_mes():
    return [Message('hi', 1), Message('my name is', 7)]