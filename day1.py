#Reverse Integer
#with typcasting
def rev(num):
    r=str(num)
    return r==r[:: -1]
rev(902)

#without typcasting
def reverse(num):
    result=0
    while num !=0:
        rem = num%10
        result=result*10 +rem
        num= num // 10
        return result
    
#palindrome
def palindrone(num):
    N=num
    rev=0
    while N !=0:
        rem=N %10
        rev=rev*10+rem
        N=N//10
    return num == rev
palindrone