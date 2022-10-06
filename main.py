from tkinter import Tk, Canvas, PhotoImage
from PIL import Image, ImageDraw
from checkers.game import Game
from checkers.constants import X_SIZE, Y_SIZE, CELL_SIZE
from checkers.enums import SideType
from checkers.move import Move


def main():
    main_canvas = Image.new('RGB', (CELL_SIZE * X_SIZE, CELL_SIZE * Y_SIZE), color='#ffffff')

    game = Game(main_canvas, X_SIZE, Y_SIZE)
    game._Game__select_checker(2, 5)
    print(game._Game__get_moves_list(SideType.WHITE))

    main_canvas.save('desk.png')


if __name__ == '__main__':
    main()
