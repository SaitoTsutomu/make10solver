import math
import operator
from itertools import permutations, product

import fire


def solve_make10(num1: int, num2: int, num3: int, num4: int, *, target: int = 10) -> str:
    """逆ポーランド記法(RPN)版"""
    epsilon = 1e-6
    ops = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,  # 浮動小数点除算
    }
    structures = [  # n: 数字, o: 演算子
        ["n", "n", "o", "n", "o", "n", "o"],
        ["n", "n", "o", "n", "n", "o", "o"],
        ["n", "n", "n", "o", "o", "n", "o"],
        ["n", "n", "n", "o", "n", "o", "o"],
        ["n", "n", "n", "n", "o", "o", "o"],
    ]

    for nums in set(permutations([num1, num2, num3, num4])):  # ruff: ignore[too-many-nested-blocks]
        for op_keys in product(ops.keys(), repeat=3):
            for struct in structures:
                stack = []
                n_idx, o_idx = 0, 0

                try:  # ruff: ignore[too-many-statements-in-try-clause]
                    for s in struct:
                        if s == "n":
                            val = float(nums[n_idx])
                            stack.append((val, str(nums[n_idx])))
                            n_idx += 1
                        else:
                            val_b, expr_b = stack.pop()
                            val_a, expr_a = stack.pop()

                            op_char = op_keys[o_idx]
                            res_val = ops[op_char](val_a, val_b)

                            stack.append((res_val, f"({expr_a} {op_char} {expr_b})"))
                            o_idx += 1

                    final_val, final_expr = stack[0]
                    if math.isclose(final_val, target, abs_tol=epsilon):
                        return final_expr

                except ZeroDivisionError:
                    continue
    return ""


def main() -> None:
    """CLI用"""
    fire.Fire(solve_make10)
