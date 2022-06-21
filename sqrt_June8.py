class Solution(object):
    def mySqrt(self, x):
        l, r =0, x
        while(l<=r) :
            mid = l +(r-l)//2
            if mid*mid==x : 
                return mid
            if mid*mid < x :
                l=mid+1
            else  :
                r=mid -1
        return r
soln = Solution()
print(soln.mySqrt(56))