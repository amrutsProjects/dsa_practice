class solution:
    def palindrome(self, num: int) -> bool:
        given_num = num
        reversed_num = 0
        while num > 0:
            last_digit = num % 10
            reversed_num = reversed_num * 10 + last_digit
            num = num // 10
        
        if given_num == reversed_num:
            return True
        return False

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    obj = solution()
    check_palindrome = obj.palindrome(num)
    if(check_palindrome):
        print(f"{num} is a palidrome.")
    else:
        print(f"{num} is not a palindrome.")