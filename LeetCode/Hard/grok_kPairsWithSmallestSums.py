# TC = O(N * M * logK) where N and M are list lengths, if we assume both lists have K elements then O(K^2 * logK)
# SC = O(K)

def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    max_heap = []

    for i in range(min(k, len(nums1))):
        for j in range(min(k, len(nums2))):
            if len(max_heap) < k:
                heapq.heappush(max_heap, [-(nums1[i] + nums2[j]), i, j])
            else:
                if nums1[i] + nums2[j] > -max_heap[0][0]:
                    break
                else:
                    heapq.heappop(max_heap)
                    heapq.heappush(max_heap, [-(nums1[i] + nums2[j]), i, j])

    result = []
    for (_, i, j) in max_heap:
        result.append([nums1[i], nums2[j]])
    return result