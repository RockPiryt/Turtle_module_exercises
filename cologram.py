#pip install colorgram.py

import colorgram

rgb_colors=[]
colors = colorgram.extract('image.jpg', 30)
for x in colors:
    r = x.rgb.r
    g = x.rgb.g
    b = x.rgb.b
    new_color=(r,g,b)
    rgb_colors.append(new_color)

print(rgb_colors)

#zwraca listę krotek
#[(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241)]

color_page = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]


###Angela 1###################
# rgb_colors=[]
# colors = colorgram.extract('image.jpg', 30)
# for x in colors:
#     rgb_colors.append(x.rgb)
# print(rgb_colors)

# zwraca [Rgb(r=245, g=243, b=238), Rgb(r=246, g=242, b=244), Rgb(r=202, g=164, b=110),



#####first item from list########
# first_color = colors[0]
# print(first_color)

#zwraca <colorgram.py Color: Rgb(r=245, g=243, b=238), 64.68350168350169%>

####description from page##############
# #example
# import colorgram

# # Extract 6 colors from an image.
# colors = colorgram.extract('sweet_pic.jpg', 6)

# # colorgram.extract returns Color objects, which let you access
# # RGB, HSL, and what proportion of the image was that color.
# first_color = colors[0]
# rgb = first_color.rgb # e.g. (255, 151, 210)
# hsl = first_color.hsl # e.g. (230, 255, 203)
# proportion  = first_color.proportion # e.g. 0.34

# # RGB and HSL are named tuples, so values can be accessed as properties.
# # These all work just as well:
# red = rgb[0]
# red = rgb.r
# saturation = hsl[1]
# saturation = hsl.s