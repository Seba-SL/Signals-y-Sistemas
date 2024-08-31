from manim import *

class SimpleScene(Scene):
    def construct(self):
        # Crear un cuadrado
        square = Square()

        # Mostrar el cuadrado en la pantalla
        self.play(Create(square))

        # Esperar un segundo antes de finalizar la animación
        self.wait(1)

