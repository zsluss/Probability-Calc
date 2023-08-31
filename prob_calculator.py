import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **allitem):
        self.name= self
        self.contents = []
        for key,value in allitem.items():
            for item in range(value):
                self.contents.append(key)
    def draw(self,pulls):
        ballstopull = pulls
        pulledList = []
        while(ballstopull > 0 and len(self.contents) > 0):
            pulled = random.choice(self.contents)
            self.contents.remove(pulled)
            pulledList.append(pulled)
            ballstopull = ballstopull - 1
        return pulledList





def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    correct = 0
    for unk in range(0,num_experiments):
        copyhat = copy.deepcopy(hat)
        value = copyhat.draw(num_balls_drawn)
        truth = True
        value = {ball: value.count(ball) for ball in set(value)}
        for k,v in expected_balls.items():
            if k not in value or value[k] < expected_balls[k]:
                truth = False
                break
        if truth is  True:
                correct = correct + 1
    return correct/num_experiments
        

