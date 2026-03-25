def palindrome(s):
    if len(s)<=1:
        return True
    return palindrome(s[1:-1])
word=input("enter the string:")
if palindrome(word):
    print("palindrome")
else:
    print("not palindrome")