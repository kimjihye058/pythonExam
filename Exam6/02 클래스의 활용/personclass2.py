class Person():
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def __str__(self):      # 객체와 관련된 정보를 포함하고 있는 문자열 반환 메소드
        return "Person 설명, 이름은 " + self.name + " 키는 " + str(self.height)
    
    def __len__(self):      # 리스트 내부에 포함된 요소의 개수 반환 메소드
        return self.height
    
    def __getitem__(self, key):     # 대괄호 안의 첨자를 통해 객체에 접근할 때 첨자로 전달되는 키 값에 따라 대응되는 적정한 값 반환 메소드
        if key == "name":
            return self.name
        if key == "age":
            return self.age
        return None
    
p = Person("철수", 18, 170)
print(p)
print(len(p))       # 키만 나옴(len을 재정의 해서)
print(p['age'])     # 리스트의 0번째를 key로 넘겨주었다.
print(p['unknown'])