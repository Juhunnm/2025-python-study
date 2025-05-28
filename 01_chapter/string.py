'text'
"text"
"""text"""
''''text'''

#큰 따옴표 포함된 문자열 처리
char = '"Python is very easy"'
# print(char)

# 역슬래시 사용해서 작은 따움표 큰따옴표 포함하기
a = 'Python\'s'
b = "\"Python is very easy\""
# print(b)

#multiline'''*3 """*3
multiline = '''
life is
too 
short
'''
print(multiline)

#문자열 산수 + *
a = "python"
a * 2
"pythonpython"

print("="*50)
# ==================================================


# 문자열 길이 구하기
len("string")


# 인덱싱 슬라이싱
str = "Life is too short, You need Python"
str[3] # e
str[-1] #n

str1 = str[0] + str[1] + str[2] + str[3]
# print(str1) Life
str[0:5]
'Life '
str[0:4]
'Life'
str[0:3]
'Lif'

a[0:2]
'Li'
a[5:7]
'is'
a[12:17]
'short'

a[19:]
'You need Python'

a[:]
'Life is too short, You need Python'

# 불변 (immutable) 자료형

im = 'Pithon'
'''
im[1] = 'y'
print(im)

     im[1] = 'y'
     ~~^^^
 TypeError: 'str' object does not support item assignment
에러 발생
'''

im = im[:1] + 'y' +im[2:]
print(im)
'python'


# 포매팅 (문자열 안에 어떤 값을 삽입하는 방법)

'숫자 바로 대입'
print('I eat %d apples'%3)

'문자열 바로 대입'
print('I eat %s apples'%'five')

'숫자 값을 나타내는 변수로 대입'
number = 3
print('I eat %d apples'%number)
day = 'three'
print('I eat %d apples so I was sick for %s days'%(number,day))

# "Error is %d%." % 98 XX
"Error is %d%%." % 98, 'OO'


# 정렬 & 공백
"%10s" % "hi"
'        hi'

"%-10sjane." % 'hi'
'hi        jane.'

#format 포매팅
"I eat {0} apples".format(3)
'I eat 3 apples'

'정렬'
"{0:<10}".format("hi")
'hi        '
"{0:>10}".format("hi")
'        hi'
"{0:^10}".format("hi")
'    hi    '

'공백 채우기'
"{0:=^10}".format("hi")
'====hi===='
"{0:!<10}".format("hi")
'hi!!!!!!!!'

# f 문자열 포매팅
name = '홍길동'
age = 30
f'나의 이름은 {name}입니다. 나이는 {age}입니다.'
'나의 이름은 홍길동입니다. 나이는 30입니다.'

'정렬'
f'{"hi":<10}'  # 왼쪽 정렬
'hi        '
f'{"hi":>10}'  # 오른쪽 정렬
'        hi'
f'{"hi":^10}'  # 가운데 정렬
'    hi    '

'공백'
f'{"hi":=^10}'  # 가운데 정렬하고 '=' 문자로 공백 채우기
'====hi===='
f'{"hi":!<10}'  # 왼쪽 정렬하고 '!' 문자로 공백 채우기
'hi!!!!!!!!'

y = 3.42134234
f'{y:0.4f}'  # 소수점 4자리까지만 표현
'3.4213'
f'{y:10.4f}'  # 소수점 4자리까지 표현하고 총 자리수를 10으로 맞춤
'    3.4213'

f"난 {1500000:,}원이 필요해"
'난 1,500,000원이 필요해'

#문자열 함수

'''count'''

a = 'hobby'
print(a.count('b'))
'2'

'''find 위치알려주기'''
a = "Python is the best choice"
a.find('b')
14
a.find('k') #존재하지 않으면 -1 반환
-1

'''index find 와 동일하지만 존재하지 않으면 오류 발생'''

'''join 문자열 삽입'''
print(','.join('abcd'))
'a,b,c,d'

",".join(['a', 'b', 'c', 'd'])
'a,b,c,d'

# 소 대문자
a = "hi"
a.upper()
'HI'

a = "HI"
a.lower()
'hi'

#공백지우기
a = " hi "
a.lstrip()
'hi '

a= " hi "
a.rstrip()
' hi'

a = " hi "
a.strip()
'hi'

#  replace 문자열 바꾸기
a = "Life is too short"
print(a.replace('Life','Your leg'))

# split 문자열 나누기 리스트로 나누어짐짐
a = "Life is too short"
a.split()
['Life', 'is', 'too', 'short']

b = "a:b:c:d"
b.split(':')
['a', 'b', 'c', 'd']


# isalpha 문자열이 알파벳으로만 구성되어있는지
'.isalpha()'
# isdigit 숫자로만 구성되어있는지
'.isdigit()'

#endswith  특정 문자열로 끝나는지 확인하기
'.endswith'