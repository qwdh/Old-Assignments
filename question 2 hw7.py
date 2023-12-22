def genFib(num):
    if not isinstance(num, int) or num <= 0:
        return "Errors: Please enter a positive integer."
    
    fibSeq = [1, 1]
    for i in range(2, num):
        nextFib = fibSeq[-1] + fibSeq[-2]
        fibSeq.append(nextFib)
    
    return fibSeq[:num]

try:
    num = int(input("How many numbers does that generate?: "))
    result = genFib(num)
    print(result)
except ValueError:
    print("Errors: Please enter a valid integer.")
