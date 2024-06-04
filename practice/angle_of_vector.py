from manim import *
class VectorsScene(Scene):
    def construct(self):
        self.add_vectors()
    def add_vector(self, value):
        vector=Vector(RIGHT)
        angle=angle_of_vector(vector.get_end()-vector.get_start())
        angle_tracker=ValueTracker(angle)
        vector.add_updater(lambda v: v.set_angle(angle_tracker.get_value()))
        self.add(vector)
        self.play(angle_tracker.animate.set_value(value))
        return vector
    def add_vectors(self):
        rotation=[i for i in np.random.uniform(0,TAU, 2)]
        vectors=VGroup().arrange_in_grid(cols=2, rows=1, buff=1)
        for i in rotation:
            vector=self.add_vector(i)
            vectors.add(vector)
        vectors
        self.wait()

class VectorArrayScene(Scene):
    def construct(self):
        vectors=self.add_vector_array()
        self.play(vectors.animate.shift(UP))
        self.wait()
    def add_vector(self, value):
        vector=Vector(RIGHT)
        return vector
    def add_vector_array(self):
        vectors=VGroup()
        for i in range(4):
            vector=self.add_vector(i*PI/4)
            vectors.add(vector)
        vectors.arrange_in_grid(cols=2, rows=2, buff=1)
        return vectors