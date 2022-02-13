       #Brute force approach with two for loops: T.C = O(n^2) & S.C = O(1)

        #Sorting the array first: T.C = O(n log n) & S.C = O(1)
        nums.sort()

        if (len(nums) == 1):
            return False

        for i in range(len(nums)):
            if nums[i] == nums[i-1]:
                return True

        return False

        #Using Hash Map: T.C = O(n) & S.C = O(n)
        numsDictionary = dict()

        for item in nums:
            if item in numsDictionary:
                return True
            else:
                numsDictionary[item] = True

        return False

        #Using sets
        return len(nums) > len(set(nums))
