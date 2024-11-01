#exercitiul 1
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack += [item]

    def pop(self):
        if len(self.stack) == 0:
            return None
        item = self.stack[-1]
        self.stack = self.stack[:-1] 
        return item

    def peek(self):
        if len(self.stack) == 0:
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

print("Exercitiul 1:")
stack = Stack()
stack.push(5)
stack.push(10)
print(stack.peek())
print(stack.pop())
print(stack.pop())   
print(stack.pop())   
print(stack.peek())	

#exercitiul 2
class Queue:
    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue += [item]

    def pop(self):
        if len(self.queue) == 0:
            return None
        item = self.queue[0] 
        self.queue = self.queue[1:] 
        return item

    def peek(self):
        if len(self.queue) == 0:
            return None
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

print("Exercitiul 2:")
queue = Queue()
queue.push(1)
queue.push(2)
queue.push(3)
print(queue.size()) 
print(queue.peek()) 
print(queue.pop())  
print(queue.pop())   
print(queue.peek())  	

#exercitiul 3
class Matrix:
    def __init__(self, rows, cols, fill=0):
        self.rows = rows
        self.cols = cols
        self.data = [[fill for _ in range(cols)] for _ in range(rows)]

    def get(self, row, col):
        return self.data[row][col]

    def set(self, row, col, value):
        self.data[row][col] = value

    def transpose(self):
        transposed = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                transposed.set(j, i, self.data[i][j])
        return transposed

    def multiply(self, other):
        if self.cols != other.rows:
            print("Dimensiuni diferite! Nu se pot inmulti matricile.")
            return None
        
        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                sum = 0
                for k in range(self.cols):
                    sum += self.data[i][k] * other.get(k, j)
                result.set(i, j, sum)
        
        return result

    def transformation(self, fct):
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] = fct(self.data[i][j])

    def __str__(self):
        return "\n".join([" ".join(map(str, row)) for row in self.data])

print("Exercitiul 3:")
matrix = Matrix(3, 2, 9)
print("Matricea initiala:")
print(matrix)
matrix.set(0, 0, 5)
print(matrix.get(0, 0))
print("Matricea transpusa:")
print(matrix.transpose())
matrix2 = Matrix(2, 3, 1)
print("Matricea 2:")
print(matrix2)
print("Inmultirea matricilor:")
print(matrix.multiply(matrix2))
print("Matricea 1 dupa transformare:")
matrix.transformation(lambda x: x-1)
print(matrix)