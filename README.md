# Nash Equilibrium Bimatrix Solver Skill

Exact solver computing pure and mixed-strategy Nash equilibria in 2-player strategic normal form games.

```mermaid
flowchart TD
    Payoff["Bimatrix Payoffs (A, B)"] --> BestResponse["Check Pure Best-Response Crossings"]
    Payoff --> Indifference["Solve Marginal Indifference Equation System"]
    BestResponse --> PureEq["Pure Nash Equilibria List"]
    Indifference --> MixedEq["Mixed Strategy Vector (p, 1-p) & (q, 1-q)"]
```

## Features
- **100% Python Standard Library**: Analytical solving of linear indifference equations.
- **Pure & Mixed Detection**: Simultaneously returns all pure saddle points and mixed solutions.
- **MCP Server Ready**: Direct stdio integration for multi-agent game orchestration.
