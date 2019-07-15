#coding challenge #37 
#he power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.
#For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}

l = [0,1,2,3,4,5,6,7]
def subset(ar):
    if len(ar) <= 1:
        yield ar
        yield []
    else:
        for item in subset(ar[1:]):
            yield [ar[0]]+item
            yield item
    
subset(l)
r = [x for x in subset(l)]
r.sort()
print (r)

