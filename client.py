"""Two-Player Bimatrix Nash Equilibrium Solver.
100% Python Standard Library.
"""

class NashEquilibriumSolver:
    """Computes pure and mixed-strategy Nash equilibria for 2x2 normal-form bimatrix games."""
    @staticmethod
    def solve_2x2(payoff_A, payoff_B):
        a11, a12 = payoff_A[0]
        a21, a22 = payoff_A[1]
        b11, b12 = payoff_B[0]
        b21, b22 = payoff_B[1]
        
        denom_q = (a11 - a12 - a21 + a22)
        q = (a22 - a12) / denom_q if abs(denom_q) > 1e-9 else None
        
        denom_p = (b11 - b21 - b12 + b22)
        p = (b22 - b21) / denom_p if abs(denom_p) > 1e-9 else None
        
        mixed = None
        if p is not None and q is not None and 0.0 <= p <= 1.0 and 0.0 <= q <= 1.0:
            mixed = {
                "row_strategy": [round(p, 4), round(1.0 - p, 4)],
                "col_strategy": [round(q, 4), round(1.0 - q, 4)]
            }
            
        pure = []
        for i in range(2):
            for j in range(2):
                row_br = payoff_A[i][j] >= payoff_A[1 - i][j]
                col_br = payoff_B[i][j] >= payoff_B[i][1 - j]
                if row_br and col_br:
                    pure.append((i, j))
                    
        return {"pure_equilibria": pure, "mixed_equilibrium": mixed}
