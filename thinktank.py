def rec_dyno(hb, num):
    if num == hb.size**2 and hb.isSolved():
        return hb
    if num == hb.size**2 + 1:
        return None

    start = hb.find(num)
    if start == None: return None
    x, y = start

    if hb.find(num+1) != None:
        if hb.isNeighbor(num + 1, (x, y)):
            return rec_dyno(hb, num + 1)
        return None

    for dx, dy in hb.directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < hb.size and 0 <= ny < hb.size and hb.board[ny][nx] == 0:
            new_board = hb.place(num + 1, nx, ny)
            result = rec_dyno(new_board, num + 1)
            if result is not None:
                return result

    return None

def iter_dyno(hb, start):
    stack = [(hb, 1)]

    while stack:
        current_board, num = stack.pop()
        
        if num == current_board.size**2 and current_board.isSolved():
            return current_board
        
        if num == current_board.size**2 + 1:
            continue

        start = current_board.find(num)
        if start is None:
            continue

        x, y = start
        
        if current_board.find(num + 1) is not None:
            if current_board.isNeighbor(num + 1, (x, y)):
                stack.append((current_board, num + 1))
                continue
            else:
                continue
        
        for dx, dy in current_board.directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < current_board.size and 0 <= ny < current_board.size and current_board.board[ny][nx] == 0:
                new_board = current_board.place(num + 1, nx, ny)
                stack.append((new_board, num + 1))

    return None
