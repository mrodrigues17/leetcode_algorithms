
Given an integer `x`, return true if `x` is palindrome integer.

An integer is a **palindrome** when it reads the same backward as forward.

- For example, 121 is a palindrome while 123 is not.

Approach:
- If the number is negative, return False since all negative numbers are inherently not palindromes
- Use a while loop and find the last digit of the number. Then use rounding division to move to the next digit (e.g. the ones place to tens, then hundreds, etc.)
- Determine how many digits the number has so we can determine which digits to compare
- Using the digits stored in a list, compare the first and last digits and traverse through the list. If they are all matches, then the number is a palindrome. If there is at least one mismatch, the number is not a palindrome



