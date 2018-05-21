STARTING_HEIGHT = 5000
PARACHUTING_HEIGHT = 1000

class Player:
    def __init__(self, target, bus):
        global STARTING_HEIGHT
        global PARACHUTING_HEIGHT
        self.position = PVector(0, 0, STARTING_HEIGHT)
        self.state = 0 # 0 means in bus, 1 means skydiving, 2 means parachuting, 3 means reached destination... enums? :(
        self.velocity = PVector(1, 1)
        self.fillColor = color(random(0, 255), random(0, 255), random(0, 255))
        self.occupiedBus = bus
        self.endGoal = target
        self.reachedGoal = False
    
    def draw(self):
        tri_size = 15
        pushMatrix();
        translate(self.position.x, self.position.y)
        rotate(atan2(self.velocity.y, self.velocity.x) - HALF_PI)
        fill(self.fillColor)
        strokeWeight(1)
        stroke(0)
        triangle(0, tri_size/2.5, tri_size/3.0, -tri_size/2, -tri_size/3.0, -tri_size/2)
        popMatrix()
        line(self.position.x, self.position.y, self.endGoal.x, self.endGoal.y)
            
    def update(self):
        if self.state == 0:
            self.position.x = self.occupiedBus.position.x
            self.position.y = self.occupiedBus.position.y
        elif self.state == 1:
            self.computeSkyDivingVelocity()
            # self.clampVelocity();
            self.position.add(self.velocity)
        elif self.state == 2:
            self.computeParachutingVelocity()
            # self.clampVelocity();
            self.position.add(self.velocity)
        
        distanceToTarget = dist(self.position.x, self.position.y, self.endGoal.x, self.endGoal.y)
        text(distanceToTarget, 12, 12)
        
        if self.state == 0 and self.shouldJumpFromBus():
            self.state = 1
            
        if self.state == 1 and self.position.z < PARACHUTING_HEIGHT:
            self.state = 2
            
        if self.state == 2 and distanceToTarget < 5:
            self.state = 3
            self.reachedGoal = True
        
    def clampVelocity(self):
        pass
    
    def shouldJumpFromBus(self):
        distanceToTarget = dist(self.position.x, self.position.y, self.endGoal.x, self.endGoal.y)
        return distanceToTarget < 230
            
    def computeSkyDivingVelocity(self):
        vecToTarget = PVector(self.endGoal.x, self.endGoal.y)
        vecToTarget.sub(self.position)
        vecToTarget.normalize()
        self.velocity.x = vecToTarget.x
        self.velocity.y = vecToTarget.y
        
    def computeParachutingVelocity(self):
        vecToTarget = PVector(self.endGoal.x, self.endGoal.y)
        vecToTarget.sub(self.position)
        vecToTarget.normalize()
        self.velocity.x = vecToTarget.x
        self.velocity.y = vecToTarget.y
