# -*- coding: utf-8 -*-
from svg_turtle import SvgTurtle
import math

def draw_square(t, size, color):
    t.penup()
    t.fillcolor(color)
    t.begin_fill() 
    for _ in range(4):
        t.forward(size)
        t.right(90)
    t.end_fill()
        
def draw_pythagoras_tree(t, size, depth, color):
    if depth == 0:
        return

    draw_square(t, size, color[depth-1])
    t.forward(size)

    # compute sizes of next squares facing different angles
    next_size_30 = size / 2
    next_size_60 = size * math.sqrt(3) / 2

    # draw left branch (60° rotation for 30-90-60 triangle)
    t.left(30)
    draw_pythagoras_tree(t, next_size_60, depth - 1, color)
    t.right(30)

    # draw right branch (30° rotation for 30-90-60 triangle)
    t.right(60)
    t.forward(next_size_60)
    draw_pythagoras_tree(t, next_size_30, depth - 1, color)
    t.backward(next_size_60)
    t.left(60)

    t.backward(size)

def mytree(t, depth=5, color="#ffffff"):
    t.penup()
    t.goto(-250, -250)
    t.pendown()
    draw_pythagoras_tree(t, 100, depth, color)

def write_file(draw_func, filename, width , height):
    t = SvgTurtle(width, height)
    draw_func(t)
    t.save_as(filename)

def main():
    color = ["#f9e5bf", "#03180e", "#930f0e", "#e65653", "#f3a041", "#e65653", "#f3a041", "#62a916"]
    outpath = "test.svg"
    depth = 7
    write_file(lambda t: mytree(t, depth, color), outpath, 500, 500)
    print("[pythago.py] Done.")

if __name__ == '__main__':
    main()