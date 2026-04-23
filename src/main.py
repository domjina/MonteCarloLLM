import random as rnd
import math
import itertools
import matplotlib.pyplot as plt
from typing import Protocol, Sequence
from dataclasses import dataclass

@dataclass(frozen=True)
class SimulationConfig:
    num_timestamps: int
    num_lines: int
    sigma: float
    mean: int

class MovementGenerator(Protocol):
    def __call__(
            self, 
            sigma: float,
            mean: int,
            num_movements: int
        ) -> Sequence[float]: ...

def generate_movement(
        sigma: float,
        mean: int,
        num_movements: int
) -> list[float]:
    return [rnd.gauss(mu=mean, sigma=sigma) for _ in range(num_movements)]

def main(
        config: SimulationConfig,
        generator: MovementGenerator
) -> None:
    walks = []
    for _ in range(config.num_lines):
        moves = generator(
            config.sigma, 
            config.mean, 
            config.num_timestamps
        )
        walk = list(itertools.accumulate(moves, initial=0))
        walks.append(walk)
    
    for walk in walks:
        plt.plot(walk)
    plt.show()

if __name__ == "__main__":
    config = SimulationConfig(
        num_timestamps=10,
        num_lines=5000,
        sigma=1.5,
        mean=0
    )

    main(config, generate_movement)