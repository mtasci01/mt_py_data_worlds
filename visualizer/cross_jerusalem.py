import matplotlib.pyplot as plt

def draw_cross(line_list, center, length):
    x1 = [center[0] - length, center[0] + length]
    y1 = [center[1], center[1]]
    x2 = [center[0], center[0]]
    y2 = [center[1] + length, center[1] - length]
    line_list.append([x1, y1])
    line_list.append([x2, y2])

all_lines = []

main_center = [50,50]
main_cross_length = 10
smaller_cross_length = 2
radius = main_cross_length + 2

draw_cross(all_lines,main_center,main_cross_length)

curr_center = [main_center[0] - main_cross_length/2, main_center[1] + main_cross_length/2]
draw_cross(all_lines,curr_center,smaller_cross_length)

curr_center = [main_center[0] + main_cross_length/2, main_center[1] + main_cross_length/2]
draw_cross(all_lines,curr_center,smaller_cross_length)

curr_center = [main_center[0] - main_cross_length/2, main_center[1] - main_cross_length/2]
draw_cross(all_lines,curr_center,smaller_cross_length)

curr_center = [main_center[0] + main_cross_length/2, main_center[1] - main_cross_length/2]
draw_cross(all_lines,curr_center,smaller_cross_length)


for line in all_lines:
    plt.plot(line[0], line[1], marker = 'o')

circle=plt.Circle(main_center,radius,facecolor='white',edgecolor='blue')
plt.gca().add_patch(circle)

plt.show()