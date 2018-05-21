class Bus:
    def __init__(self, width, height):
        self.mapWidth = width
        self.mapHeight = height
        self.origin = PVector(0, 0)
        self.position = PVector(self.origin.x, self.origin.y)
        self.destination = PVector(width, height)
        self.velocity = PVector(self.destination.x, self.destination.y)
        self.velocity.sub(self.origin)
        self.velocity.normalize()
        
    def draw(self):
        strokeWeight(1)
        stroke(0)
        line(self.origin.x, self.origin.y, self.destination.x, self.destination.y)
        pushMatrix();
        translate(self.position.x, self.position.y)
        rotate(atan2(self.velocity.y, self.velocity.x))
        busHeight = 20
        busWidth = 65
        fill(255, 255, 255)
        rect(-busWidth/2, -busHeight/2.0, 65, busHeight)
        stroke(255, 0, 0)
        strokeWeight(5)
        point(0, 0)
        popMatrix();
        # update
        self.position.add(self.velocity)
