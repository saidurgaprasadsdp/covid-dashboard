n = int(input())
factors = 0 
for w in range(2,n):
    if (n%w==0):
        factors += 1 
if factors==0:
    print("PRIME NUMBER")
else:
    print("not a primenumber")