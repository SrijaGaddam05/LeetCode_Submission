class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count =0
        total =0
        prefix_sum ={0:1}
        for num in nums:
            total +=num
            remaining = total-k
            if remaining in prefix_sum:

                count += prefix_sum[remaining]
            prefix_sum[total]=prefix_sum.get(total,0)+1
        return count
        