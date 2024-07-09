from manim import *

class Windmill2Points(Scene):
    def construct(self):
        points = [3 * LEFT, 3 * RIGHT, 3 * UP+ 2 * RIGHT, DOWN+LEFT]
        dots = VGroup(*[Dot(p) for p in points])
        self.add_foreground_mobjects(dots)
        
        self.integers=VGroup()
        for point in points:
            integer=Integer(0)
            integer.next_to(point,UP)
            self.integers.add(integer)

        line = Line(config["frame_width"] * LEFT, config["frame_width"] * RIGHT)
        line.set_color(RED)
        line.rotate(PI / 4)
        line.move_to(points[0])
        self.add(dots, line, self.integers)

        # Estado inicial
        self.current_pivot = points[0]

        def update_line(line, dt):
            # Rotar la línea alrededor del pivote actual
            line.rotate(dt * PI / 2, about_point=self.current_pivot)

            # Recalcular las diferencias de ángulo en cada frame
            angle_0 = angle_of_vector(points[0] - line.get_center())
            angle_1 = angle_of_vector(points[1] - line.get_center())
            angle_2 = angle_of_vector(points[2] - line.get_center())
            angle_3 = angle_of_vector(points[3] - line.get_center())
            diff_angle_0 = np.abs(angle_0 - line.get_angle())
            diff_angle_1 = np.abs(angle_1 - line.get_angle())
            diff_angle_2 =np.abs(angle_2-line.get_angle())
            diff_angle_3 = np.abs(angle_3-line.get_angle())
            if diff_angle_0 < 0.1:
                self.current_pivot = points[0]
                line.move_to(points[0])
                self.integers[0].increment_value()
            elif diff_angle_1 < 0.1:
                self.current_pivot = points[1]
                line.move_to(points[1])
                self.integers[1].increment_value()
            elif diff_angle_2 <.1:
                self.current_pivot = points[2]
                line.move_to(points[2])
                self.integers[2].increment_value()
            elif diff_angle_3 <.1:
                self.current_pivot = points[3]
                line.move_to(points[3])
                self.integers[3].increment_value()
            
        line.add_updater(update_line)
        self.wait(30)
        line.remove_updater(update_line)
