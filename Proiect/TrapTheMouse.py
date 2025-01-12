import tkinter as tk
from PIL import Image, ImageTk
import sys
from math import sin, cos, pi
import random

# Function to draw a hexagon
def draw_hexagon(canvas, x, y, r, color="white", outline="black"):
    points = []
    for i in range(6):
        angle = (pi / 3) * i
        points.append((x + r * cos(angle), y + r * sin(angle)))
    flat_points = [coord for point in points for coord in point]
    canvas.create_polygon(flat_points, fill=color, outline=outline)

def is_point_in_hexagon(x, y, hex_x, hex_y, r):
    dx = abs(x - hex_x) / r
    dy = abs(y - hex_y) / r
    return dy <= 0.5 and dx <= 1 - dy / 2 or dy <= 1 and dx <= 0.5

def get_neighbors(hex_coords):
    x, y = hex_coords
    neighbors = []
    if x == 0 and y == 0:
        neighbors.append((x, y + 1))
        neighbors.append((x + 1, y))
    elif x == 0 and y == 10:
        neighbors.append((x, y - 1))
        neighbors.append((x + 1, y))
    elif x == 10 and y == 0:
        neighbors.append((x, y + 1))
        neighbors.append((x - 1, y))
        neighbors.append((x - 1, y + 1))
    elif x == 10 and y == 10:
        neighbors.append((x, y - 1))
        neighbors.append((x - 1, y))
        neighbors.append((x - 1, y - 1))
    elif x == 0 and y > 0 and y % 2 != 0:
        neighbors.append((x, y + 1))
        neighbors.append((x + 1, y))
        neighbors.append((x + 1, y + 1))
        neighbors.append((x, y - 1))
        neighbors.append((x + 1, y - 1))
    elif x > 0 and y == 0:
        neighbors.append((x - 1, y))
        neighbors.append((x + 1, y))
        neighbors.append((x, y + 1))
        neighbors.append((x - 1, y + 1))
    elif x > 0 and y > 0 and y % 2 != 0:
        neighbors.append((x - 1, y))
        neighbors.append((x + 1, y))
        neighbors.append((x, y + 1))
        neighbors.append((x + 1, y + 1))
        neighbors.append((x, y - 1))
        neighbors.append((x + 1, y - 1))
    elif x > 0 and y > 0 and y % 2 == 0:
        neighbors.append((x - 1, y))
        neighbors.append((x + 1, y))
        neighbors.append((x, y - 1))
        neighbors.append((x - 1, y - 1))
        neighbors.append((x + 1, y + 1))
        neighbors.append((x - 1, y + 1))
        neighbors.append((x, y + 1))
    elif x == 0 and y > 0 and y % 2 == 0:
        neighbors.append((x, y + 1))
        neighbors.append((x + 1, y))
        neighbors.append((x, y - 1))
    elif x == 10 and y > 0 and y % 2 != 0:
        neighbors.append((x, y + 1))
        neighbors.append((x - 1, y))
        neighbors.append((x, y - 1))
    elif x == 10 and y > 0 and y % 2 == 0:
        neighbors.append((x, y + 1))
        neighbors.append((x - 1, y))
        neighbors.append((x, y - 1))
        neighbors.append((x - 1, y - 1))
        neighbors.append((x - 1, y + 1))
    return neighbors


