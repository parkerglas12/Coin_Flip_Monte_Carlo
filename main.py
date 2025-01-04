import numpy as np
from numpy.random import PCG64 as pcg
from numpy.random import Generator as gen
import matplotlib.pyplot as plt
import seaborn as sns

def get_user_input() -> int:
    while True:
        try:
            sims: int = int(input("How many coin flips would you like to perform: "))
            if sims <= 1 or sims >= 100000001:
                raise ValueError("Enter an integer between 2 and 100,000,000.")
        except ValueError as e:
            print(f"Error: {e}")
        else:
            return sims    

def get_results(rng, sims: int) -> tuple[int, int]:
    results = rng.integers(0, 2, sims)
    tails: int= np.count_nonzero(results == 0)
    heads: int = sims - tails
    return tails, heads

def print_results(tails: int, heads: int, sims: int) -> None:
    print(f"Of the {sims:,} flips, tails were flipped {tails:,} times, and heads were flipped {heads:,} times.")

def create_bar_chart(tails: int, heads: int, sims: int) -> None:
    sns.set()
    sns.set_style("white")
    plt.figure(figsize=(10, 6))
    bars = plt.bar(["Tails", "Heads"], [tails, heads], color="#0081cf")
    plt.xlabel("Outcome", fontsize=14, weight="bold", labelpad=10)
    plt.xticks(fontsize=12, weight="bold")
    plt.ylabel("Count",  fontsize=14, weight="bold", labelpad=15)
    plt.title(f"Monte Carlo Simulation of {sims:,} Coin Flips",  fontsize=14, weight="bold", pad=15)
    
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval, f"{yval:,}", ha="center", va="bottom", fontsize=12, weight="bold")

    sns.despine()
    plt.tight_layout(pad=1)
    plt.show()

def main() -> None:
    rng = gen(pcg()) # Random number generator
    sims: int = get_user_input()
    tails, heads = get_results(rng, sims)
    print_results(tails, heads, sims)
    create_bar_chart(tails, heads, sims)

if __name__ == "__main__":
    main()