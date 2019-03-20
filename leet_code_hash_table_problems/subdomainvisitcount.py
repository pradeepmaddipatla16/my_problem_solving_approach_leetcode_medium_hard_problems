'''
from collections import Counter
def function1(domainlist):
    buf_dict= Counter()
    for each_domain in domainlist:
        count,domain = each_domain.split()
        count = int(count)
        fragments = domain.split('.')
        for i in range(len(fragments)):
            buf_dict['.'.join(fragments[i:])]+=count
    return ["{} {}".format(ct, dom) for dom,ct in buf_dict.items()]



print(function1(["9001 discuss.leetcode.com"]))

'''

class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        buf_dict={}
        for each in cpdomains:
            count,domain = each.split(" ")
            count = int(count)
            domainlist = domain.split(".")
            for i in range(len(domainlist)):
                key = '.'.join(domainlist[i:])
                if key in buf_dict:
                    buf_dict[key]+=count
                else:
                    buf_dict[key]=count
        return ["{} {}".format(ct,dom) for dom,ct in buf_dict.items()]


a = Solution()
print(a.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))
