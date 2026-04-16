class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # create a set 
        # if nums - 1 not in set we know thats where we start the sequence
        #     create sequence
        # else we 
        seen = set(nums)
        longest = 0

        for num in seen:
            if (num - 1) not in seen:
                length = 1
                while(num + length) in seen:
                    length += 1
                longest = max(length, longest)
        return longest