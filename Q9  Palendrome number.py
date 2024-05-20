#Given an integer x, return true if x is a palindromeand false otherwise
def ispalendrome(x:int):
    if str(x) == str(x)[::-1]:
        return "true"
    else:
        return "false"
print(ispalendrome(-121))