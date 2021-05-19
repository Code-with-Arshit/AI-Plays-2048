from tkinter import Frame, Label, CENTER

import AI
import game_functions

edge_lenght = 400
cell_count = 4
cell_pad = 10

up_key = "'w'"
down_key = "'s'"
left_key = "'a'"
right_key = "'d'"
AI_key = "'q'"
AI_Play_key = "'p'"

label_font = ("Verdana", 40, "bold")

game_colour = "#a6bdbb"

empty_colour = "#8eaba8"

tile_colours = {2: "#daeddf", 4: "#9ae3ae", 8: "#6ce68d", 16: "#42ed71",
                   32: "#17e650", 64: "#17c246", 128: "#149938",
                   256: "#107d2e", 512: "#0e6325", 1024: "#0b4a1c",
                   2048: "#031f0a", 4096: "#000000", 8192: "#000000",}

label_colours = {2: "#011c08", 4: "#011c08", 8: "#011c08", 16: "#011c08",
                   32: "#011c08", 64: "#f2f2f0", 128: "#f2f2f0",
                   256: "#f2f2f0", 512: "#f2f2f0", 1024: "#f2f2f0",
                   2048: "#f2f2f0", 4096: "#f2f2f0", 8192: "#f2f2f0",}

class Display(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.grid()
        self.master.title("2048")
        self.master.bind("<Key>", self.key_press)

        self.command = {up_key: game_functions.move_up,
                     down_key: game_functions.move_down,
                     left_key: game_functions.move_left,
                     right_key: game_functions.move_right,
                     AI_key: AI.ai_move,
                     }

        self.grid_cells = []
        self.build_grid()
        self.init_matrix()
        self.draw_grid_cells()

        self.mainloop()

    def build_grid(self):
        background = Frame(self, bg=game_colour,
                           width=edge_lenght, height=edge_lenght)
        background.grid()

        for row in range(cell_count):
            grid_row = []
            for col in range(cell_count):
                cell = Frame(background, bg=empty_colour,
                             width=edge_lenght / cell_count,
                             height=edge_lenght / cell_count)
                cell.grid(row=row, column=col, padx=cell_pad,
                          pady=cell_pad)
                t = Label(master=cell, text="",
                          bg=empty_colour,
                          justify=CENTER, font=label_font, width=5, height=2)
                t.grid()
                grid_row.append(t)

            self.grid_cells.append(grid_row)

    def init_matrix(self):
        self.matrix = game_functions.initialize_game()

    def draw_grid_cells(self):
        for row in range(cell_count):
            for col in range(cell_count):
                tile_value = self.matrix[row][col]
                if not tile_value:
                    self.grid_cells[row][col].configure(
                        text="", bg=empty_colour)
                else:
                    self.grid_cells[row][col].configure(text=str(
                        tile_value), bg=tile_colours[tile_value],
                    fg=label_colours[tile_value])
        self.update_idletasks()

    def key_press(self, event):
        valid_game = True
        key = repr(event.char)
        if key == AI_Play_key:
            move_count = 0
            while valid_game:
                self.matrix, valid_game = AI.ai_move(self.matrix, 40, 30)
                if valid_game:
                    self.matrix = game_functions.add_new_tile(self.matrix)
                    self.draw_grid_cells()
                move_count += 1
        if key == AI_key:
            self.matrix, move_made, = AI.ai_move(self.matrix, 20, 30)
            if move_made:
                self.matrix = game_functions.add_new_tile(self.matrix)
                self.draw_grid_cells()
            move_count += 1

        elif key in self.command:
            self.matrix, move_made, _ = self.command[repr(event.char)](self.matrix)
            if move_made:
                self.matrix = game_functions.add_new_tile(self.matrix)
                self.draw_grid_cells()
                move_made = False
gamegrid = Display()