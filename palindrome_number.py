# Using modulo to solve
def palindrome_number(x):
    # store the digits in a list
    if x <= -10:
        return False # return false for negative numbers s
    lst = []
    while x > 0:
        lst.append(x % 10)
        x = x // 10
    # Determine how many iterations to loop through list from both sides
    iter_num = len(lst) // 2
    palindrome_counter = 0
    for i in range(iter_num):
        if lst[i] == lst[-i -1]:
            pass
        elif lst[i] != lst[-i -1]:
            palindrome_counter +=1
            return False
    return True
    


print(palindrome_number(-123454321))
