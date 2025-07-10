# The Fibonacci is a sequence where each number is the sum of the two numbers before it. 
# This can be represented as Fn = Fn-1 + Fn-2, where F represents a Fibonacci number and n is the term number in the sequence. 
# Example : 0, 1, 1, 2, 3, 5, 8, 13, 21...  (starting from: 0)

#-------------F0-------------
'''
def fibonacci (a):
    return 0 
    '''

#-------------F0 & F1 -------------
'''
def fibonacci (a):
    return a 
    '''

#-------------F2 - F4 -------------
'''
def fibonacci (a):
    if a < 2 :
        return a
    else:
        return a-1
    '''
#-------------F5 -------------
def fibonacci(a):
    if a == 0:
        return 0
    elif a == 1:
        return 1
    else:
        x ,y = 0,1
        for _ in range(2, a + 1):
            x, y = y, x + y
        return y
