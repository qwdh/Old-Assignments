#Functions

def BSearch(a, n):
    l, h = 0, len(a) - 1
    
    while l <= h:
        m = (l + h) // 2
        
        if a[m] == n:
            return m
        
        elif a[m] < n:
            l = m + 1
        
        else:
            h = m - 1
    
    return -1

def BSRec(a, l, h, n):
    
    if l <= h:
        m = (l + h) // 2
        
        if a[m] == n:
            return m
        
        elif a[m] < n:
            return BSRec(a, m + 1, h, n)
        
        else:
            return BSRec(a, l, m - 1, n)
    
    else:
        return -1

#Test
a = [10, 20, 30, 50, 60, 80, 100, 110, 130, 170]

n1 = 110
n2 = 175
n3 = 110
n4 = 175

r1 = BSearch(a, n1)
r2 = BSearch(a, n2)
r3 = BSRec(a, 0, len(a) - 1, n3)
r4 = BSRec(a, 0, len(a) - 1, n4)

if r1 != -1:
    print(f"The given element is present at index {r1}.")

else:
    print("The given element is not in the array.")

if r2 != -1:
    print(f"The given element is present at index {r2}.")

else:
    print("The given element is not in the array.")

if r3 != -1:
    print(f"The given element is present at index {r3}.")

else:
    print("The given element is not in the array.")

if r4 != -1:
    print(f"The given element is present at index {r4}.")

else:
    print("The given element is not in the array.")
