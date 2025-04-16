import tkinter as tk
import random

class MemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Game")

        # Zoznam písmen, ktoré sa budú používať ako hodnoty kariet
        self.cards = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        self.cards = self.cards * 2  # Dvojité páry písmen
        random.shuffle(self.cards)

        self.buttons = []
        self.flipped = []
        self.matches = 0

        self.create_buttons()

    def create_buttons(self):
        """Vytvoriť tlačidlá pre každú kartu"""
        for row in range(4):  # 4 riadky
            button_row = []
            for col in range(4):  # 4 stĺpce
                button = tk.Button(self.root, text=" ", width=10, height=4,
                                   command=lambda r=row, c=col: self.flip_card(r, c))
                button.grid(row=row, column=col)
                button_row.append(button)
            self.buttons.append(button_row)

    def flip_card(self, row, col):
        """Otočí kartu pri kliknutí"""
        if len(self.flipped) == 2:
            return

        card_value = self.cards[row * 4 + col]
        self.buttons[row][col].config(text=card_value, state="disabled")  # Zobrazíme písmeno

        self.flipped.append((row, col, card_value))

        if len(self.flipped) == 2:
            self.root.after(1000, self.check_match)

    def check_match(self):
        """Skontroluje, či sú dve otočené karty rovnaké"""
        first_row, first_col, first_value = self.flipped[0]
        second_row, second_col, second_value = self.flipped[1]

        if first_value == second_value:
            self.matches += 1
            self.flipped = []

            # Zmeniť farbu na zlatú pre nájdené karty
            self.buttons[first_row][first_col].config(bg="gold", state="disabled")
            self.buttons[second_row][second_col].config(bg="gold", state="disabled")

            if self.matches == 8:  # Hra končí, keď sú všetky páry nájdené
                self.game_over()

        else:
            self.buttons[first_row][first_col].config(text=" ", state="normal")
            self.buttons[second_row][second_col].config(text=" ", state="normal")
            self.flipped = []

    def game_over(self):
        """Zobrazí správu o výhre"""
        game_over_label = tk.Label(self.root, text="Game Over! You won!", font=("Helvetica", 16))
        game_over_label.grid(row=4, column=0, columnspan=4)

if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()
