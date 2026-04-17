class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mapp=set()

        for n in nums:
            if n in mapp:
                return True
            mapp.add(n)
        return False