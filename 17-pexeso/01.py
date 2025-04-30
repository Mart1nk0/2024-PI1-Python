import tkinter as tk
import random
import time

class MemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Game")

        self.cards = list(range(8)) * 2  # 8 pairs of cards
        random.shuffle(self.cards)

        self.buttons = []
        self.flipped = []
        self.matches = 0

        self.create_buttons()
    
    def create_buttons(self):
        for row in range(4):  # 4 rows
            button_row = []
            for col in range(4):  # 4 columns
                button = tk.Button(self.root, text=" ", width=10, height=4,
                                   command=lambda r=row, c=col: self.flip_card(r, c))
                button.grid(row=row, column=col)
                button_row.append(button)
            self.buttons.append(button_row)

    def flip_card(self, row, col):
        # Prevent clicking if two cards are already flipped
        if len(self.flipped) == 2:
            return

        card_value = self.cards[row * 4 + col]
        self.buttons[row][col].config(text=str(card_value), state="disabled")

        self.flipped.append((row, col, card_value))

        if len(self.flipped) == 2:
            self.root.after(1000, self.check_match)

    def check_match(self):
        first_row, first_col, first_value = self.flipped[0]
        second_row, second_col, second_value = self.flipped[1]

        if first_value == second_value:
            self.matches += 1
            self.flipped = []

            if self.matches == 8:  # Game ends when all pairs are matched
                self.game_over()

        else:
            self.buttons[first_row][first_col].config(text=" ", state="normal")
            self.buttons[second_row][second_col].config(text=" ", state="normal")
            self.flipped = []

    def game_over(self):
        game_over_label = tk.Label(self.root, text="Game Over! You won!", font=("Helvetica", 16))
        game_over_label.grid(row=4, column=0, columnspan=4)

if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()
gdgd =  2