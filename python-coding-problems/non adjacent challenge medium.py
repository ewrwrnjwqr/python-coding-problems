#coding problem #9
#Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
#For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
even = []
odd = []
i = 0
def sortnonadj():
    global i
    for item in l:
        if i == 0:
            i += 1
            even.append(l[-1])
            l.remove(l[-1])
        if i == 1:
            i += -1
            odd.append(l[-1])
            l.remove(l[-1])
            
def lastterm():
    global i
    l.insert(0,0)
    sortnonadj()
     
def nonadjsiz():
    if sum(even) > sum(odd):
        print(sum(even))
        print(even)
    if sum(odd) > sum(even):
        print(sum(odd))
        print(odd)
    if sum(odd) == sum(even):
        print("they are equal")
    
sortnonadj()
lastterm()
nonadjsiz()
