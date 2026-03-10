import math
class solution:
    """
        Given an integer N, return the number of digits in N. 
    """
    def countDigitsByConvertingToString(self, num: int) -> int:
        str_num = str(num)
        count = len(str_num)
        return count
    
    def countDigitsByDeviding(self, num: int) -> int:
        if num == 0:
            return 1
        count = 0
        while num > 0:
            num = num // 10
            count = count + 1
        return count
    
    def countDigitsWithLog(self, num: int) -> int:
        if num == 0:
            return 1
        return math.floor(math.log10(num)) + 1

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    obj = solution()
    print("approach 1: ",obj.countDigitsByConvertingToString(num))
    print("approach 2: ", obj.countDigitsByDeviding(num))
    print("approach 3: ", obj.countDigitsWithLog(num))