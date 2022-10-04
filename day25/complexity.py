# Enter your code here. Read input from STDIN. Print output to STDOUT
num_of_inputs = input()
for num_of_input in range(int(num_of_inputs)):
    num = int(input())
    
    is_prime = True
    if num == 1:
        is_prime = False
    i = 2
    while i * i <= num:
        if num % i == 0 and i != num:
            is_prime = False
            break
        i += 1
    if is_prime:
        print("Prime")
    else:
        print("Not prime")
