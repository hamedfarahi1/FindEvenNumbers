
class Solution(object):
    def permute_unique(self, nums):
        perms = [[]]
        for n in nums:
            new_perm = []
            for perm in perms:
                for i in range(len(perm) + 1):
                    new_perm.append(perm[:i] + [n] + perm[i:])
                    if i < len(perm) and perm[i] == n : break
            perms = new_perm
        return perms



class Class:
    number = 0
    numbers = []
    state = []

def getNumber():
    Class.number=0
    Class.numbers=[]
    Class.state=[]
    N = input('Enter a even number: ')
    Class.number = int(N)
    for i in range(1 , int(Class.number/2)+1):
        if (2*i) % 2 == 0:
            Class.numbers.append(2*i)
def sumValue(nums):
    sum=0
    for i in nums:
        sum=sum+i
    return sum

def printQueue(Q):
    s=[]
    for i in Q:
        s.append(i)

    Class.state.append(s)

def printResult(q):
    st=""
    for i in q:
        st=st+str(i)+" + "
    print(st[:-3]+" = "+str(Class.number))

def calculate(a):

    for num in a:
        qu = []
        while True:
            if len(qu) == 0:
                qu.append(num)
            elif sumValue(qu) < Class.number:
                qu.append(2)
            elif sumValue(qu) == Class.number and len(qu) == 1:
                break
            elif sumValue(qu) == Class.number:
                printQueue(qu)
                qu.append(qu.pop()+qu.pop())

    Class.state.append([Class.number])

def main():
    while True:
        getNumber()
        a = Class.numbers
        calculate(a)
        s = Solution()
        fin=[]
        states=[]
        for n in Class.state:
            fin = fin + s.permute_unique(n)
        fin.sort()
        for k in fin:
            if k not in states:
                printResult(k)
                states.append(k)
            else:
                pass

        if(input('enter e for exit ')=='e'):
            break

if __name__ == '__main__':
    main()


