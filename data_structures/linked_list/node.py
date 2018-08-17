class Node(object):
    def __init__(self, value, _next=None):
        self.val = value
        self._next = _next

    def __str__(self):
        return f'{self.val}'

    def __repr__(self):
        return f'<Node | val: {self.val} | Next: {self._next}>'