class solution:
    def reverse(self, num: int) -> int:
        reverseNumber = 0
        while num > 0:
            last_digit = num % 10
            reverseNumber = reverseNumber * 10 + last_digit
            num = num // 10
        return reverseNumber
if __name__ == "__main__":
    num = int(input("Enter an integer: "))
    obj = solution()
    print("approach 1: ", obj.reverse(num))