nums = [1, 2, 3]
def add(a, b, c):
    return a + b + c
 
print(add(*nums))        # unpacks list → add(1, 2, 3)
 
info = {"a": 1, "b": 2, "c": 3}
print(add(**info))       # unpacks dict → add(a=1, b=2, c=3)