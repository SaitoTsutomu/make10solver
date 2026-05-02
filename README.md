# make10solver

Given four integers as input, this tool finds an expression that makes 10 using the four basic arithmetic operations and parentheses.

## Usage

```bash
uv run make10 1 2 3 4
```

If no solution exists, it outputs nothing.

To change the target value:

```bash
uv run make10 1 2 3 4 --target 24
```
