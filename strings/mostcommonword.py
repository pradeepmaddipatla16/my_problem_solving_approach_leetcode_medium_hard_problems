from collections import Counter
def mostcommonwords(paragraph,banned):
    banset=set(banned)
    freq = Counter([word.strip("?!,.'") for word in paragraph.lower().split(' ')])
    l=list(freq.most_common())
    for each in l:
        if each[0] not in banset:
            return each[0]






paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned=["hit"]
print(mostcommonwords(paragraph,banned))