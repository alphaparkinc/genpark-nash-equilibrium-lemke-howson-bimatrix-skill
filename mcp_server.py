"""MCP stdio server for Nash Equilibrium Solver."""
import sys
import json

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import NashEquilibriumSolver

def handle_rpc(request):
    req_id = request.get("id")
    method = request.get("method")
    params = request.get("params", {})

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "solve_nash_equilibrium",
                        "description": "Compute pure and mixed Nash equilibria for 2x2 bimatrix game",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "payoff_A": {"type": "array", "items": {"type": "array", "items": {"type": "number"}}, "minItems": 2, "maxItems": 2},
                                "payoff_B": {"type": "array", "items": {"type": "array", "items": {"type": "number"}}, "minItems": 2, "maxItems": 2}
                            },
                            "required": ["payoff_A", "payoff_B"]
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})
        if name == "solve_nash_equilibrium":
            A = args.get("payoff_A", [])
            B = args.get("payoff_B", [])
            res = NashEquilibriumSolver.solve_2x2(A, B)
            return {"jsonrpc": "2.0", "id": req_id, "result": res}
        return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": f"Method {name} not found"}}
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32600, "message": "Invalid request"}}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_rpc(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()
        except Exception as e:
            sys.stdout.write(json.dumps({"jsonrpc": "2.0", "error": {"code": -32700, "message": str(e)}}) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
