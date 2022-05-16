from math import ceil
from collections import defaultdict
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        1.zip the list to a dict with count of each element
        2.sort the unique keys for later iteration
        3.iter the keys to find the target (x, y, z), min = X, max =z
            (1). x > 0, then no candicate for sure, just break the progress
            (2). x == 0, find from dict to see whether there are enough zeros to generate [0, 0, 0]
            (3). x < 0, then z should meet lower_bound = ceil[|x| / 2] <= z <= 2|x| = upper_bound, y = 0 - (x + z), find from the dict whether there are enought x, y, z
        """
        results = []
        stats = defaultdict(int)
        while nums:
			# use pop to save memory, we don't need nums anymore
            v = nums.pop()
            stats[v] += 1

        keys = sorted(stats.keys())
        for x in keys:
		    # since we begin with lowest of the list, checking witth x < 0 save more cpu and faster
            if x < 0:
                search_upper_bound = 2 * abs(x)
                search_lower_bound = ceil(abs(x) / 2)
                for i in range(1, len(keys) + 1):
                    z = keys[-i]
                    if z > search_upper_bound:
                        continue
                    elif z < search_lower_bound:
                        break
                    else:
                        y = 0 - (x + z)
                        if y in stats:
                            zs = stats[z]
                            ys = stats[y]
                            if (y == z and zs >= 2) or (y == x and ys >= 2) or (x != y and y != z):
                                results.append([x, y, z])
            elif x == 0:
                if stats[0] >= 3:
                    results.append([0, 0, 0])
            else:
                break
        return results
