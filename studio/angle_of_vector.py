from manim import *

class VectorArrayScene(Scene):
    def construct(self):
        vectors = self.add_vector_array()
        self.wait()
    
    def add_vector(self, value, frequency):
        vector = Vector(RIGHT)
        vector.angle_tracker = ValueTracker(0)
        
        def updater(v, dt):
            v.rotate(frequency * dt, about_point=v.get_start())
        
        vector.add_updater(updater)
        return vector
    
    def add_vector_array(self):
        vectors = VGroup()
        frequencies = [0.5, 1.0, 1.5, 2.0]  # Different frequencies for each vector

        for i, frequency in enumerate(frequencies):
            value = i * PI / 4
            vector = self.add_vector(value, frequency)
            vectors.add(vector)

        vectors.arrange_in_grid(cols=2, rows=2, buff=1)
        return vectors

class VectorRotationScene(VectorArrayScene):
    def construct(self):
        vectors = self.add_vector_array()
        self.add(vectors)
        self.wait(4)  # Wait to observe the rotation

if __name__ == "__main__":
    scene = VectorRotationScene()
    scene.render()
