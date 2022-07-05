for i in range(1,11,1):
    print(i)
for j in range(5):
    print(j)
List1=['hello','hello','hedeyang','yoo','nor','emea']
for e in List1:
    print(e)
Dic = {'name':'Tuu','Job':'soldier','age':'25'}
for key,value in Dic.items():
    print(key,value)
i = 1
# while is infinities loop
while i < 6:
    print(i)
    i += 1
a = True
if a:
    print("a is true")
    a = 33
    b = 1
if b>a:
    print("b is greater than a")
else:
    print("a is greater than b")
a = False
if a:
    print("a is true")
else:
    print("a is false")
    a=33
    b=33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")