import tkinter as tk
from PIL import Image, ImageTk
import sys
from math import sin, cos, pi
import random
from collections import deque
from collections import Counter

def draw_hexagon(canvas, x, y, r, color="white", outline="black"):
    """
    Deseneaza un hexagon pe canvas.

    Parametrii:
          canvas (tkinter.Canvas): canvas-ul pe care va fi desenat hexagonul
          x (float): coordonata pe asa X a centrului hexagonului
          y (float): coordonata pe axa Y a centrului hexagonului
          r (float): raza hexagonului
          color (str): culoarea interiorului hexagonului
          outline (str): culoarea conturului hexagonului   

    """
    points=[]
    for i in range(6):
        angle=(pi/3)*i
        points.append((x+r*cos(angle), y+r*sin(angle)))
    flat_points=[coord for point in points for coord in point]
    canvas.create_polygon(flat_points, fill=color, outline=outline)

def is_point_in_hexagon(x, y, hex_x, hex_y, r):
    """
    Verifica daca un punct (x,y) se afla in interiorul unui hexagon.

    Parametrii:
            x (float): coordonata pe axa X a punctului 
            y (float): coordonata pe axa Y a punctului
            hex_x (float): coordonata pe axa X a centrului hexagonului
            hex_y (float): coordonata pe axa Y a centrului hexagonului
            r (float): raza hexagonului 

    """
    dx=abs(x-hex_x)/r
    dy=abs(y-hex_y)/r
    return dy<=0.5 and dx<=1-dy/2 or dy<=1 and dx<= 0.5

def get_neighbors(hex_coords):
    """
    Returneaza vecinii unui hexagon.

    Parametrii:
            hex_coords (tuplu): coordonatele (x, y) ale hexagonului

    Returneaza:
            neighbors (list): lista cu coordonatele tuturor vecinilor hexagonului

    """
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


