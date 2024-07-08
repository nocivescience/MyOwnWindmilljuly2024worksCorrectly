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
        current_pivot = [points[0]]
        rotation_speed = 0.5  # Ajusta la velocidad de rotación según sea necesario

        def update_line(line, dt):
            # Rotar la línea alrededor del pivote actual
            line.rotate(dt * PI * rotation_speed, about_point=current_pivot[0])
            # Verificar si la línea cruza el segundo punto
            if np.array_equal(current_pivot[0], points[0]):
                if np.linalg.norm(line.get_center() - points[1]) < 0.1:
                    current_pivot[0] = points[1]
            elif np.array_equal(current_pivot[0], points[1]):
                if np.linalg.norm(line.get_center() - points[0]) < 0.1:
                    current_pivot[0] = points[0]

        line.add_updater(update_line)
        self.wait(10)
        line.remove_updater(update_line)

