class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, element):
        self.stack.append(element)
        self.size += 1

    def pop(self):
        if self.isempty():
            raise IndexError("Stack is empty")
        self.size -= 1
        return self.stack.pop()

    def top(self):
        if self.isempty():
            raise IndexError("Stack is empty")
        return self.stack[-1]

    def isempty(self):
        return self.size == 0


class Queue:
    def __init__(self):
        self.queue = []
        self.size = 0
        self.first = 0

    def enqueue(self, element):
        self.queue.append(element)
        self.size += 1

    def dequeue(self):
        if self.isempty():
            raise IndexError("Queue is empty")
        return self.queue.pop(0)

    def front(self):
        if self.isempty():
            raise IndexError("Queue is empty")
        return self.queue[self.first]

    def isempty(self):
        return self.size == 0


def pathFinder(grid, startX, startY, endX, endY):
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.direction = 0

    notbeen = [[True] * len(grid) for _ in range(len(grid))]

    myStack = Stack()

    secondStack = Stack()
    lastStack = Stack()

    CurrentPosition = Point(startX, startY)
    aspoint = [CurrentPosition.x, CurrentPosition.y]
    myStack.push(CurrentPosition)
    secondStack.push(aspoint)

    while not myStack.isempty():
        CurrentPosition = myStack.pop()
        d = CurrentPosition.direction
        xCoord = CurrentPosition.x
        yCoord = CurrentPosition.y
        CurrentPosition.direction += 1
        myStack.push(CurrentPosition)

        notbeen[xCoord][yCoord] = False

        if xCoord == endX and yCoord == endY:
            while not secondStack.isempty():
                lastStack.push(secondStack.pop())
            while not lastStack.isempty():
                [i, j] = lastStack.pop()
                i = str(i)
                j = str(j)
                print("[" + i + "," + j + "]")
            return None

        if d == 0:  # for down (a+1, b)
            if xCoord + 1 < len(grid) and grid[xCoord + 1][yCoord] and notbeen[xCoord + 1][yCoord]:
                Position = Point(xCoord + 1, yCoord)
                notbeen[xCoord + 1][yCoord] = False
                myStack.push(Position)
                secondStack.push([Position.x, Position.y])

        elif d == 1:  # for right (a, b+1)
            if yCoord + 1 < len(grid) and grid[xCoord][yCoord + 1] and notbeen[xCoord][yCoord + 1]:
                Position = Point(xCoord, yCoord + 1)
                notbeen[xCoord][yCoord + 1] = False
                myStack.push(Position)
                secondStack.push([Position.x, Position.y])

        elif d == 2:  # for up (a-1, b)
            if xCoord - 1 >= 0 and grid[xCoord - 1][yCoord] and notbeen[xCoord - 1][yCoord]:
                Position = Point(xCoord - 1, yCoord)
                notbeen[xCoord - 1][yCoord] = False
                myStack.push(Position)
                secondStack.push([Position.x, Position.y])

        elif d == 3:  # for right (a, b-1)
            if yCoord - 1 >= 0 and grid[xCoord][yCoord - 1] and notbeen[xCoord][yCoord - 1]:
                Position = Point(xCoord, yCoord - 1)
                notbeen[xCoord][yCoord - 1] = False
                myStack.push(Position)
                secondStack.push([Position.x, Position.y])

        else:
            notbeen[CurrentPosition.x][CurrentPosition.y] = True
            myStack.pop()
            secondStack.pop()

    print("Path not found")