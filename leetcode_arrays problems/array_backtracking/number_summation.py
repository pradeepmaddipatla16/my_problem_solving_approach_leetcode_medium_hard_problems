class summation(object):
    def main(self,array,summation,max):
        n = len(array)
        array.sort()
        res = []
        self.computation(array,0,[],max,res)
        final_res = []
        for each in res:
            if len(each) == summation:
                final_res.append(each)
        return final_res
    def computation(self,array,start,dfspath,max,res):
        if max < 0:
            return
        if max == 0:
            res.append(dfspath[:])
        for i in range(start,len(array)):
            if i > start and array[i] == array[i-1]:
                continue
            dfspath.append(array[i])
            self.computation(array,i+1,dfspath,max-array[i],res)
            del dfspath[-1]



