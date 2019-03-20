def func1(words1,words2,pairs):
    if len(words1)!=len(words2):return False
    pairset = set(map(tuple,pairs))
    for w1,w2 in zip(words1,words2):
        if w1==w2 or (w1,w2) in pairset or (w2,w1) in pairset:return True

    return False


print(func1(['great','acting','skills'],['fine','drama','talent'],[['great','fine'],['acting','drama'],['skills','talent']]))
