# Enter your code here. Read input from STDIN. Print output to STDOUT
returnDate = [int(x) for x in input().split()]

dueDate = [int(x) for x in input().split()]

def fine(returnDate, dueDate):
    if returnDate[2] > dueDate[2]:
        print(10000)
        return
    elif returnDate[2] ==  dueDate[2]:
        if returnDate[1] > dueDate[1]:
            print(500 * (returnDate[1] - dueDate[1]))
            return
        elif returnDate[1] == dueDate[1]:
            if returnDate[0] > dueDate[0]:
                print(15 * (returnDate[0] - dueDate[0]))
                return
    print(0)


fine(returnDate, dueDate)
