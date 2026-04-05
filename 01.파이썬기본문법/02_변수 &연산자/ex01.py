a = 10
b = 12.34
c = 'Hello'

# type() 함수로 자료형 확인
print( type(a) )
print( type(b) )
print( type(c) )

list = [1, 2, 3, 4, 5]
print( type(list) )
print( list )

# JSON과 유사한 자료형 - 딕셔너리 (Dictionary)
dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print( type(dict) )
print( dict )

x = 10
y = 20

print( x + y )
print( x - y )
print( x * y )
print( x / y )
print( x ** y )
print( x // y )
print( x % y )

z = 5
print( "z =", z )

z += 1
print( "z += 1\n z =", z )

# and or not
# Java => && || !
print( (x > y) and (x < z) )
print( (x < y) or (x < z) )
print( not (x > y) )

# a in c : a가 c에 포함되어 있는지 확인하는 연산자
# a not in c : a가 c에 포함되어 있지 않은지 확인하는 연산자
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

x = 3 in a
y = 6 in a
z = 7 not in b

print( "x : {}".format(x) )
print( "y : {}".format(y) )
print( "z : {}".format(z) )

m = 100
n = 200

# if 조건 연산자
# if m - n > 0 => m
# else => n
result = m if (m - n) > 0 else n
print( "result : {}".format(result) )