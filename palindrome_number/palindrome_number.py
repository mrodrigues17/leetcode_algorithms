# Using modulo to solve
def palindrome_number(x):
    if x < 0:
        return False # return false for negative numbers since never a palindrome
    # store the digits in a list
    lst = []
    while x > 0:
        lst.append(x % 10)
        x = x // 10
    # Determine how many iterations to loop through list from both sides
    iter_num = len(lst) // 2
    for i in range(iter_num):
        if lst[i] != lst[-i -1]:
            return False
    return True
    


print(palindrome_number(1234543211))
