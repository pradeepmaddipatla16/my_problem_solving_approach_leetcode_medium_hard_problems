def function1(list1):
    traversed = set()
    for each in list1:
        local = each[:each.index('@')]
        domain=each[(each.index('@')+1):]
        if '+' in local:
            local = local[:local.index('+')]
        traversed.add(local.replace('.','')+'@'+domain)
    return len(traversed)

print(function1(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))