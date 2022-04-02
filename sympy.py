# sympyをインポート
import sympy, cgitb,io,sys

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
for(int i = 0; i < 10; i++)
    n = random.randint(0, 10) - 5
    while n != 0:
      n = random.randint(0, 10) - 5
    num.append(n)

efcont = [
          [[num[0]], 
           [num[1]*a+num[2]]
          ],
          [[a], 
           [num[0]*a+num[1]]
          ], 
          [[num[0]*a + num[1]],
           [num[0]*a + num[1]]
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

# 多項式の積
g = f1 * f2
ex_g = sympy.expand(g)

# 置換えデータ作成（サンプル用）
page_data = {}
page_data['qEasy'] = ex_g
page_data['aEasy'] = sympy.factor(ex_g)
page_data['qNormal'] = '<h1>ONE NOTES</h1>'
page_data['aNormal'] = '<h2>'+ page_data['page_title'] +'</h2><p>Pythonを使って作成したサンプルページです</p>'
page_data['qHard'] = '<p>サイドバー</p>'
page_data['aHard'] = '<p>フッター</p>'

# template.htmlの読み込み
with open('subpage.html','r') as file:
    html = file.read()
file.closed

# {% %}をpage_dataに置換え
for key, value in page_data.items():
    html = html.replace('{% ' + key + ' %}', value)

#HTML出力
print(html)

