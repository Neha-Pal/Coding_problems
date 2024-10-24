# example - 
# a = (a[0],a[1],a[2]) = (5,6,7)
# b = (b[0],b[1],b[2]) = (3,6,10)

# if a[0]>b[0] -> Alice receives 1 point
# if a[0]<b[0] -> Bob receives 1 point
# if a[0]=b[0] -> No one receives any point

def output(a, b):
    alice = 0
    bob = 0
    for i in range(len(a)):
        if a[i]>b[i]:
            alice += 1
        elif a[i]<b[i]:
            bob += 1

    return [alice, bob]

a = [17, 28, 30]
b = [99, 16, 8]
print(output(a,b))
