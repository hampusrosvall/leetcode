class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_values = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not len(self.min_values): 
            self.min_values.append(x)
            return 
        
        min_value = min(x, self.min_values[-1])
        self.min_values.append(min_value)

    def pop(self) -> None:
        self.stack.pop()
        self.min_values.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_values[-1]
