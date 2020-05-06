
class Solution:
    def firstBadVersion(self, n):
        #create an array 1...n
        # arr = [i for i in range(1, n+1)]
        left = 0
        right = len(arr) - 1
        first_bad = None
        while left <= right:
            mid = round((left + right) / 2) 
            print(mid)
            if not self.isBadVersion(arr[mid]):
            # if arr[mid] == False:
                left = mid + 1
            # elif arr[mid] == True:
            elif self.isBadVersion(arr[mid]):
                first_bad = arr[mid]
                right = mid - 1
        return first_bad

        # left = 0
        # right = len(array) - 1

        # while left <= right:
        #     mid = round((left + right) / 2)
    
        #     if array[mid] == item:
        #         return mid
        #     elif array[mid] > item:
        #         right = mid - 1 #change position of right

        #     elif array[mid] < item:
        #         left = mid + 1 #change position of left
        # return None
s1 = Solution()
s1.firstBadVersion(4)
