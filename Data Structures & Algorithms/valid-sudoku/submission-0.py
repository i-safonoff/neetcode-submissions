class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        counter = dict()

        prefs = ['row_', 'col_', 'sq_']
        digits = "123456789"
        default_list = [0] * 9
        for i in range(len(board)):
            for j in range(len(board)):
                posts = [i, j, (i // 3, j // 3)]
                val = board[i][j]
                if val in digits:
                    for k in range(len(prefs)):
                        key = f"{prefs[k]}{posts[k]}"
                        cur_state = counter.get(key, default_list.copy())
                        cur_state[int(val) - 1] += 1
                        if 2 in cur_state:
                            return False
                        counter[key] = cur_state

        return True