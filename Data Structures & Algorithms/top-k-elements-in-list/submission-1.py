class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count= {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        arr=[]
        for num,cnt in count.items():
            arr.append([cnt,num])
        arr.sort()
        print (arr)

        ans=[]
        while k>0:
            ans.append(arr.pop()[1])
            k -=1


        

        return ans
                
        