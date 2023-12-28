
def hIndex( citations):
    """
    Leetcode: 274. H-Index
    Difficulty: Medium
    URL: https://leetcode.com/problems/h-index/

    Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.
    According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each,
    and the other N − h papers have no more than h citations each."
    Note: If there are several possible values for h, the maximum one is taken as the h-index.

    Example:
    Input: citations = [3,0,6,1,5]
    Output: 3


    """
    # method 1: O(nlogn) time complexity
    # c=0
    # citations.sort(reverse=True)
    # for i in range(len(citations)):
    #     if citations[i]>=i+1:
    #         c+=1
    # return c


    # method 2: O(n) time complexity, O(n) space complexity
    n = len(citations)
    papers = [0] * (n + 1)
    
    # Counting papers for each citation number
    for citation in citations:
        papers[min(n, citation)] += 1
    
    # print(papers)
    k = 0
    for i in range(n, -1, -1):
        k += papers[i]
        if k >= i:
            return i
    return 0


#test cases
citations = [3,0,6,1,5]
print(hIndex(citations))

citations = [1,3,1]
print(hIndex(citations))
