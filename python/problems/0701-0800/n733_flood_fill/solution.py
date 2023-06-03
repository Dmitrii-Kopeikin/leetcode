from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        o_color = image[sr][sc]
        if o_color == color:
            return image

        directions = ((0, -1), (-1, 0), (0, 1), (1, 0))

        stack = [(sr, sc)]
        while stack:
            (r, c) = stack.pop()
            if image[r][c] == o_color:
                image[r][c] = color
                for (n_r, n_c) in directions:
                    n_r += r
                    n_c += c
                    if 0 <= n_r < len(image) and 0 <= n_c < len(image[0]) and image[n_r][n_c] == o_color:
                        stack.append((n_r, n_c))

        return image
