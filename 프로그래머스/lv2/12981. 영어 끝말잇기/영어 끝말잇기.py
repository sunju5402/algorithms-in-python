def solution(n, words):
    answer = [0, 0]
    st = set()
    for i in range(len(words)):
        if st:
            if words[i] in st or words[i][0] != words[i - 1][-1]:
                return [i % n + 1, i // n + 1]
        st.add(words[i])
    return answer