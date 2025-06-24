# Last updated: 6/25/2025, 4:11:41 AM
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        empty = []

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empty.append((r, c))
                else:
                    num = board[r][c]
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[(r // 3) * 3 + (c // 3)].add(num)

        def backtrack():
            if not empty:
                return True

            # MRV: Choose the empty cell with fewest options
            empty.sort(key=lambda rc: len([
                num for num in map(str, range(1, 10))
                if num not in rows[rc[0]] and num not in cols[rc[1]] and num not in boxes[(rc[0] // 3) * 3 + (rc[1] // 3)]
            ]))
            r, c = empty.pop(0)
            box_idx = (r // 3) * 3 + (c // 3)

            for num in map(str, range(1, 10)):
                if num not in rows[r] and num not in cols[c] and num not in boxes[box_idx]:
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box_idx].add(num)

                    if backtrack():
                        return True

                    board[r][c] = '.'
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[box_idx].remove(num)

            empty.insert(0, (r, c))
            return False

        backtrack()
