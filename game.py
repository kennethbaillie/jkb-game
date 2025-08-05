# sk_platformer.py
import spritekit as sk            # third‐party wrapper
from random import uniform

class Game(sk.Scene):
    def setup(self):
        self.gravity = (0, -9.8)  # m/s2 like Box2D
        ground = sk.BoxNode(size=(600, 40),
                            position=(0, -150),
                            dynamic=False)
        self.add_child(ground)

        # Drop 10 random balls so you can tweak restitution, density, ...
        for _ in range(10):
            ball = sk.CircleNode(radius=20,
                                 position=(uniform(-250, 250), 200))
            ball.restitution = 0.8
            ball.density = 0.5
            self.add_child(ball)

sk.run(Game())
