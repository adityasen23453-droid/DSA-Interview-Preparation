// Problem: Merge Intervals
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python
// Verdict: Accepted
// URL: https://leetcode.com/problems/merge-intervals/
// Solved on: 2026-10-31T16:35:07.974Z

class Solution(object):
    def merge(self, intervals):
        i = 0
        temp = []
        intervals.sort(key = lambda x : x[0])
        temp.append(intervals[0])
        for i in range(1 ,len(intervals)):
            if intervals[i][0] <= temp[-1][1] :
                temp[-1][1] = max(intervals[i][1],temp[-1][1])
            else :
                temp.append(intervals[i])
        return temp
