# main.py
import tkinter as tk
from game import Game
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, GRID_SIZE

def main():
    root = tk.Tk()
    root.title("Snake Game")

    canvas = tk.Canvas(root, width=SCREEN_WIDTH, height=SCREEN_HEIGHT, bg="black")
    canvas.pack()

    game = Game(canvas)

    def update_game():
        if game.update():
            game.draw()
            root.after(100, update_game)  # Call update_game after 100 milliseconds
        else:
            canvas.create_text(
                SCREEN_WIDTH / 2,
                SCREEN_HEIGHT / 2,
                text=f"Game Over! Score: {game.score}",
                fill="white",
                font=("Helvetica", 24),
            )

    def on_key_press(event):
        # Handle keyboard input to change the snake's direction
        key = event.keysym
        if key == "Up":
            game.snake.change_direction("UP")
        elif key == "Down":
            game.snake.change_direction("DOWN")
        elif key == "Left":
            game.snake.change_direction("LEFT")
        elif key == "Right":
            game.snake.change_direction("RIGHT")

    root.after(100, update_game)  # Start the game loop
    root.bind("<KeyPress>", on_key_press)  # Bind keyboard events
    root.mainloop()

if __name__ == "__main__":
    main()
