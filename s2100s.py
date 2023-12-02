
#2147. number of ways to divide a long corridor
class Solution2147:
    # Combinatorics 组合 - 数学
    def numberOfWays(self, corridor: str) -> int:
        MOD = 1_000_000_007

        positions = []

        for i, thing in enumerate(corridor):
            if thing == "S":
                positions.append(i)

        if positions == [] or len(positions) % 2 == 1:
            return 0

        count = 1

        prev_pair_last = 1
        curr_pair_first = 2

        while curr_pair_first < len(positions):
            count *= (positions[curr_pair_first] - positions[prev_pair_last])
            count %= MOD

            prev_pair_last += 2
            curr_pair_first += 2

        return count