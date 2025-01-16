import tkinter as tk
from PIL import Image, ImageTk
import sys
from math import sin, cos, pi
import random
from collections import deque

# Function to draw a hexagon
def draw_hexagon(canvas, x, y, r, color="white", outline="black"):
    points=[]
    for i in range(6):
        angle=(pi/3)*i
        points.append((x+r*cos(angle), y+r*sin(angle)))
    flat_points=[coord for point in points for coord in point]
    canvas.create_polygon(flat_points, fill=color, outline=outline)

def is_point_in_hexagon(x, y, hex_x, hex_y, r):
    dx=abs(x-hex_x)/r
    dy=abs(y-hex_y)/r
    return dy<=0.5 and dx<=1-dy/2 or dy<=1 and dx<= 0.5

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
    elif x > 0 and y == 10:
        neighbors.append((x - 1, y))
        neighbors.append((x + 1, y))
        neighbors.append((x, y - 1))
        neighbors.append((x - 1, y - 1))
    return neighbors


# Class for game logic
class Game:
    def __init__(self, adversar, width=600, height=700, title="Trap The Mouse"):
        self.adversar = adversar
        self.root = tk.Tk()
        self.root.title(f"{title} : playing with {adversar}")
        self.canvas = tk.Canvas(self.root, width=width, height=height, bg="green")
        self.canvas.pack()
        self.running = True
        self.mouse_player = False
        self.tiles = {}
        self.message_label = tk.Label(self.root, text="",bg="red", font=("Arial", 12, "bold"), fg="blue", anchor="center")
        self.root.bind("<ButtonPress-1>", self.place_tile)
        if self.adversar=="player":
            self.level=0
            self.draw_board()
        if self.adversar=="calculator":
            self.choose_level()


    def choose_level(self):
        self.canvas.delete("all")
        self.canvas.create_text(
            300, 75, 
            text="Choose a dificulty level", 
            font=("Arial", 24, "bold"), 
            fill="black",
        )
        self.canvas.create_window(300,200, window=tk.Button(self.root, text="EASY", command=self.easy_lvl, bg="lightblue", fg="black", font=("Arial", 16, "bold"), relief="raised", width=40, height=2))
        self.canvas.create_window(300,300, window=tk.Button(self.root, text="MEDIUM", command=self.medium_lvl, bg="blue", fg="white", font=("Arial", 16, "bold"), relief="raised", width=40, height=2))
        self.canvas.create_window(300,400, window=tk.Button(self.root, text="HARD", command=self.hard_lvl, bg="darkblue", fg="white", font=("Arial", 16, "bold"), relief="raised", width=40, height=2))

    def easy_lvl(self):
        print("Ai ales nivelul 1: easy")
        self.level=1
        self.draw_board()
    def medium_lvl(self):
        print("Ai ales nivelul 2: medium")
        self.level=2
        self.draw_board()
    def hard_lvl(self):
        print("Ai ales nivelul 3: hard")
        self.level=3
        self.draw_board()

    def ai_easy(self):
        mouse_neighbors = get_neighbors(self.prev_mouse_coords)
        available_moves=[k for k in self.tiles.keys() if (self.tiles[k][1], self.tiles[k][2]) in mouse_neighbors and self.tiles[k][0]=="white"]
        print(available_moves)
        move = random.sample(available_moves, 1)[0]
        print(move)
        x, y = move
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
        self.tiles[(x, y)] = ("mouse", self.tiles[(x, y)][1], self.tiles[(x, y)][2])
        draw_hexagon(self.canvas, self.prev_mouse[0], self.prev_mouse[1], 30, color="white", outline="black")
        self.tiles[self.prev_mouse] = ("white", self.prev_mouse_coords[0], self.prev_mouse_coords[1])
        print(f"Moved mouse to {self.tiles[(x, y)][1]}, {self.tiles[(x, y)][2]}")
        self.prev_mouse = (x, y)
        self.prev_mouse_coords = (self.tiles[(x, y)][1], self.tiles[(x, y)][2])
        self.mouse_player = False
        if not self.game_over():
            self.root.bind("<ButtonPress-1>", self.place_tile)

    #algoritmul bfs
    def ai_medium(self):
        queue=deque([self.prev_mouse_coords])
        came_from={self.prev_mouse_coords:None}
        path = []
        while queue:
            print(queue)
            current=queue.pop()
            print(current)
            if current[0]==0 or current[0]==10 or current[1]==0 or current[1]==10:
                path =[]
                while current:
                    path.append(current)
                    current=came_from[current]
                path.reverse()
            if current is not None:
                for next in get_neighbors(current):
                    if next not in came_from and any(k for k in self.tiles.keys() if self.tiles[k][1]==next[0] and self.tiles[k][2]==next[1] and self.tiles[k][0]=="white"):
                        queue.append(next)
                        came_from[next]=current
        if not path:
            self.ai_easy()
        print(path)
        move=[k for k in self.tiles.keys() if self.tiles[k][1]==path[1][0] and self.tiles[k][2]==path[1][1]][0]
        x, y = move
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
        self.tiles[(x, y)] = ("mouse", self.tiles[(x, y)][1], self.tiles[(x, y)][2])
        draw_hexagon(self.canvas, self.prev_mouse[0], self.prev_mouse[1], 30, color="white", outline="black")
        self.tiles[self.prev_mouse] = ("white", self.prev_mouse_coords[0], self.prev_mouse_coords[1])
        print(f"Moved mouse to {self.tiles[(x, y)][1]}, {self.tiles[(x, y)][2]}")
        self.prev_mouse = (x, y)
        self.prev_mouse_coords = (self.tiles[(x, y)][1], self.tiles[(x, y)][2])
        self.mouse_player = False
        if not self.game_over():
            self.root.bind("<ButtonPress-1>", self.place_tile)

    #algoritmul a*
    def ai_hard(self):
        def heuristic(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])
        
        open_set = set([self.prev_mouse_coords])
        closed_set = set()
        came_from = {}
        g_score = {node: float('inf') for node in self.tiles.keys()}
        g_score[self.prev_mouse_coords] = 0
        f_score = {node: float('inf') for node in self.tiles.keys()}
        f_score[self.prev_mouse_coords] = heuristic(self.prev_mouse_coords, (0, 0))

        # Check if any neighbor is at the edge
        edge_positions = [(0, 0), (10, 0), (0, 10), (10, 10)]

        while open_set:
            current = min(open_set, key=lambda x: f_score[x])
            if current in edge_positions:
                path = [current]
                while current in came_from:
                    current = came_from[current]
                    path.append(current)
                path.reverse()
                break
            
            open_set.remove(current)
            closed_set.add(current)

            for neighbor in get_neighbors(current):
                if neighbor in closed_set or not any(k for k in self.tiles.keys() if self.tiles[k][1] == neighbor[0] and self.tiles[k][2] == neighbor[1] and self.tiles[k][0] == "white"):
                    continue

                tentative_g_score = g_score[current] + 1  # Assuming uniform cost for movement
                if neighbor not in open_set or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, (0, 0))
                    if neighbor not in open_set:
                        open_set.add(neighbor)
        else:
            self.ai_easy()

        if path:
            move = next(k for k in self.tiles.keys() if self.tiles[k][1] == path[1][0] and self.tiles[k][2] == path[1][1])
            x, y = move
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
            self.tiles[(x, y)] = ("mouse", self.tiles[(x, y)][1], self.tiles[(x, y)][2])
            draw_hexagon(self.canvas, self.prev_mouse[0], self.prev_mouse[1], 30, color="white", outline="black")
            self.tiles[self.prev_mouse] = ("white", self.prev_mouse_coords[0], self.prev_mouse_coords[1])
            print(f"Moved mouse to {self.tiles[(x, y)][1]}, {self.tiles[(x, y)][2]}")
            self.prev_mouse = (x, y)
            self.prev_mouse_coords = (self.tiles[(x, y)][1], self.tiles[(x, y)][2])
            self.mouse_player = False
            if not self.game_over():
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
                        break
                    else:
                        if self.level==0:
                            self.root.bind("<ButtonPress-1>", self.move_mouse)
                            break
                        if self.level==1:
                            self.ai_easy()
                            break
                        if self.level==2:
                            self.ai_medium()
                            break
                        if self.level==3:
                            self.ai_hard()
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
                        self.tiles[key] = ("mouse", self.tiles[key][1], self.tiles[key][2])
                        draw_hexagon(self.canvas, self.prev_mouse[0], self.prev_mouse[1], 30, color="white", outline="black")
                        self.tiles[self.prev_mouse] = ("white", self.prev_mouse_coords[0], self.prev_mouse_coords[1])
                        print(f"Moved mouse to {row}, {col}")
                        self.prev_mouse = (x, y)
                        self.prev_mouse_coords = (row, col)
                        self.mouse_player = False
                        if self.game_over():
                            break
                        else:
                            self.root.bind("<ButtonPress-1>", self.place_tile)
                            break
                else:
                    print(f"Nu poti muta soarecele la {x}, {y}")
                    break

    def game_over(self):
        mouse_pos=self.prev_mouse_coords
        if mouse_pos[0]==0 or mouse_pos[0]==10 or mouse_pos[1]==0 or mouse_pos[1]==10:
            print("Soarecele a castigat!")
            self.message_label.config(text="Soarecele a castigat!")
            self.message_label.pack(side="top", fill="x")
            self.root.unbind("<ButtonPress-1>")
            self.root.after(5000, self.root.destroy)
            return True
        mouse_neighbors = get_neighbors(mouse_pos)
        if all(self.tiles.get(next((key for key in self.tiles if self.tiles[key][1] == nx and self.tiles[key][2] == ny), None),
                               ("white",))[0] == "red" for nx, ny in mouse_neighbors):
            print("Soarecele a fost prins!")
            self.message_label.config(text="Soarecele a fost prins!")
            self.message_label.pack(side="top", fill="x")
            self.root.unbind("<ButtonPress-1>")
            self.root.after(5000, self.root.destroy)
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

    def draw_board(self):
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
