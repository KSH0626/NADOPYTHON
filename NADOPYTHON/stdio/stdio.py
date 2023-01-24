print("Python","Java", "JavaScript", sep=" vs ")
print("Python", "Java", sep=",", end="?") # 파라미터 사이의 연결구조 밑 줄바꿈 모양 변경 가능
print("무엇이 더 재밌을까요?")

import sys
print("Python", "Java", file=sys.stdout)
print("Python", "Java", file=sys.stderr)

scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":")#좌우정렬

# 은행 대기순번표
# 001,002,003,004 ...
for num in range(1,21):
    print("대기번호 : "+str(num).zfill(3))#zfill: 빈자리에 0으로 채우기

answer = input("아무 값이나 입력하세요: ")
#input으로 받으면 항상 str형태로 받게 된다!
print("입력하신 값은 "+ str(answer) + "입니다.")