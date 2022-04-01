# sympyをインポート
import sympy

# 文字を定義
sympy.var('a b')

# 多項式を定義
f1 = a + 5 * b + 2
f2 = a + 2 * b + 5

# 多項式の積
g = f1 * f2

print(g)