class Game:
    """	
    Clasa pentru logica jocului Trap The Mouse.

    Atribute:
            adversar (str): tipul adversarului (player sau calculator)
            root (tkinter.Tk): fereastra principala a jocului
            canvas (tkinter.Canvas): canvas-ul pe care se desfasoara jocul
            tiles (dict): dictionar care contine informatii despre fiecare hexagon de pe tabla de joc (culoare, coordonate)
            message_label (tkinter.Label): label pentru afisarea mesajelor pe canvas
            level (int): nivelul de dificultate al calculatorului (0 = player, 1 = usor, 2 = mediu, 3 = greu)
            prev_mouse (tuplu): coordonatele hexagonului pe care se afla soarecele
            prev_mouse_coords (tuplu): coordonatele hexagonului pe care se afla soarecele in format (row, col)
            mouse_image_id (int): id-ul imaginii soarecelui de pe canvas

    Metode:
            __init__(self, adversar, width=600, height=700, title="Trap The Mouse"): constructor pentru clasa Game
            choose_level(self): creeaza o fereastra pentru alegerea nivelului de dificultate al calculatorului
            easy_lvl(self): seteaza valoarea parametrului level la 1 (usor) si apeleaza metoda draw_board
            medium_lvl(self): seteaza valoarea parametrului level la 2 (mediu) si apeleaza metoda draw_board
            hard_lvl(self): seteaza valoarea parametrului level la 3 (greu) si apeleaza metoda draw_board
            ai_easy(self): logica calculatorului pentru nivelul usor
            ai_medium(self): logica calculatorului pentru nivelul mediu
            ai_hard(self): logica calculatorului pentru nivelul greu
            place_tile(self, event): plaseaza un obstacol (piesa) pe tabla de joc
            move_mouse(self, event): muta soarecele pe tabla de joc
            game_over(self): verifica starea jocului 
            place_random_tiles(self): plaseaza in mod aleatoriu un numar de obstacole pe tabla de joc
            draw_board(self): deseneaza tabla de joc
            run(self): ruleaza jocul.

    """
    def __init__(self, adversar, width=600, height=700, title="Trap The Mouse"):
        """
        Constructor pentru clasa Game.

        Parametrii:
            adversar (str): tipul adversarului dat (player sau calculator)
            width (int): latimea canvas-ului
            height (int): inaltimea canvas-ului
            title (str): titlul ferestrei

        """
        self.adversar = adversar
        self.root = tk.Tk()
        self.root.title(f"{title} : playing with {adversar}")
        self.canvas = tk.Canvas(self.root, width=width, height=height, bg="green")
        self.canvas.pack()
        self.tiles = {}
        self.message_label = tk.Label(self.root, text="",bg="red", font=("Arial", 12, "bold"), fg="blue", anchor="center")
        self.root.bind("<ButtonPress-1>", self.place_tile)
        if self.adversar=="player":
            self.level=0
            self.draw_board()
        if self.adversar=="calculator":
            self.choose_level()


    def choose_level(self):
        """
        Creeaza o fereastra pentru ca jucatorul sa aleaga nivelul de dificultate al calculatorului.

        Creeaza butoane pentru fiecare nivel de dificultate (usor, mediu si greu).

        """
        self.canvas.delete("all")
        self.canvas.create_text(300, 75, text="Choose a dificulty level", font=("Arial", 24, "bold"), fill="black")
        self.canvas.create_window(300,200, window=tk.Button(self.root, text="EASY", command=self.easy_lvl, bg="lightblue", fg="black", font=("Arial", 16, "bold"), relief="raised", width=40, height=2))
        self.canvas.create_window(300,300, window=tk.Button(self.root, text="MEDIUM", command=self.medium_lvl, bg="blue", fg="white", font=("Arial", 16, "bold"), relief="raised", width=40, height=2))
        self.canvas.create_window(300,400, window=tk.Button(self.root, text="HARD", command=self.hard_lvl, bg="darkblue", fg="white", font=("Arial", 16, "bold"), relief="raised", width=40, height=2))

    def easy_lvl(self):
        """
        Seteaza valoarea parametrului level la 1 (usor) si apeleaza metoda draw_board.

        """
        print("Ai ales nivelul 1: easy")
        self.level=1
        self.draw_board()

    def medium_lvl(self):
        """
        Seteaza valoarea parametrului level la 2 (mediu) si apeleaza metoda draw_board.

        """
        print("Ai ales nivelul 2: medium")
        self.level=2
        self.draw_board()

    def hard_lvl(self):
        """
        Seteaza valoarea parametrului level la 3 (greu) si apeleaza metoda draw_board.

        """
        print("Ai ales nivelul 3: hard")
        self.level=3
        self.draw_board()

    def ai_easy(self):
        """
        Modalitatea de joc a calculatorului pentru nivelul usor.

        Alege in mod aleatoriu una dintre mutarile disponibile si muta soarecele pe acea pozitie.

        """
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
        if not self.game_over():
            self.root.bind("<ButtonPress-1>", self.place_tile)


    def ai_medium(self):
        """
        Modalitatea de joc a calculatorului pentru nivelul mediu.

        Foloseste algortimul BFS pentru a gasi un drum spre una dintre marginile tablei.

        """
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
        if not self.game_over():
            self.root.bind("<ButtonPress-1>", self.place_tile)

    def ai_hard(self):
        """
        Modalitatea de joc a calculatorului pentru nivelul greu.

        Foloseste algoritmul A* pentru a gasi cel mai bun drum spre una dintre marginile tablei,
        luand in considerare si numarul obstacolelor.

        """
        def heuristic(a, edges):
            return min(abs(a[0] - edge[0]) + abs(a[1] - edge[1]) for edge in edges)
        
        open_set = set([self.prev_mouse_coords])
        closed_set = set()
        came_from = {}
        g_score = {node: float('inf') for node in self.tiles.keys()}
        g_score[self.prev_mouse_coords] = 0
        f_score = {node: float('inf') for node in self.tiles.keys()}

        edges = [(0, 0), (10, 0), (0, 10), (10, 10)]
        f_score[self.prev_mouse_coords] = heuristic(self.prev_mouse_coords, edges)

        while open_set:
            current = min(open_set, key=lambda x: f_score[x])
            if current[0]==0 or current[0]==10 or current[1]==0 or current[1]==10:
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

                new_g_score = g_score[current] + Counter(k for k in self.tiles.keys() if (self.tiles[k][1], self.tiles[k][2]) in get_neighbors(neighbor) and self.tiles[k][0] == "red")[0]
                if neighbor not in open_set or new_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = new_g_score
                    f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, edges)
                    if neighbor not in open_set:
                        open_set.add(neighbor)

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
            if not self.game_over():
                self.root.bind("<ButtonPress-1>", self.place_tile)
        else:
            self.ai_easy()



    def place_tile(self, event):
        """
        Plaseaza o piesa pe tabla de joc.

        Parametrii:
            event (tk.Event): evenimentul care a generat apelul functiei

        Verifica daca coordonatele evenimentului se afla in interiorul unui hexagon liber (de culoare alba),
          in caz afirmativ, plaseaza obstacolul (hexagon de culoare rosie), iar in caz negativ, afiseaza un mesaj de eroare 
          si jucatorul poate alege o noua pozitie unde sa plaseze piesa.

        """
        for key in self.tiles:
            x, y = key
            if is_point_in_hexagon(event.x, event.y, x, y, 30):
                if self.tiles[key][0] == "white":
                    draw_hexagon(self.canvas, x, y, 30, color="red", outline="black")
                    self.tiles[key] = ("red", self.tiles[key][1], self.tiles[key][2])
                    print(f"Placed tile at {x}, {y}, {self.tiles[key]}")
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
        """
        Muta soarecele pe tabla de joc.

        Parametrii:
            event (tk.Event): evenimentul care a generat apelul functiei

        Verifica daca coordonatele evenimentului se afla in interiorul unui hexagon liber (de culoare alba) si vecin cu pozitia curenta
        a soarecelui, iar in caz afirmativ, muta soarecele pe noua pozitie. In caz negativ, 
        afiseaza un mesaj de eroare si jucatorul poate alege o noua pozitie pentru a muta soarecele.

        """
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
                        if self.game_over():
                            break
                        else:
                            self.root.bind("<ButtonPress-1>", self.place_tile)
                            break
                else:
                    print(f"Nu poti muta soarecele la {x}, {y}")
                    break

    def game_over(self):
        """
        Verifica starea jocului (daca acesta s-a terminat sau nu).

        Returneaza:
                bool: True daca jocul s-a terminat, False in caz contrar.

        """
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
        """
        Plaseaza in mod aleatoriu un numar de obstacole pe tabla de joc.

        """
        nr = random.randint(3, 10)
        tiles = list(k for k in self.tiles.keys() if k != (300.0, 365.7883832488647))
        tiles = random.sample(tiles, nr)
        for i in range(nr):
            x, y = tiles[i]
            draw_hexagon(self.canvas, x, y, 30, color="red", outline="black")
            self.tiles[(x, y)] = ("red", self.tiles[(x, y)][1], self.tiles[(x, y)][2])

    def draw_board(self):
        """
        Deseneaza tabla de joc.

        Apeleaza functia draw_hexagon pentru a desena hexagoanele in format de grid si le salveaza informatiile intr-un dictionar, 
        apeleaza functia place_random_tiles pentru a initializa tabla de joc cu diverse obstacolele si plaseaza soarecele pe centrul tablei.

        """
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
        """
        Ruleaza jocul.

        """
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
