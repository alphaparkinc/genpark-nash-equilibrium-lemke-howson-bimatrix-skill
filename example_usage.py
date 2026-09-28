"""Example solving Matching Pennies Nash equilibrium."""
from client import NashEquilibriumSolver

def main():
    payoff_A = [[1, -1], [-1, 1]]
    payoff_B = [[-1, 1], [1, -1]]
    sol = NashEquilibriumSolver.solve_2x2(payoff_A, payoff_B)
    print("Matching Pennies Analysis:")
    print("  Pure Equilibria:", sol["pure_equilibria"])
    print("  Mixed Equilibrium:", sol["mixed_equilibrium"])

if __name__ == "__main__":
    main()
