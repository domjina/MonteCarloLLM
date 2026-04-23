import random as rnd
import itertools
import matplotlib.pyplot as plt
from typing import Protocol, Sequence
from dataclasses import dataclass

@dataclass(frozen=True)
class SimulationConfig:
    num_timestamps: int
    num_lines: int
    range_vals: Sequence[int]
    weights: Sequence[float]

class MovementGenerator(Protocol):
    def __call__(
            self, 
            range_vals: Sequence[int],
            weights: Sequence[float],
            k: int
        ) -> Sequence[int]: ...

def generate_movement(
        range_vals: Sequence[int],
        weights: Sequence[float],
        k: int
) -> list[int]:
    return rnd.choices(range_vals, weights=weights, k=k)

def main(
        config: SimulationConfig,
        generator: MovementGenerator
) -> None:
    walks = []
    for _ in range(config.num_lines):
        moves = generator(
            config.range_vals, 
            config.weights, 
            config.num_timestamps
        )
        walk = list(itertools.accumulate(moves, initial=0))
        walks.append(walk)
    
    for walk in walks:
        plt.plot(walk)
        plt.pause(0.01)
    plt.show()

if __name__ == "__main__":
    config = SimulationConfig(
        num_timestamps=10,
        num_lines=50,
        range_vals=list(range(-5,4)),
        weights=[0.1, 0.2, 0.3, 0.4, 0.5, 0.4, 0.3, 0.2, 0.1]
    )

    main(config, generate_movement)