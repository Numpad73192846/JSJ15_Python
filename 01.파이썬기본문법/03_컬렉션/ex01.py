li = [100, 12.34, "Hello"]
print( 'li : ', li )

# indexing
print ( 'li[0] : ', li[0] )
print ( 'li[1] : ', li[1] )
print ( 'li[2] : ', li[2] )

# slicing
print ( 'li[0:2] : ', li[0:2] )
print ( 'li[1:] : ', li[1:] )
print ( 'li[:2] : ', li[:2] )

# append() : 리스트의 마지막에 요소를 추가하는 함수
li.append(200)
print( 'li : ', li )

# insert() : 리스트의 특정 위치에 요소를 추가하는 함수
li.insert(1, 300)
print( 'li : ', li )

# pop() : 리스트의 마지막 요소를 제거하는 함수
li.pop()
print( 'li : ', li )

# pop(index) : 리스트의 특정 위치에 있는 요소를 제거하는 함수
li.pop(1)
print( 'li : ', li )

dic = { "name": "Alice", "age": 30, "city": "New York" }
print( 'dic : ', dic )

# dic[key] = value : 딕셔너리에 새로운 키-값 쌍을 추가하는 방법
dic['address'] = "123 Main St"
print( 'dic : ', dic )

# setdefault() : 딕셔너리에 키가 존재하지 않으면 키-값 쌍을 추가하는 함수
# key가 없으면 새로운 value를 추가 없으면 기존의 value를 반환
# 현재 name이라는 key가 있기때문에 Bob이 아닌 Alice를 반환
dic.setdefault('name', 'Bob')
print( 'dic : ', dic )

dic.setdefault('phone', '010-1234-5678')
print( 'dic : ', dic )

# update() : 딕셔너리에 여러 개의 키-값 쌍을 추가하는 함수
# key가 있으면 value를 업데이트 없으면 새로운 key-value를 추가
dic.update( age = 20, email = "alice@example.com" )
print( 'dic : ', dic )

dic.pop('email')
print( 'dic : ', dic )