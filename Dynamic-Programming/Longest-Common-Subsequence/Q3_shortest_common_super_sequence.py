# shortest super subsequence
# given two string find out subsequence which contains all character from both string
# common(text1, text2) + uncommon(text1, text2)
# ie lcs(text1, text2) + extra(text1) + extra(text2)
# this problem is extension of longest common subsequence

from Q1_longest_common_subsequence import Solution as LCS
class Solution:
    def tabulation_shortest_super_sequence(self, text1, text2):

        lcs_solution = LCS()
        lcs = lcs_solution.tabulation_lcs(text1, text2)
        # TODO


        pass

if __name__ == '__main__':
    pass
