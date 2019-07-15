#coding problem #11
#Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.
#For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

lst = ['safe', 'safety', 'safer']
       autofillable = []
i = 0

def done():
    if input() != '':
       print("done")

def int():
    global i
    input("input the letter s")
    print(lst)
    if input() == 'sa':
        autofillable.append(lst[:3])
        print(autofillable)
        del lst[:]
        lst.insert(0,0)
        if input() == 'saf':
            print(autofillable)
            if input() == 'safe':
                print(autofillable)
                done()
                if input() == 'safer':
                    autofillable.pop([0])
                    autofillable.pop([1])
                    print(autofillable)
                    done()
                if input() == 'safet':
                    autofillable.pop([0])
                    autofillable.pop([i])
                    print(autofillable)
int()
