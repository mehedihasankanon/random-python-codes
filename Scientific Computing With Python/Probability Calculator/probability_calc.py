import copy
import random

class Hat:
    def __init__(self,**kwargs):
        self.contents = [];
        for key, times in kwargs.items():
            for _ in range(times):
                self.contents.append(key)

    def draw(self,num):
        cont = self.contents
            
        if num > len(self.contents):
            num = len(self.contents)
        
        ret = []
        for _ in range(num):
            x = random.randint(0,len(cont) - 1) 
            ret.append(cont.pop(x))

        return ret

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    fnd = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        temp_exp = copy.deepcopy(expected_balls)
        temp = hat_copy.draw(num_balls_drawn)
        fl = True
        for ball in temp:
            if ball in temp_exp:
                temp_exp[ball] -= 1
        
        if all(val <= 0 for val in temp_exp.values()):
            fnd += 1
    return fnd / num_experiments
