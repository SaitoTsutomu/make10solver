import itertools
import math
import operator

import fire


def solve_make10(num1: int, num2: int, num3: int, num4: int, *, target: int = 10) -> str:  # noqa: C901
    """4つの数字を使って10を作る式を探す関数"""
    epsilon = 1e-6  # 浮動小数点比較のための許容誤差
    # 演算子の定義
    ops = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,  # 浮動小数点除算
    }
    op_symbols = [*ops]

    # 1. 数字のすべての順列を生成 (重複する数字があっても対応)
    num_permutations = set(itertools.permutations([num1, num2, num3, num4]))

    # 2. 演算子のすべての組み合わせを生成 (3つの演算子)
    op_combinations = [*itertools.product(op_symbols, repeat=3)]

    for p in num_permutations:
        n1, n2, n3, n4 = p

        for op1_sym, op2_sym, op3_sym in op_combinations:
            op1 = ops[op1_sym]
            op2 = ops[op2_sym]
            op3 = ops[op3_sym]

            # 3. 括弧の付け方(計算順序)を試す
            # (パターン1) (n1 op1 n2) op2 (n3 op3 n4)
            try:
                val1 = op1(n1, n2)
                val2 = op3(n3, n4)
                result = op2(val1, val2)
                if math.isclose(result, target, abs_tol=epsilon):
                    return f"({n1} {op1_sym} {n2}) {op2_sym} ({n3} {op3_sym} {n4})"
            except ZeroDivisionError:
                pass

            # (パターン2) ((n1 op1 n2) op2 n3) op3 n4
            try:
                val1 = op1(n1, n2)
                val2 = op2(val1, n3)
                result = op3(val2, n4)
                if math.isclose(result, target, abs_tol=epsilon):
                    return f"(({n1} {op1_sym} {n2}) {op2_sym} {n3}) {op3_sym} {n4}"
            except ZeroDivisionError:
                pass

            # (パターン3) (n1 op1 (n2 op2 n3)) op3 n4
            try:
                val1 = op2(n2, n3)
                val2 = op1(n1, val1)
                result = op3(val2, n4)
                if math.isclose(result, target, abs_tol=epsilon):
                    return f"({n1} {op1_sym} ({n2} {op2_sym} {n3})) {op3_sym} {n4}"
            except ZeroDivisionError:
                pass

            # (パターン4) n1 op1 ((n2 op2 n3) op3 n4)
            try:
                val1 = op2(n2, n3)
                val2 = op3(val1, n4)
                result = op1(n1, val2)
                if math.isclose(result, target, abs_tol=epsilon):
                    return f"{n1} {op1_sym} (({n2} {op2_sym} {n3}) {op3_sym} {n4})"
            except ZeroDivisionError:
                pass

            # (パターン5) n1 op1 (n2 op2 (n3 op3 n4))
            try:
                val1 = op3(n3, n4)
                val2 = op2(n2, val1)
                result = op1(n1, val2)
                if math.isclose(result, target, abs_tol=epsilon):
                    return f"{n1} {op1_sym} ({n2} {op2_sym} ({n3} {op3_sym} {n4}))"
            except ZeroDivisionError:
                pass
    return ""


def main() -> None:
    """CLI用"""
    fire.Fire(solve_make10)
