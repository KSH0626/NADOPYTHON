def profile(name, age, main_lang):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}"\
         .format(name, age, main_lang)) #\후 enter는 한 문장으로 적용
profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")

#같은 학교 같은 학년 같은 반 같은 수업.
#기본값 사용 방법

def profile(name, age=17, main_lang="파이썬"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}"\
         .format(name, age, main_lang))

profile("유재석")
profile("김태호")

def profile(name, age, main_lang):
    print(name, age, main_lang)
profile(name = "유재석", main_lang = "파이썬", age=20)
profile(main_lang = "자바", age = 25, name = "김태호") #이런식으로 순서가 뒤섞여있어도 어떤 값이 어느 변수에 들어가는지 지정만 잘 해주면 ㄱㅊ