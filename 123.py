#search if there is a 439
numberset=[2329,3434,76767,5453,565,434,232,545,76,439,656557]
found=False
for i in numberset:
    if i==439:
        found=True
    print(found,i)


try:
    a=2
    b=3
    print(a+b)
except:
    print('error')
    

a,b,c=eval(input('Enter coefficients a,b and c in the equation:'))
delta=eval('b*b-4*a*c')
if delta>0:
    x1=(-b+(delta)**0.5)/2/a
    x2=(-b-(delta)**0.5)/2/a
    print('The two roots of the equation are x1=%.2f and x2=%.2f.'%(x1,x2))

elif delta==0:
    x=-b/2/a
    print('There is only one root x=%.2f.'%x)

else:
    print('The equation has no real roots')



while True:
    number=eval(input('Enter a number:'))
    sumup=0
    while number>0:
        sumup=sumup+number%10
        number=number//10
    print(sumup)
    decision=input('do you want to continue? y or n:')
    if decision=='n':
        break
    else:
        continue

    
