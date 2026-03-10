class solution:
    def reverse(self, num: int) -> int:
        reverseNumber = 0
        sign = -1 if num < 0 else 1
        num = abs(num)
        while num > 0:
            last_digit = num % 10
            reverseNumber = reverseNumber * 10 + last_digit
            num = num // 10
        return sign * reverseNumber

if __name__ == "__main__":
    num = int(input("Enter an integer: "))
    obj = solution()
    print("reversed: ", obj.reverse(num))