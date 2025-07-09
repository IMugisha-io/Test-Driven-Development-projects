#def multiply (a,b):
#    return a*b

# Stretch Exercise: What might you do if your language didn't natively support multiply?

def multiply(a, b):
    total = 0
    for _ in range(b):
        total += a
    return total

   