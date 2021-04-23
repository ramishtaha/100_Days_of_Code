# import colorgram
#
# colors = colorgram.extract('C:\\Users\\ramis\\Desktop\\100_Days_of_Code_Challange\\DAY_18\\Practice\\spot_painting\\image.jpg', 35)
# colors_list = []
#
#
# for i in range(len(colors)):
#     # temp_list = [colors[i].rgb[r]]
#     # temp_list += [colors[i].rgb[g]]
#     # temp_list += [colors[i].rgb[b]]
#     color = colors[i]
#     rgb_color = []
#     for j in range(3):
#         rgb_color.append(color.rgb[j])
#     colors_list.append(tuple(rgb_color))
#
# print(colors_list)
import turtle as t
import random

colors_list = [(249, 212, 93), (150, 69, 97), (53, 99, 155), (232, 137, 62),
               (107, 174, 211), (243, 237, 241), (114, 83, 59), (201, 146, 177), (200, 77, 109), (145, 134, 72),
               (230, 90, 59),
               (141, 192, 140), (72, 103, 90), (68, 162, 92), (5, 165, 179), (227, 161, 183), (115, 126, 142),
               (163, 196, 221),
               (16, 66, 123), (187, 24, 34), (13, 56, 103), (235, 172, 160), (175, 201, 179), (163, 200, 215),
               (186, 27, 25),
               (80, 55, 37), (96, 61, 30), (53, 74, 65)]

trix = t.Turtle()
trix.penup()
trix.hideturtle()
t.colormode(255)
trix.setheading(225)
trix.forward(300)
trix.setheading(0)
trix.speed('fastest')
for _ in range(10):
    for _ in range(10):
        trix.dot(20, random.choice(colors_list))

        trix.forward(50)
    trix.setheading(90)
    trix.forward(50)
    trix.setheading(180)
    trix.forward(500)
    trix.setheading(360)


screen = t.Screen()
screen.exitonclick()
