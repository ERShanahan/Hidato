from board import HidatoBoard
from thinktank import iter_dyno as dyno

def main():
    print("Example 1: Solvable")
    board1 = [
        [1, 0, 0],
        [0, 3, 5],
        [8, 0, 0]
    ]
    hb1 = HidatoBoard(3)
    hb1.setBoard(board1)
    print("Initial Board:")
    hb1.print_board()
    print("\nSolving...\n")
    result1 = dyno(hb1, 1)
    if result1:
        print("Solved Board:")
        result1.print_board()
    else:
        print("No solution found.")
    print("\n" + "="*30 + "\n")

    print("Example 2: Multiple Solution Board")
    board2 = [
        [1, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 16],
        [0, 0, 0, 15]
    ]
    hb2 = HidatoBoard(4)
    hb2.setBoard(board2)
    print("Initial Board:")
    hb2.print_board()
    print("\nSolving...\n")
    result2 = dyno(hb2, 1)
    if result2:
        print("Solved Board:")
        result2.print_board()
    else:
        print("No solution found.")
    print("\n" + "="*30 + "\n")

    print("Example 3: Multiple Solution Board")
    board3 = [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 9]
    ]
    hb3 = HidatoBoard(3)
    hb3.setBoard(board3)
    print("Initial Board:")
    hb3.print_board()
    print("\nSolving...\n")
    result3 = dyno(hb3, 1)
    if result3:
        print("Solved Board:")
        result3.print_board()
    else:
        print("No solution found.")
    print("\n" + "="*30 + "\n")

if __name__ == "__main__":
    main()
