"""Slide and Catch game
    Rocket avoids meteors"""

import random, pygame, simpleGE

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("OGA-Background-1.png")
        
        self.rocket = Rocket(self)
        self.meteor = Meteor(self)
        
        self.sprites = [self.rocket, self.meteor]

    def process(self):
        if self.meteor.collidesWith(self.rocket):
            self.meteor.reset()

        
class Rocket(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("ship_recolor_001.png")
        self.setSize(75, 75)
        self.position = (320, 420)
        self.moveSpeed = 5
        
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed


class Meteor(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Asteroid2.png")
        self.setSize(50, 50)
        self.reset()
        
    def reset(self):
        self.y = 10
        self.x = random.randint(0, self.screenWidth)
        self.dy = random.randint(3, 8)

    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()
            
            
def main():
    game = Game()
    game.start()
    
    
if __name__ == "__main__":
    main()