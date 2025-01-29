import unittest
from dfs import dfs
from constants import DIRECTIONS

class TestPathfindingAlgorithms(unittest.TestCase):
    def test_dfs(self):
        grid = [
            [0, 0, 0, 0, 0, 2],
            [0, 3, 3, 3, 3, 3],
            [0, 3, 0, 3, 0, 0],
            [0, 3, 0, 3, 0, 0],
            [0, 0, 0, 3, 3, 0],
            [1, 0, 0, 0, 0, 0]
        ]

        visited_nodes = list(dfs(grid, 5, 0))

        # Check if the goal was reached
        self.assertIn((0, 5), visited_nodes)

        # Ensure all visited nodes are valid (not walls)
        for r, c in visited_nodes:
            self.assertNotEqual(grid[r][c], 3)

        # Ensure the path is continuous (each step is adjacent)
        for i in range(1, len(visited_nodes)):
            r1, c1 = visited_nodes[i - 1]
            r2, c2 = visited_nodes[i]
            self.assertIn((r2 - r1, c2 - c1), DIRECTIONS)


if __name__ == "__main__":
    unittest.main()