# coding: utf-8
# Your code here!

# sympyをインポート
import sympy,cgitb,io,sys,random

#エラー表示
cgitb.enable()

#日本語用
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

#ヘッダー出力
print ("Content-Type: text/html; charset=UTF-8;\n\n")


# 文字を定義
sympy.var('a b c d e')

num = []
n = 0
for i in range(10):
    n = random.randint(0, 10) - 5
    while n == 0:
      n = random.randint(0, 10) - 5
    num.append(n)

#print(num)

efcont = [
          [[num[0]*a], 
           [num[1]*a+num[2]]
          ], 
          [[num[0]*a + num[1]],
           [num[0]*a + num[1]]
          ],
          [[num[0]*a + num[1]],
           [num[0]*a - num[1]]
          ],
          [[num[0]*a + num[1]],
           [num[0]*a + num[2]]
          ],
          [[num[0]*a + num[1]],
           [num[2]*a + num[3]]
          ],
          [[num[0]*a + num[1]],
           [num[2]*b + num[3]]
          ]
        ]

mode = random.randint(0, 5)

# 多項式を定義
f1 = efcont[mode][0]
f2 = efcont[mode][1]

#print(f1, f2)

# 多項式の積
g = f1[0] * f2[0]
ex_g = sympy.expand(g)

#print(ex_g)

ex_gl = list(str(ex_g))

#print(ex_gl)

wex_gl=""
i = 0
for i in range(len(ex_gl)+50):
    try:
        if ex_gl[i] == "*":
            if ex_gl[i+1] == "*":
                ex_gl[i:i+1] = "<sup>"
                ex_gl.insert(i+7, "</sup>")
            else:
                ex_gl[i] = ""
        wex_gl += str(ex_gl[i])
    except:
        break
        

#print(wex_gl)

ex_ga = sympy.factor(ex_g)
ex_gal = list(str(ex_ga))
wex_gal = ""
for i in range(len(ex_gal)+50):
    try:
        if ex_gal[i] == "*":
            if ex_gal[i+1] == "*":
                ex_gal[i:i+1] = "<sup>"
                ex_gal.insert(i+7, "</sup>")
            else:
                ex_gal[i] = ""
        wex_gal += str(ex_gal[i])
    except:
        break
    
#print(wex_gal)



# 置換えデータ作成（サンプル用）
page_data = {}
page_data['qEasy'] = wex_gl 
page_data['aEasy'] = wex_gal 
page_data['qNormal'] = ''
page_data['aNormal'] = ''
page_data['qHard'] = ''
page_data['aHard'] = ''

# template.htmlの読み込み
with open('subpage.html','r') as file:
    html = file.read()
file.closed

# {% %}をpage_dataに置換え
for key, value in page_data.items():
    html = html.replace('{% ' + key + ' %}', value)

#HTML出力
print(html)
