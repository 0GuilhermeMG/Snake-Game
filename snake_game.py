from tkinter import *
import random

LARGURA_JOGO = 1000
ALTURA_JOGO = 1000
VELOCIDADE = 100
TAMANHO_ESPAÇO = 50
PARTES_DO_CORPO = 3
COR_DA_COBRA = "#00FF00"
COR_DA_COMIDA = "#FF0000"
COR_DE_FUNDO = "#008000"


class Cobra:
    
    def __init__(self):
        self.tamanho_corpo = PARTES_DO_CORPO
        self.coordenadas = []
        self.quadrados = []
        self.direcao = 'down'

        for i in range(0, PARTES_DO_CORPO):
            self.coordenadas.append([0,0])

        for x, y in self.coordenadas:
            quadrado = canvas.create_rectangle(x,y,x + TAMANHO_ESPAÇO, y + TAMANHO_ESPAÇO, fill=COR_DA_COBRA, tags="cobra")
            self.quadrados.append(quadrado)

class Comida:
   
    def __init__(self):
        
        
        x = random.randint(0, int(LARGURA_JOGO/TAMANHO_ESPAÇO) - 1) * TAMANHO_ESPAÇO
        y = random.randint(0, int(ALTURA_JOGO/TAMANHO_ESPAÇO) - 1) * TAMANHO_ESPAÇO

        self.coordinates = [x,y]

        canvas.create_oval(x,y,x + TAMANHO_ESPAÇO,y + TAMANHO_ESPAÇO, fill=COR_DA_COMIDA, tag="comida")

def proximo_passo(Cobra, Comidas):
    
    global comida
    x, y = cobra.coordenadas[0]

    if direcao == "up":
        y -= TAMANHO_ESPAÇO

    elif direcao == "down":
        y += TAMANHO_ESPAÇO

    elif direcao == "left":
        x -= TAMANHO_ESPAÇO

    elif direcao == "right":
        x += TAMANHO_ESPAÇO

    cobra.coordenadas.insert(0,(x,y))

    quadrado = canvas.create_rectangle(x,y,x + TAMANHO_ESPAÇO, y + TAMANHO_ESPAÇO, fill=COR_DA_COBRA)

    cobra.quadrados.insert(0, quadrado)

    if x == comida.coordinates[0] and y == comida.coordinates[1]:

        global placar

        placar += 1

        label.config(text="Placar:{}".format(placar))

        canvas.delete("comida")

        comida = Comida()

    else:

        del cobra.coordenadas[-1]

        canvas.delete(cobra.quadrados[-1])

        del cobra.quadrados[-1]

    if checar_colisoes(cobra):
        game_over()

    else:
        window.after(VELOCIDADE, proximo_passo, cobra, comida)


def mudar_direcao(new_direction):
    
    global direcao

    if new_direction == 'left':
        if direcao != 'right':
            direcao = new_direction

    elif new_direction == 'right':
        if direcao != 'left':
            direcao = new_direction

    elif new_direction == 'up':
        if direcao != 'down':
            direcao = new_direction

    elif new_direction == 'down':
        if direcao != 'up':
            direcao = new_direction


def checar_colisoes(cobra):
    
    x,y = cobra.coordenadas[0]

    if x < 0 or x >= LARGURA_JOGO:
        print("GAME OVER")
        return True
    
    elif y < 0 or y >= ALTURA_JOGO:
        print("GAME OVER")
        return True
    
    for PARTES_DO_CORPO in cobra.coordenadas[1:]:
        if x == PARTES_DO_CORPO[0] and y == PARTES_DO_CORPO[1]:
            print("GAME OVER")
            return True
        
    return False

def game_over():
    
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=("consolas",70), text=f"GAME OVER : {placar}", fill="red", tags="GAMEOVER")

window = Tk()
window.title("Jogo da cobra")
window.resizable(False, False)

placar = 0
direcao = 'down'

label = Label(window, text ="Placar:{}".format(placar,font=("consolas",40)))
label.pack()

canvas = Canvas(window, bg=COR_DE_FUNDO, height =ALTURA_JOGO, width=LARGURA_JOGO)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_width / 2) - (window_width / 2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<Left>', lambda event: mudar_direcao('left'))
window.bind('<Right>', lambda event: mudar_direcao('right'))
window.bind('<Up>', lambda event: mudar_direcao('up'))
window.bind('<Down>', lambda event: mudar_direcao('down'))

cobra = Cobra()
comida = Comida()

proximo_passo(cobra, comida)

window.mainloop()