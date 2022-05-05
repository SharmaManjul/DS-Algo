#TC = O(N * N!) and SC = O(N * N!)

#Recursively
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.permuter([], result, 0, nums)
        return result

    #Recursivce fucntion to perform permutation.
    def permuter(self, cur_permutation, result, index, nums):
        #In every permutation add the next element in all possible spots inside until we run out of nums.
        if len(nums) == index:
            result.append(cur_permutation)
            return
        else:
            for i in range(len(cur_permutation) + 1):
                new_permutation = list(cur_permutation)
                new_permutation.insert(i, nums[index])
                self.permuter(new_permutation, result, index + 1, nums)

#Iteratively
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        permutations = deque()
        permutations.append([])

        #loop through all the nums
        for cur_num in nums:
            p_len = len(permutations)
            #For each num loop through all the created permutations.
            for _ in range(p_len):
                old_permutation = permutations.popleft()
                #For each permutation combine the new num in lenght of permutation ways.
                for i in range(len(old_permutation) + 1):
                    new_permutation = list(old_permutation)
                    new_permutation.insert(i, cur_num)
                    #If the newly created permutation is equal to the lenght of the nums list then we a valid permutation.
                    if len(new_permutation) == len(nums):
                        result.append(new_permutation)
                    #Otherwise continue adding to the permutations list to repeat the process.
                    else:
                        permutations.append(new_permutation)

        return result