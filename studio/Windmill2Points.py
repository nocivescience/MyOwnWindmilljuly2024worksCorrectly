from manim import *
import numpy as np
class Windmill2Points(Scene):
    def construct(self):
        points=[3*LEFT,3*RIGHT]
        dots = VGroup(*[Dot(p) for p in points])
        self.add_foreground_mobjects(dots)
        line = Line(config['frame_width']*LEFT,config['frame_width']*RIGHT)
        line.set_color(RED)
        line.rotate(PI/4)
        line.move_to(points[0])
        self.add(dots,line)
        self.wait()