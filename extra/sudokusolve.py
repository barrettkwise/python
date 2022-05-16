class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        nums = {str(i) for i in range(1, 10)}
        rows, cols, boxes = [set() for _ in range(9)], [set() for _ in range(9)], [set() for _ in range(9)]
        for i, row in enumerate(board):
            for j, n in enumerate(row):
                if n == ".":
                    continue
                rows[i].add(n)
                cols[j].add(n)
                boxes[i//3*3+j//3].add(n)

        def back_tracking(ir: int, ic: int) -> bool:
            while board[ir][ic] != ".":
                if ic < 8:
                    ic += 1
                elif ir < 8:
                    ir += 1
                    ic = 0
                else:   # completed
                    return True

            ib = ir//3*3+ic//3
            for num in nums - (rows[ir] | cols[ic] | boxes[ib]):
                rows[ir].add(num)
                cols[ic].add(num)
                boxes[ib].add(num)
                board[ir][ic] = str(num)
                if back_tracking(ir, ic):
                    return True
                rows[ir].remove(num)
                cols[ic].remove(num)
                boxes[ib].remove(num)
                board[ir][ic] = "."
            return False

        back_tracking(0, 0)
