import numpy as np
import random as rnd
from tkinter import *


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Segment:
    def __init__(self, A, B):
        self.A = B.x - A.x
        self.B = B.y - A.y


class Polygone:
    def __init__(self, List):
        self.List = []


def determinant(AB, AC):  # Ici on fait le produit vectoriel et plus précisément on cherche le déterminant ce qui nous permet de savoir si le point est à gauche ou à droite du segment
    det = (AB.A * AC.B - AC.B * AB.B)
    return det


def orientation(AB, AC):
    det = determinant(AB, AC)
    if det > 0:
        print("Le point est à gauche du segment sur la Zone 4")
    elif det < 0:
        print("Le point est à droite du segment sur la Zone5 ")
        return 5
    elif det == 0:
        scalaireap = np.dot(AB,
                            AC)  # ici on fait le produit scalaire cequi nous permet de savoir si le point est devant ou derrière le segment (plus long ou négatif
        if scalaireap < 0:
            print("Le point est derrière le point A en Zone 3 ")
        else:
            scalaireab = np.dot(AB, AB)
            if scalaireap > scalaireab:
                print("Le point est au delà du segment sur la Zone 2")
            else:
                print("Le point est sur le segment sur la Zone 1 ")

def orientationPoly(AB, AC):
    det = determinant(AB, AC)
    if det > 0:
        print("Le point est à gauche du segment sur la Zone5 ")
        return 4
    elif det < 0:
        print("Le point est à droite du segment sur la Zone5 ")
        return 5





def PolyConvConc(List):
    long = len(List)
    listSegm = []
    verifdroite = 0
    verifgauche = 0
    test = 0
    for i in range(0, long):
        modulo1 = (i + 1) % long
        modulo2 = (i + 2) % long
        listSegm.append(Segment(List[i], List[modulo1]))
    for i in range(0, long):

        modulo1 = (i + 1) % long
        modulo2 = (i + 2) % long
        test = orientationPoly(listSegm[i], listSegm[modulo1])
        if test == 5:
            verifdroite += 1
        elif test == 4:
            verifgauche +=1
    if verifgauche == (long) or verifdroite == (long):
        print("Le Polygone est Convexe")
    else:
        print("Le Polygone est Concave")
    print("Verif gauche = ", verifgauche)
    print("Verif droite = ", verifdroite)








# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    A = Point(rnd.randrange(0, 100), rnd.randrange(0, 100))
    B = Point(rnd.randrange(0, 100), rnd.randrange(0, 100))
    C = Point(rnd.randrange(0, 100), rnd.randrange(0, 100))
    D = Point(rnd.randrange(0, 100), rnd.randrange(0, 100))
    E = Point(rnd.randrange(0, 100), rnd.randrange(0, 100))

    List = [A, B, C, D, E]
    AB = Segment(A, B)
    AC = Segment(A, C)

    canva = Tk()
    canva.title("Polygone")
    canva.geometry("600x600")




    # Define a function to draw the line between two points
    def draw_line(event):
        x1 = event.x
        y1 = event.y
        x2 = event.x
        y2 = event.y
        # Draw an oval in the given co-ordinates
        canvas.create_oval(x1, y1, x2, y2, fill="black", width=8)
        return x1,y1


    # Create a canvas widget
    canvas = Canvas(canva, width=500, height=500, background="white")
    canvas.place(x=50 , y=50)
    canvas.bind('<Button-1>', draw_line)
    click_num = 0




    canva.mainloop()

    # orientation(det, AB, AC)
    PolyConvConc(List)
    ##print("Le point A à pour coordinate x = ", A.x, "et y = ", A.y)
    ##print("Le point B à pour coordinate x = ", B.x, "et y = ", B.y)
    ##print("Le point C à pour coordinate x = ", C.x, "et y = ", C.y)
