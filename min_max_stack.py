    # Feel free to add new properties and methods to the class.
class MinMaxStack:

    def __init__(self): 
        self.stack = []
        self.minMax = []

    def peek(self): 
        return self.stack[-1] if len(self.stack) else None 

    def pop(self):
        nbr = self.stack.pop()
        self.minMax.pop()
        return nbr 

    def push(self, number):
        self.stack.append(number)
        
        if not len(self.minMax): 
            self.minMax.append({'maxValue': number, 'minValue': number})
        elif number < self.minMax[-1]['minValue']: 
            self.minMax.append({'maxValue': self.minMax[-1]['maxValue'], 'minValue': number})
        elif number > self.minMax[-1]['maxValue']: 
            self.minMax.append({'maxValue': number, 'minValue': self.minMax[-1]['minValue']})

    def getMin(self):
        if not len(self.stack): return None 
        return self.minMax[-1]['minValue']

    def getMax(self):
        if not len(self.stack): return None 
        return self.minMax[-1]['maxValue']

stack = MinMaxStack()

stack.push(2)
print(stack.getMin())
stack.push(-1)
print(stack.getMin())
print(stack.getMax())
