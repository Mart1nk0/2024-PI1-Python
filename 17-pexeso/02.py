import tkinter as tk
import random

class MemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Game")

        self.cards = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'] * 2  # 8 písmen, každý pár sa objaví 2x
        random.shuffle(self.cards)

        self.buttons = []
        self.flipped = []
        self.matches = 0

        self.colors = {
            'A': '#FF5733',  # červená
            'B': '#33FF57',  # zelená
            'C': '#3357FF',  # modrá
            'D': '#FFFF33',  # žltá
            'E': '#FF33A1',  # ružová
            'F': '#33FFF9',  # tyrkysová
            'G': '#9B33FF',  # fialová
            'H': '#FF9133'   # oranžová
        }

        self.create_buttons()
    
    def create_buttons(self):
        for row in range(4):  # 4 riadky
            button_row = []
            for col in range(4):  # 4 stĺpce
                button = tk.Button(self.root, text=" ", width=10, height=4,
                                   font=("Helvetica", 34),  # Nastavíme väčšie písmo
                                   command=lambda r=row, c=col: self.flip_card(r, c))
                button.grid(row=row, column=col)
                button_row.append(button)
            self.buttons.append(button_row)

    def flip_card(self, row, col):
        # Zabránenie kliknutiu, ak sú už dve karty obrátené
        if len(self.flipped) == 2:
            return

        card_value = self.cards[row * 4 + col]
        self.buttons[row][col].config(text=card_value, state="disabled", 
                                      bg=self.colors[card_value])  # Nastavíme text a farbu karty

        self.flipped.append((row, col, card_value))

        if len(self.flipped) == 2:
            self.root.after(1000, self.check_match)

    def check_match(self):
        first_row, first_col, first_value = self.flipped[0]
        second_row, second_col, second_value = self.flipped[1]

        if first_value == second_value:
            self.matches += 1
            self.flipped = []

            if self.matches == 8:  # Hra končí, keď sú všetky páry nájdené
                self.game_over()

        else:
            self.buttons[first_row][first_col].config(text=" ", state="normal", bg='SystemButtonFace')
            self.buttons[second_row][second_col].config(text=" ", state="normal", bg='SystemButtonFace')
            self.flipped = []

    def game_over(self):
        game_over_label = tk.Label(self.root, text="Game Over! You won!", font=("Helvetica", 16))
        game_over_label.grid(row=4, column=0, columnspan=4)

if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()
