class Class:
    number = 0
    numbers = []
    state = []

def sumValue(nums):
    sum=0
    for i in nums:
        sum=sum+i
    return sum

def printQueue(Q):
    st=""
    Class.state.append(Q)
    for i in Q:
       st=st + str(i) + " + "
    print(st[:-3])

def calculate():
    queue = []
    num=2
    cond = True
    while cond:
        if sumValue(queue) < Class.number:
            queue.append(num)
        elif sumValue(queue) == Class.number:
            printQueue(queue)
            if queue.pop(0) < num:
               pass
            else:
                num = num+2
                queue.append(num)
        else:
            queue.pop(0)
        if num == Class.number or num > Class.number:
            cond = False
    

def getNumber():
    N = input('Enter a even number: ')
    Class.number = int(N)
    for i in range(2 , int(Class.number/2)+1):
        if (2*i) % 2 == 0:
            Class.numbers.append(2*i)


def main():
    getNumber()
    calculate()

if __name__ == '__main__':
    main()


