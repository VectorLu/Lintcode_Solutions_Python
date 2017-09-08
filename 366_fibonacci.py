class Solution:
    """
    @param: n: an integer
    @return: an ineger f(n)
    """
    def fibonacci(self, n):
        # write your code here
        a, b = 0, 1
        i = 1
        while(i < n):
            a, b = b, a+b
            i = i+1
        return a
