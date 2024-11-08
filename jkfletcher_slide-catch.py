"""Slide and Catch game
    Rocket avoids meteors"""

import random, pygame, simpleGE

class Instructions(simpleGE.Scene):
    def __init__(self, time):
        super().__init__()
        self.setImage("OGA-Background-1.png")
        
        self.response = "Play"
        
        self.instructions = simpleGE.MultiLabel()
        self.instructions.textLines = [
            "Avoid the meteors!",
            "Use the left and right arrows to move.",
            "You have 3 lives."
            ]
        self.instructions.center = (320, 240)
        self.instructions.size = (500, 250)
        
        self.btnPlay = simpleGE.Button()
        self.btnPlay.text = "Play"
        self.btnPlay.center = (100, 400)
        
        self.prevTime = time
        self.prevTime = simpleGE.Label()
        self.prevTime.text = f"Previous Time: {time:.2f}"
        self.prevTime.size = (250, 30)
        self.prevTime.center = (320, 400)
        
        self.btnQuit = simpleGE.Button()
        self.btnQuit.text = "Quit"
        self.btnQuit.center = (550, 400)
        
        self.sprites = [self.instructions, self.prevTime, self.btnPlay, self.btnQuit]
        
    def process(self):
        if self.btnQuit.clicked:
            self.response = "Quit"
            self.stop()
        if self.btnPlay.clicked:
            self.response = "Play"
            self.stop()


class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("OGA-Background-1.png")
        
        self.timer = simpleGE.Timer()
        self.time = 0
        
        self.lives = 3
        
        self.sndHit = simpleGE.Sound("sfx_explosionNormal.ogg")
        
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
                self.sndHit.play()
                self.lives -= 1
                self.lblLives.text = f"Lives: {self.lives}"
                
        self.lblTime.text = f"Time: {self.timer.getElapsedTime():.2f}"
                
        if self.lives == 0:
            self.stop()
            self.time = self.timer.getElapsedTime()
            print(self.time)

        
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
    keepGoing = True
    time = 0
    while keepGoing:
        
        instructions = Instructions(time)
        instructions.start()
        
        if instructions.response == "Play":
            game = Game()
            game.start()
            time = game.time
        if instructions.response == "Quit":
            keepGoing = False
            exit()
            
    
if __name__ == "__main__":
    main()