from manim import *

class Windmill2Points(Scene):
    def construct(self):
        points = [3 * LEFT, 3 * RIGHT]
        dots = VGroup(*[Dot(p) for p in points])
        self.add_foreground_mobjects(dots)

        line = Line(config["frame_width"] * LEFT, config["frame_width"] * RIGHT)
        line.set_color(RED)
        line.rotate(PI / 4)
        line.move_to(points[0])
        self.add(dots, line)

        # Estado inicial
        self.current_pivot = points[0]

        self.time = 0
        self.diff_angle_0= np.abs(angle_of_vector(points[0])-line.get_angle())
        self.diff_angle_1= np.abs(angle_of_vector(points[1])-line.get_angle())
        
        print('diff_angle_0: ', self.diff_angle_0)
        print('diff_angle_1: ', self.diff_angle_1)
        
        def update_line(line, dt):
            # Rotar la línea alrededor del pivote actual
            self.time += dt
            print(self.time*10)
            if self.diff_angle_0 < 0.1:
                self.current_pivot=points[0]
            elif self.diff_angle_1 < 0.1:
                self.current_pivot=points[1]
            # if (self.time)*10 % 2 == 0:
            #     self.current_pivot=points[1]
            # elif (self.time)*10 % 2 == 1:
            #     self.current_pivot=points[0]
            line.rotate(dt * PI / 2, about_point=self.current_pivot)
            line.move_to(self.current_pivot)

        line.add_updater(update_line)
        self.wait(10)
        line.remove_updater(update_line)
