#Function
def LSearch(a, n):
    
    for i in range(len(a)):
        
        if a[i] == n:
            
            return i
    
    return -1



#Test
a = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]

n1 = 110
n2 = 175

r1 = LSearch(a, n1)
r2 = LSearch(a, n2)

if r1 != -1:
    print(f"The given element is present at index {r1}.")

else:
    print("The given element is not in the array.")

if r2 != -1:
    print(f"The given element is present at index {r2}.")

else:
    print("The given element is not in the array.")
