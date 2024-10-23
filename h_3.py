# example -->
# arr = [1,1,0,-1,-1] n = 5

# output =>
# 0.400000
# 0.400000
# 0.200000

# as there are 2 negative 2 positive and 1 zero, so 2/5 = 0.400000 and 1/5 = 0.200000

def result(arr):
    positive = 0
    negative = 0
    zeros = 0
    for i in arr:
        if i>0:
            positive += 1
        elif i == 0:
            zeros += 1
        else:
            negative += 1

    p_ratio = positive/len(arr)
    n_ratio = negative/len(arr)
    z_ratio = zeros/len(arr)

    print(f'{p_ratio:.6f}')
    print(f'{n_ratio:.6f}')
    print(f'{z_ratio:.6f}')


arr = [1,1,0,-1,-1]   
print(result(arr))
        
        