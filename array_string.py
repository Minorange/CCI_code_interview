#!/usr/local/bin/python3

class Questions:
    def isUnique(self,string):
        if len(string) > 128:
            return False
        hashmap = {}
        for letter in string:
            if letter in hashmap:
                return False
            else:
                hashmap[letter] = 1
        return True

    def checkPermutation(self,strA,strB):
        import collections
        if len(strA) != len(strB):
            return False
        setA = collections.Counter(strA)
        setB = collections.Counter(strB)
        return setA == setB

    def URLify(self,string):
        strList = string.split()
        return '%20'.join(strList)
    
    def palindromePerm(self,string):
        import collections
        setStr = collections.Counter(string)
        count = 0
        for key in setStr.keys():
            if key != ' ' and setStr[key] % 2 != 0:
                count += 1
        return not (count > 1)

    def oneWay(self,A,B):
        # A,B are two strings

        # Length check
        if abs(len(A) - len(B)) > 1:
            return False
        # make sure A is shorter than B
        if len(A) > len(B):
            return self.oneWay(B,A)
        
        idx1 = idx2 = 0
        foundDiff = False
        while idx2 < len(B) and idx1 < len(A):
            if A[idx1] != B[idx2]:
                if foundDiff:
                    return False
                else:
                    foundDiff = True
                if len(A) == len(B):
                    idx1 += 1
            else:
                idx1 +=1 
            idx2 += 1
            # for insertion and removal, when no equal, longer +1
        return True


    def stringCompress(self,string):
        newS = string[0]
        string += '#'
        count = 1
        for i in range(1,len(string)):
            if string[i] == string[i-1]:
                count += 1
            else:
                newS += str(count) + string[i]
                count = 1
        return newS[:-1] if len(newS) < len(string) else string[:-1]
def main():
    import sys
    while True:
        try:
            argumentList = sys.argv
            print('Interview Questions: ', argumentList[1])
            if argumentList[1] == '1.1':
                ret = Questions().isUnique(argumentList[2])

            if argumentList[1] == '1.2':
                ret = Questions().checkPermutation(argumentList[2],argumentList[3])

            if argumentList[1] == '1.3':
                ret = Questions().URLify(argumentList[2])

            if argumentList[1] == '1.4':
                ret = Questions().palindromePerm(argumentList[2])

            if argumentList[1] == '1.5':
                ret = Questions().oneWay(argumentList[2],argumentList[3])

            if argumentList[1] == '1.6':
                ret = Questions().stringCompress(argumentList[2])

            print(ret)
            break
        except ValueError:
            print("Not enough arguments.")
            #break

if __name__ == '__main__':
    main()
