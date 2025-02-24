import turtle
import time

#Pokeball clicker v0.5

"""Outil permettant... De compter les clics !"""
"""Attention cependant à ne pas cliquer trop vite, le module Turtle n'est pas le plus adapté pour ce programme !"""
"""A partir d'un certain nombre de clics l'image de la pokéball change."""

# définir la fenêtre
wn = turtle.Screen()
wn.title("Poké-Ball Clicker (v0.5)")
wn.bgcolor("black")

# définir le compteur de clics
clicks = 0

# définir l'image initiale de la pokéball 
wn.register_shape("faiblo_ball.gif")
pokeball = turtle.Turtle()
pokeball.speed(0)
pokeball.shape("faiblo_ball.gif")

# définir texte initial
pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0, 200)
pen.write(f"Clicks: {clicks}", align="center", font=("Verdana", 35, "normal"))

# fonction qui ajoute 1, ou plus, au compteur de clics
def clicked(x, y):
    global clicks
    clicks += 1
    pen.clear()
    time.sleep(0.01)
    pen.goto(0, 200)
    pen.write(f"Clicks: {clicks}", align="center", font=("Verdana", 35, "normal"))

    # changements d'image de la pokéball
    if (clicks >= 20) and (clicks < 100):
        wn.register_shape("poke_ball.gif")
        pokeball.shape("poke_ball.gif")  
        clicks += 1
        
    elif (clicks >= 100) and (clicks < 500):
        wn.register_shape("bis_ball.gif")
        pokeball.shape("bis_ball.gif")
        clicks += 2
    
    elif (clicks >= 500) and (clicks < 1000):
        wn.register_shape("speed_ball.gif")
        pokeball.shape("speed_ball.gif")
        clicks += 6
    
    elif (clicks >= 1000) and (clicks < 3500):
        wn.register_shape("super_ball.gif")
        pokeball.shape("super_ball.gif")
        clicks += 11
    
    elif (clicks >= 3500) and (clicks < 8000):
        wn.register_shape("copain_ball.gif")
        pokeball.shape("copain_ball.gif")
        clicks += 19

    elif (clicks >= 8000) and (clicks < 20000):
        wn.register_shape("safari_ball.gif")
        pokeball.shape("safari_ball.gif")
        clicks += 39

    elif (clicks >= 20000) and (clicks < 50000):
        wn.register_shape("hyper_ball.gif")
        pokeball.shape("hyper_ball.gif")
        clicks += 64

    elif (clicks >= 50000) and (clicks < 100000):
        wn.register_shape("niveau_ball.gif")
        pokeball.shape("niveau_ball.gif")
        clicks += 94
    
    elif (clicks >= 100000) and (clicks < 400000):
        wn.register_shape("sombre_ball.gif")
        pokeball.shape("sombre_ball.gif")
        clicks += 119

    elif (clicks >= 400000) and (clicks < 1200000):
        wn.register_shape("rapide_ball.gif")
        pokeball.shape("rapide_ball.gif")
        clicks += 249

# appeler fonction "clicked" lorsqu'on clique sur la pokéball
pokeball.onclick(clicked)

# indispensable pour l'affichage de la fenêtre en module Turtle
wn.mainloop()