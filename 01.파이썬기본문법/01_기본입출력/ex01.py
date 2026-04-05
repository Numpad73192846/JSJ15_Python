# ctrl + F5 : Run
# shift + enter : Run in terminal

# print() : 화면에 출력하는 함수
print(" Hello World!")

# 여러 줄을 출력할 때는 """ """ 또는 ''' '''를 사용한다.
print("""
Hello World!
This is Python Programming.
""")

print('''
Hello World!
This is Python Programming.
''')

# 문자열을 변수에 저장할 수 있다.
a = "Python"
b = "Programming"

# 문자열을 연결하여 출력할 수 있다.
print( a + " " + b ) 

# 문자열과 숫자를 연결하여 출력할 때는 str() 함수를 사용하여 숫자를 문자열로 변환해야 한다.
num = 10
print("The number is : " + str(num))

# ,를 사용하여 문자열과 숫자를 연결할 수도 있다. 이 경우에는 str() 함수를 사용하지 않아도 된다.
print( "The number is :", num)

# * 연산자를 사용하여 문자열을 반복할 수 있다.
print("Hello \n" * 10)