def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        nums2  = nums[:] 
        for i in nums2:
            print(nums)
            if i == val:
                nums.remove(i)
            else:
                count += 1
        print(count)

    # Hello Eceryone and 
        print("Suresh")

