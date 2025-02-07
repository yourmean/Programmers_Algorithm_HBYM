def solution(new_id):
    answer = ''
    # 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환
    new_id = new_id.lower()
    # 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거
    for w in new_id:
        if w.isalnum() or w in '-_.':
            answer += w
    # 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
    while '..' in answer:
        answer = answer.replace('..','.')
    # 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거
    if answer[0] == '.':
        answer = answer[1:]
    if answer != '':
        if answer[-1] == '.':
            answer = answer[:-1]
    # 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입
    if answer == '':
        answer = 'a'
    # 6단계
    # new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거
    # 만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거
    if len(answer) >=16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    # 7단계 new_id의 길이가 2자 이하라면, 
    # new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입
    if len(answer) <=2:
        answer = answer + answer[-1] * (3-len(answer))
    return answer

# new_id = "...!@BaT#*..y.abcdefghijklm"
# print(solution(new_id))

# new_id = "z-+.^."
# print(solution(new_id))

# new_id = "=.="
# print(solution(new_id))

# new_id = "123_.def"
# print(solution(new_id))

# new_id = "abcdefghijklmn.p"
# print(solution(new_id))