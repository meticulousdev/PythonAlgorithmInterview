# [1] brute force method
def bf_match(txt: str, pat: str) -> int:
    pt = 0
    pp = 0

    while pt != len(txt) and pp != len(pat):
        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1
        else:
            pt = pt - pp +1
            pp = 0

    return pt - pp if pp == len(pat) else -1

# [2] Knuth-Morris-Pratt method 
def kmp_match(txt: str, pat: str) -> int:
    pt = 1
    pp = 0
    skip = [0] * (len(pat) + 1)


if __name__ == "__main__":
    s1 = "ADJNSABAISABCAJSDQNRMZPD"
    s2 = "ABC"

    idx = bf_match(s1, s2)

    if idx == -1:
        print("텍스트 안에 패턴이 존재하지 않습니다.")
    else:
        print(f"{idx+1}번째 문자가 일치합니다.")

# Reference
# Do it! 자료구조와 함께 배우는 알고리즘 입문: 파이썬 편