
def twoSum(nums, target: int):
    for i in range(len(nums)):
        r = target - nums[i]
        try:
            j = nums.index(r)
            if j != i:
                return [i,j]
        except:
            pass

nums = list(map(int,input('nums = ').split(' ')))
target = int(input('target = '))
print(twoSum(nums,target))
