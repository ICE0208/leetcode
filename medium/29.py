class Solution:
    def divide(self, dividend, divisor):
        rst = int(dividend / divisor)
        if rst > 2147483647:
            return 2147483647
        elif rst < -2147483648:
            return -2147483648
        else:
            return rst