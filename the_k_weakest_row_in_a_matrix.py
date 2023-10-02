class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        row_strength = [(i, sum(row)) for i, row in enumerate(mat)]
        row_strength.sort(key=lambda x: (x[1], x[0]))
        return [row[0] for row in row_strength[:k]]
