class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        temp = x
        x = abs(x)
        result = 0
        while(x // 10 != 0):
            result = result*10 + x%10
            x = x//10
        result = result*10 + x
        if (temp < 0): 
            x = -1 * result
        else:
            x = result
        if (-2**31 < x < 2**31):
            return x
        else:
            return 0

        
        
