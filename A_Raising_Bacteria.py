def solver(number):
    result=0
    while number>0:
        if number%2==1:
            result+=1
        number//=2
    return result
def solver(number):
    result=0
    while number>0:
        if number&1==1:
            result+=1
        number>>=1
    return result
print(solver(int(input())))