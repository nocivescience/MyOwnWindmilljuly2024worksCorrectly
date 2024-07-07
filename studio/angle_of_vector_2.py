from manim import *
class VectorsScene(Scene):
    def construct(self):
        vectors=self.add_vectors()
        self.play(vectors.animate.shift(UP))
        self.wait()
    def add_vector(self):
        vector=Arrow(RIGHT)
        return vector
    def add_vectors(self):
        vectors=VGroup()
        for _ in range(2):
            vector=self.add_vector()
            vectors.add(vector)
        vectors.arrange_in_grid(cols=2, rows=1, buff=1)
        return vectors
    
class ArrangeScene(Scene):
    def construct(self):
        dots=VGroup()
        for i in range(1, 5):
            dot=Vector()
            angle=angle_of_vector(dot.get_end()-dot.get_start())
            angle_tracker=ValueTracker(angle)
            dot.add_updater(lambda d: d.set_angle(angle_tracker.get_value()))
            dot.move_to(i*RIGHT)
            dots.add(dot)
        dots.arrange_in_grid(cols=2, rows=2, buff=1)
        self.add(dots)
        self.play(*[angle_tracker.animate.set_value(r*PI/4) for _,r in zip(range(4), np.random.uniform(0, 2, 4))])
        self.wait()

class SecondArrangeVectors(Scene):
    def construct(self):
        vectors=self.add_vectors()
        self.add(vectors)
        self.wait()
    def add_vector(self):
        vector=Vector(RIGHT)
        vector.angle_tracker=ValueTracker(0)
        def updater(v, dt):
            v.rotate(0.5*dt, about_point=v.get_start())
        vector.add_updater(updater)
        return vector
    def add_vectors(self):
        vectors=VGroup()
        for i in range(4):
            vector=self.add_vector()
            vectors.add(vector)
        vectors.arrange_in_grid(cols=2, rows=2, buff=1)
        return vectors