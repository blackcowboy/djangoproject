import turtle

# 创建画布并设置大小
canvas = turtle.Screen()
canvas.setup(width=800, height=600)

# 创建海龟对象
heart_turtle = turtle.Turtle()


# 定义函数来绘制心形
def draw_heart():
    heart_turtle.penup()
    heart_turtle.goto(-150, -200)  # 移动到起始位置

    heart_turtle.pendown()
    heart_turtle.fillcolor("red")  # 设置填充色为红色
    heart_turtle.begin_fill()  # 开始填充图形

    for _ in range(2):
        heart_turtle.forward(300)  # 前进300像素

        heart_turtle.right(90)  # 右转90度
        heart_turtle.circle(-150, 270)  # 左侧曲线

        heart_turtle.left(140)  # 左转140度
        heart_turtle.circle(-150, 270)  # 右侧曲线

        heart_turtle.setheading(0)  # 将朝向重新调整为正北

    heart_turtle.end_fill()  # 结束填充图形


draw_heart()  # 调用函数绘制心形

# 关闭画布
canvas.exitonclick()