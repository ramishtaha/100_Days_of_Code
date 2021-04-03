import colorgram

colors = colorgram.extract('C:\\Users\\ramis\\Desktop\\100_Days_of_Code_Challange\\DAY_18\\Practice\\spot_painting\\image.jpg', 35)
colors_list = []


for i in range(len(colors)):
    # temp_list = [colors[i].rgb[r]]
    # temp_list += [colors[i].rgb[g]]
    # temp_list += [colors[i].rgb[b]]
    color = colors[i]
    rgb_color = []
    for j in range(3):
        rgb_color.append(color.rgb[j])
    colors_list.append(tuple(rgb_color))

print(colors_list)