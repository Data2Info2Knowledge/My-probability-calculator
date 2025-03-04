# This entrypoint file to be used in development. Start by reading README.md
import prob_calculator
from unittest import main
import copy

prob_calculator.random.seed(95)

hat = prob_calculator.Hat(black=6, red=4, green=3)
print(hat.contents)

probability = prob_calculator.experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)
print(probability)

# Run unit tests automatically
main(module='test_module', exit=False)
