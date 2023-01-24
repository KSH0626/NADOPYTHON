#가변인자를 이용한 함수 호출
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t". format(name, age), end = " ") #end = " "를 사용하여서 문장의 끝맺음의 방법을 바꾼다.
#     print(lang1, lang2, lang3, lang4, lang5)

# profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
# profile("김태호", 25, "Kotlin", "Swift", "", "", "") #이때 lang6으로 늘어나거나 lang2까지밖에 없는 등의 상황이 일어나게 될때 가변인자를 사용한다.

def profile(name, age,*language):
    print("이름 : {0}\t나이 : {1}\t". format(name, age), end = " ")
    for lang in language:
        print(lang, end=" ")
    print()
profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "Java")