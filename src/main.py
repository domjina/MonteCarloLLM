import random as rnd
import matplotlib.pyplot as plt
from typing import Callable

def generate_movement(
        RANGE_: list[int],
        WEIGHTS: list[float],
        TIMESTAMPS: int
):
    movement = rnd.choices(RANGE_, weights=WEIGHTS, k=TIMESTAMPS)
    return movement


def main(
        movement_generator: Callable[[list[int], list[float], int], list[int]],
        TIMESTAMPS: int,
        NUM_LINES: int,
        RANGE_: list[int],
        WEIGHTS: list[float]
):
    data = [[0] for _ in range(NUM_LINES)]

    for line in range(NUM_LINES):
        movement = movement_generator(RANGE_=RANGE_, 
                                      WEIGHTS=WEIGHTS, 
                                      TIMESTAMPS=TIMESTAMPS
                                      )
        for _ in range(len(movement)):
            data[line].append(data[line][_-1] + movement[_])

    for line in data:
        plt.plot(line)
        plt.pause(0.1)
    plt.show()


if __name__ == "__main__":
    gen = generate_movement
    TIMESTAMPS = 10
    NUM_LINES = 50
    RANGE_ = [x for x in range(-5, 4)]
    WEIGHTS = [0.1, 0.2, 0.3, 0.4, 0.5, 0.4, 0.3, 0.2, 0.1]

    main(
        movement_generator=gen,
        TIMESTAMPS=TIMESTAMPS,
        NUM_LINES=NUM_LINES,
        RANGE_=RANGE_,
        WEIGHTS=WEIGHTS
    )