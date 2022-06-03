test = [1,1,2,2,2,2,2,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,8,8,8]
print('len(test) =', len(test))
print()



def bin(num, left, right):

    mid = int((left+right-1)>>1)
    print(left, end='\t')
    print(right, end='\t')
    print(mid)
    
    if left == right:
        return left
    elif test[mid] >= num:
        right = mid - 1
        return bin(num, left, right)
    elif test[mid] <= num:
        left = mid + 1
        return bin(num, left, right)
    
        
num = 3
print('bin =', bin(num=num, left=0, right=len(test)-1))
print()

print('test.index(num) =', test.index(num))

'''
len(test) = 27

0	26	12
0	11	5
6	11	8
6	7	6
7	7	6
bin = 7

test.index(num) = 7
'''
