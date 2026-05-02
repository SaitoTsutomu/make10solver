import pytest

from make10solver.solver import solve_make10


@pytest.mark.parametrize(
    ("a", "b", "c", "d", "expected"),
    [
        (1, 1, 1, 1, ""),
        (1, 3, 4, 6, "((6 * (1 + 4)) / 3)"),
        (1, 1, 9, 9, "(((1 / 9) + 1) * 9)"),
    ],
)
def test_solve_make10(a: int, b: int, c: int, d: int, expected: str) -> None:
    """solve_make10のテスト"""
    # Act
    expr = solve_make10(a, b, c, d)

    # Assert
    assert expr == expected
