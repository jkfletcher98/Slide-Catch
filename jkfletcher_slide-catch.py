"""Slide and Catch game
    Rocket avoids meteors"""

import random, pygame, simpleGE

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("OGA-Background-1.png")
        
        self.timer = simpleGE.Timer()
        
        self.lives = 3
        
        self.rocket = Rocket(self)
        self.numMeteors = 8
        self.meteors = []
        for i in range(self.numMeteors):
            self.meteors.append(Meteor(self))
            
        self.lblTime = lblTime()
        
        self.lblLives = lblLives()
        
        self.sprites = [self.rocket, self.meteors, self.lblTime, self.lblLives]
        
    def process(self):
        for meteor in self.meteors:
            if self.rocket.collidesWith(meteor):
                meteor.reset()

        
class Rocket(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("ship_recolor_001.png")
        self.setSize(75, 75)
        self.position = (320, 400)
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
        self.setSize(48, 48)
        self.reset()
        
    def reset(self):
        self.y = 10
        self.x = random.randint(0, self.screenWidth)
        self.dy = random.randint(3, 8)

    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()
            
            
class lblTime(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Time: 0"
        self.center = (540, 30)
        
        
class lblLives(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Lives: 3"
        self.center = (95, 30)
            
            
def main():
    game = Game()
    game.start()
    
    
if __name__ == "__main__":
    main()