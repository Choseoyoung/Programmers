import re

data = """
park 800905-1049118
kim  700905-1059119
"""
pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******", data))

#결과값:
#park 800905-*******
#kim  700905-*******

#[출처] 파이썬 21 정규 표현식 (re)|작성자 asrisk

pattern=re.compile('cat')
print(pattern.sub('animal','cat and dog'))
print(pattern.sub('animal','cat and dog and cat',1))
