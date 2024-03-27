from random import choice

class RandomWalk():

    def __init__(self, num_points=5000) -> None:
        self.num_points = num_points

        self.x_values = [0]
        self.y_values = [0]
        self.color = [0]

    def fill_walk(self):
        i=0
        color = choice([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1])
        while i < self.num_points:
            x_direction = choice([1,-1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction * x_distance

            y_direction = choice([1,-1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction * y_distance

            if x_step == 0 and y_step == 0:
                continue

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
            self.color.append(color)
            i+=1