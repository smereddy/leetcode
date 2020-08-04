# Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.
#
# Note that elements beyond the length of the original array are not written.
#
# Do the above modifications to the input array in place, do not return anything from your function.
#
#
#
# Example 1:
#
# Input: [1,0,2,3,0,4,5,0]
# Output: null
# Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
# Example 2:
#
# Input: [1,2,3]
# Output: null
# Explanation: After calling your function, the input array is modified to: [1,2,3]
#
#
# Note:
#
# 1 <= arr.length <= 10000
# 0 <= arr[i] <= 9

class Solution:
    def duplicateZeros(self, arr):
        """
        Do not return anything, modify arr in-place instead.
        """

        new_list = []
        i = 0
        len_arr = len(arr)

        for i in range(len_arr):
            new_list.append(arr[i])
            if arr[i] == 0:
                new_list.append(0)

        # arr = new_list

        for i in range(len_arr):
            arr[i] = new_list[i]
