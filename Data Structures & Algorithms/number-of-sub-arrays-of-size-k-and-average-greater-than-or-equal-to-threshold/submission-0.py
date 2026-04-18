class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        currSum = 0
        count = 0
        L = 0

        for R in range(len(arr)):
            currSum += arr[R]
            if R - L + 1 == k:
                if currSum >= threshold * k:
                    count += 1
                currSum -= arr[L]
                L += 1
            
        return count

