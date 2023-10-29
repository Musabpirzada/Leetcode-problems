class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = 10**9 + 7
        a_count = e_count = i_count = o_count = u_count = 1

        for _ in range(1, n):
            a_count_new = (e_count + i_count + u_count) % mod
            e_count_new = (a_count + i_count) % mod
            i_count_new = (e_count + o_count) % mod
            o_count_new = i_count % mod
            u_count_new = (i_count + o_count) % mod

            a_count, e_count, i_count, o_count, u_count = a_count_new, e_count_new, i_count_new, o_count_new, u_count_new

        return (a_count + e_count + i_count + o_count + u_count) % mod
