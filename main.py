# ##Draw a line

# from turtle import Turtle, Screen

# timmy = Turtle()

# timmy.shape('triangle')
# timmy.forward(50)
# timmy.color('medium blue')

# screen = Screen()
# screen.exitonclick()




# #####Turtle Intro######
# from turtle import Screen
# import turtle as t

# timmy_the_turtle = t.Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")
# # timmy_the_turtle.forward(100)
# # timmy_the_turtle.backward(200)
# # timmy_the_turtle.right(90)
# # timmy_the_turtle.left(180)
# # timmy_the_turtle.setheading(0)


# ######## Draw a Square ############

# for _ in range(4):
#   timmy_the_turtle.forward(100)
#   timmy_the_turtle.right(90)

# screen = Screen()
# screen.exitonclick()

# ############Draw a dashed line##############
# from turtle import Turtle, Screen

# timmy = Turtle()

# for _ in range(10):
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()
#     timmy.forward(10)

# screen = Screen()
# screen.exitonclick()


# ##########Draw a penthagon#######################
# from turtle import Turtle, Screen

# timmy = Turtle()

# nr_sides=5
# angle=360/nr_sides
# for _ in range(nr_sides):
#     timmy.forward(50)
#     timmy.right(angle)


# screen = Screen()
# screen.exitonclick()


# ###########Draw a different shape (triangle, octaghon) with diffrent colors###########

# from turtle import Turtle, Screen
# import random

# timmy = Turtle()

# colors=['dark green','royal blue', 'yellow', 'light coral', 'blue violet']


# def draw_shape(nr_sides):
#     angle=360/nr_sides
#     for _ in range(nr_sides):
#         timmy.forward(100)
#         timmy.right(angle)

# #making sides non staticly
# # wykorzystuję pętlę w zakresie jaki mnie interesuje
# for shape_side in range(3,11):
#     draw_shape(shape_side)
#     timmy.color(random.choice(colors)) 
#     #wykorzustyje wcześniej napisaną funkcje,
#     #gdzie jako argument przekazywana jest ilość boków(shape_side) z zakresu 3-10

# screen = Screen()
# screen.exitonclick()

# #Draw random walk

# from turtle import Turtle, Screen
# import random

# timmy = Turtle()

# colors=['dark green','royal blue', 'yellow', 'light coral', 'blue violet']
# directions=[0, 90, 180, 270]
# timmy.pensize(10)
# timmy.speed('fastest')

# for _ in range(100):
#     timmy.color(random.choice(colors))
#     timmy.forward(20)
#     timmy.setheading(random.choice(directions))

# screen = Screen()
# screen.exitonclick()

#Draw a spirograph
# from turtle import Turtle, Screen
# import random

# # Random rgb color
# def random_color():
#     r = radom.randint(0,255)
#     g = radom.randint(0,255)
#     b = radom.randint(0,255)
#     rgb_color=(r, g, b)
#     return rgb_color

# timmy = Turtle()
# timmy.speed('fastest')
# timmy.colormode(255) ######## nie działa to


###nie działa
#add random rgb color to turtle
# timmy.color(random_color)



################rysuje statycznie 10 kółek z odstępem 10 --- wstępna moja wersja###############
# angle = 0
# for _ in range(10):
#     angle+=10
#     timmy.circle(50)
#     timmy.setheading(angle)
###############################################################################################





#####wersja angela ############################################################################

#timmy.heading() to aktualna pozycja żółwia, czyli 0, tak samo jako moje angle ustawione na 0
# def draw_spiro(size_gap):
#     for _ in range(int(360/size_gap)):
#         timmy.circle(100)
#         timmy.setheading(timmy.heading()+size_gap)

# # draw_spiro(5)#przekazuję statycznie wielkość size_gap
# draw_spiro(random.randint(1,10))
###############################################################################################




######moja wersja na spirgraph############

# def draw_360(size_gap):
#     count=int(360/size_gap)
#     angle = 0
#     for _ in range(count):
#         angle+=10
#         timmy.circle(50)
#         timmy.setheading(angle)


# #przekzanie do funkcji za pomocą pętli wielkości size_gap
# size_gap=0
# for size_gap in range(0,361):
#     draw_360(size_gap+10)

# ######################################



# screen = Screen()
# screen.exitonclick()

############Hirst painting###################

import turtle as turtle_module
import random

turtle_module.colormode(255)
color_page = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), 
              (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), 
              (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), 
              (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), 
              (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), 
              (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), 
              (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

tim = turtle_module.Turtle()
tim.speed('fastest')
tim.penup()
tim.hideturtle()

#nie goto() bo nie mamy zadeklarowanego okna
# tim.goto()

#zejście niżej okna
tim.setheading(225) # po skosie na dół
tim.forward(300)
tim.setheading(0)# obrót na E wschód <

number_of_dots = 100


for dot_count in range(1, number_of_dots+1):
    tim.dot(20, random.choice(color_page))
    tim.forward(50) #jazda w bok i postawienie kropki
    
    if dot_count % 10 == 0: #jeżeli mineło 10 kropek
        #nowa linia
        tim.setheading(90)# north^
        tim.forward(50)#wjazd na góre
        tim.setheading(180)#west zachód <
        tim.forward(500)# przejazd 10 kropek po 50 <---- to jest powrót
        tim.setheading(0)#obrót na wschód>



# tim.pendown()
# for x in range(10):
#     tim.seth(90)
#     for _ in range(10):
#         tim.forward(50)

    
# tim.penup()



screen =turtle_module.Screen()
screen.exitonclick()