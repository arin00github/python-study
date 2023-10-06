# STUDY : 05. 파이썬 클래스
# 클래스를 정의한다는 것은 새로운 데이터 타입을 정의한 것
# 이를 실제로 사용하려면 인스턴스라는 것을 생성해야 함
# 메서드(method): 클래스 내부에 정의돼 있는 함수


class BusinessCard:
    def __init__(self, name, email, city):
        self.name = name
        self.email = email
        self.city = city
    def print_info(self):
        print('---------------')
        print("Name: ", self.name)
        print("E-mail: ", self.email)
        print("City: ", self.city)
        print('---------------')


# 'BusinessCard'라는 클래스의 인스턴스가 메모리의 0x0302ABB0 위치에 생성되고 card1이라는 변수가 이를 바인딩

# member1 = BusinessCard()
# member1.set_info("Jane","jane@gmail.com",'Paris')
# print(member1.name, member1.city)
# member1.print_info()

# member2 = BusinessCard("Kangin Lee", "kangin@gmail.com", 'Barcellona')
# member2.print_info()


# STUDY : 2) 클래스 생성자

# 인스턴스 생성과 동시에 자동으로 호출되는 메서드인 생성자가 존재

class MyClass:
    def __init__(self):
        print("MyClass object created!")
        
        
# class1 = MyClass() # MyClass object created!


# STUDY : 5) 클래스 변수와 인스턴스 변수

# 여러 인스턴스 간에 서로 공유해야 하는 값은 클래스 변수를 통해 바인딩해야 함
# 인스턴스의 네임스페이스에 없는 이름은 클래스의 네임스페이스에서 찾아보기 때문


class Account:
    num_accounts = 0
    def __init__(self, name):
        self.name = name
        Account.num_accounts += 1
    def __del__(self):
        Account.num_accounts -= 1
        

kim = Account('kim')
lee = Account('lee')

# print(kim.num_accounts) # 2
# print(lee.num_accounts) # 2



# STUDY : 6) 클래스 상속

class Parent:
    def can_sing(self):
        print('Sing a song')
        
father1 = Parent()
father1.can_sing()

class LuckyChild(Parent):
    pass

child1 = LuckyChild()
child1.can_sing()

class LuckyChild2(Parent):
    def can_dance(self):
        print('Shuffle Dance')
        
child2 = LuckyChild2()
child2.can_dance() # Shuffle Dance