# Class for game logic
class Game:
    def __init__(self, adversar, width=600, height=700, title="Trap The Mouse"):
        self.adversar = adversar
        self.root = tk.Tk()
        self.root.title(f"{title} - {adversar}")
        self.canvas = tk.Canvas(self.root, width=width, height=height, bg="green")
        self.canvas.pack()
        self.running = True
        self.mouse_player = False
        self.tiles = {}
        self.message_label = tk.Label(self.root, text="", font=("Arial", 12), fg="blue")
        self.message_label.pack(pady=5)
        if adversar == "player":
            self.root.bind("<ButtonPress-1>", self.place_tile)

    def place_tile(self, event):
        for key in self.tiles:
            x, y = key
            if is_point_in_hexagon(event.x, event.y, x, y, 30):
                if self.tiles[key][0] == "white":
                    draw_hexagon(self.canvas, x, y, 30, color="red", outline="black")
                    self.tiles[key] = ("red", self.tiles[key][1], self.tiles[key][2])
                    print(f"Placed tile at {x}, {y}, {self.tiles[key]}")
                    self.mouse_player = True
                    if self.game_over():
                            self.root.unbind("<ButtonPress-1>")
                            break
                    else:
                        self.root.bind("<ButtonPress-1>", self.move_mouse)
                        break
                elif self.tiles[key][0] != "white":
                    print(f"Exista deja o piesa la {x}, {y}")
                    break

    def move_mouse(self, event):
        for key in self.tiles:
            x, y = key
            row, col = self.tiles[key][1], self.tiles[key][2]
            if is_point_in_hexagon(event.x, event.y, x, y, 30):
                if self.tiles[key][0] != "mouse" and (row, col) in get_neighbors(self.prev_mouse_coords):
                    if self.tiles[key][0] != "red":
                        if hasattr(self, 'mouse_image_id'):
                            self.canvas.delete(self.mouse_image_id)
                        mouse = Image.open("mouse.png")
                        mouse = mouse.resize((45, 45), Image.LANCZOS)
                        mouse_tk = ImageTk.PhotoImage(mouse)
                        label = tk.Label(image=mouse_tk)
                        label.image = mouse_tk
                        self.mouse_image_id = self.canvas.create_image(x, y, anchor=tk.CENTER, image=mouse_tk)
                        self.canvas.itemconfig(self.mouse_image_id, tags="clip")
                        self.canvas.lift("clip")
                        self.tiles[key] = "mouse"
                        draw_hexagon(self.canvas, self.prev_mouse[0], self.prev_mouse[1], 30, color="white", outline="black")
                        self.tiles[self.prev_mouse] = ("white", self.prev_mouse_coords[0], self.prev_mouse_coords[1])
                        print(f"Moved mouse to {row}, {col}")
                        self.prev_mouse = (x, y)
                        self.prev_mouse_coords = (row, col)
                        self.mouse_player = False
                        if self.game_over():
                            self.root.unbind("<ButtonPress-1>")
                            break
                        else:
                            self.root.bind("<ButtonPress-1>", self.place_tile)
                            break
                else:
                    print(f"Nu poti muta soarecele la {x}, {y}")
                    break

    def game_over(self):
        for key in self.tiles:
            c, x, y = self.tiles[key][0], self.tiles[key][1], self.tiles[key][2]
            if c == "mouse" and (y==0 or y==10 or x==0 or x==10):
                print("Soarecele a scapat")
                self.message_label.config(text="Soarecele a scapat")
                self.root.quit()
                return True
            elif c == "red":
                neighbors = get_neighbors((x, y))
                if all(self.tiles.get((nx, ny), ("white",))[0] == "red" for nx, ny in neighbors):
                    print("Soarecele a fost prins")
                    self.message_label.config(text="Soarecele a fost prins")
                    self.root.quit()
                    return True
        return False
            

    def place_random_tiles(self):
        nr = random.randint(3, 10)
        tiles = list(k for k in self.tiles.keys() if k != (300.0, 365.7883832488647))
        tiles = random.sample(tiles, nr)
        for i in range(nr):
            x, y = tiles[i]
            draw_hexagon(self.canvas, x, y, 30, color="red", outline="black")
            self.tiles[(x, y)] = ("red", self.tiles[(x, y)][1], self.tiles[(x, y)][2])

    def drawBoard(self):
        self.canvas.delete("all")
        vertical_spacing = 3**0.5 * 30
        horizontal_spacing = 1.5 * 30
        for row in range(11):
            for col in range(11):
                x = 75 + col * horizontal_spacing
                y = 80 + row * vertical_spacing
                if col % 2 == 1:
                    y += vertical_spacing / 2
                draw_hexagon(self.canvas, x, y, 30, color="white", outline="black")
                self.tiles.update({(x, y): ("white", row, col)})
                if row == 5 and col == 5:
                    mouse = Image.open("mouse.png")
                    mouse = mouse.resize((45, 45), Image.LANCZOS)
                    mouse_tk = ImageTk.PhotoImage(mouse)
                    label = tk.Label(image=mouse_tk)
                    label.image = mouse_tk
                    self.mouse_image_id = self.canvas.create_image(x, y, anchor=tk.CENTER, image=mouse_tk)
                    self.canvas.itemconfig(self.mouse_image_id, tags="clip")
                    self.canvas.lift("clip")
                    self.tiles.update({(x, y): ("mouse", row, col)})
                    self.prev_mouse = (x, y)
                    self.prev_mouse_coords = (row, col)
        self.place_random_tiles()
        print(self.tiles)

    def run(self):
        self.drawBoard()
        self.root.mainloop()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Foloseste comanda: python TrapTheMouse.py <tip adversar>")
        print("Tipuri de adversari: player, calculator")
        sys.exit(1)
    adversar = sys.argv[1]
    if adversar not in ["player", "calculator"]:
        print("Tip invalid de adversar")
        print("Tipul adversarului trebuie sa fie player sau calculator")
        sys.exit(1)
    game = Game(adversar)
    game.run()
