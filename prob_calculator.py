import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
      allcontents = dict()
      self.contents = list()
      if len(kwargs.keys()) < 1:
        allcontents = {"default_colour": 1}
      for varname, value in kwargs.items():
        allcontents[varname] = value
      for varname, value in allcontents.items():
        self.contents.extend([varname]*value)

    def draw(self, numdraw):
      numdraw = min(numdraw, len(self.contents))
      ballsdrawn = random.sample(self.contents, numdraw)
      for x in ballsdrawn:
        self.contents.remove(x)
      return ballsdrawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  gooddraws = 0
  orig_hat = copy.deepcopy(hat)
  expctkeys = expected_balls.keys()
  for i in range(num_experiments):
    hat = copy.deepcopy(orig_hat)
    ballsdrawn = hat.draw(num_balls_drawn)
    drawndict = {b:ballsdrawn.count(b) for b in ballsdrawn}
    drawnkeys = drawndict.keys()
    if not all (m in drawnkeys for m in expctkeys):
      continue
    isahit = 1.0
    for k in expctkeys:
      if drawndict[k] >= expected_balls[k]:
        is_k_hit = 1
      else:
        is_k_hit = 0
      isahit = isahit * is_k_hit
    gooddraws = gooddraws + isahit
  return (gooddraws/num_experiments)