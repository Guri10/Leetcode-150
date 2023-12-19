def merge( nums1, m, nums2, n):
    a, b, i = m-1, n-1, m + n - 1
    while b >= 0:
        if a >= 0 and nums1[a] > nums2[b]:
            nums1[i] = nums1[a]
            a -= 1
        else:
            nums1[i] = nums2[b]
            b -= 1

        i -= 1
    return nums1


nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m,n = 3,3
print(merge(nums1,m,nums2,n))
