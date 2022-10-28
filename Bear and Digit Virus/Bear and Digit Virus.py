def main():
    def findout(s):
        time=0
        check=0
        def tran(s):
            MAX=0
            for i in range(len(s)):
                if ord(s[i])-48>MAX:
                    MAX=ord(s[i])-48
                if MAX==9:
                    break
            temp=''        
            for i in range(len(s)):
                T=ord(s[i])-48
                cur=T
                if T<MAX:
                    for j in range(max(i-(MAX-T),0),min(i+(MAX-T)+1,len(s))):
                        TT=ord(s[j])-48
                        dis=abs(i-j)
                        if TT>cur:
                            if (TT-T)>=dis:
                                cur=TT
                                if cur==MAX:
                                    break
                temp+=str(cur)
            return temp
        while(tran(s)!=s):
            time+=1
            s=tran(s)
        return time    

    def find(s):
        check=1
        for i in range(len(s)):
            if ord(s[i])-48>1:
                check=0
                break
        if check==1:
            return 1
        else:
            return 0

    def zerone(s):
        maxlen=0
        check=0
        temp=[]
        curlen=0
        for i in range(len(s)):
            if s[i]=='0':
                break
        start=i
        for i in range(start,len(s)):
            if s[i]=='0':
                curlen+=1
                if i==len(s)-1:
                    temp+=[curlen]
            else:
                if curlen>0:
                    temp+=[curlen]
                    if curlen>maxlen:
                        maxlen=curlen
                    curlen=0  




        if s[0]=='1' and s[-1]=='1':
            return (maxlen+1)//2
        elif s[0]=='0' and s[-1]=='1':
            first=temp[0]
            return max(first,(maxlen+1)//2)
        elif s[0]=='1' and s[-1]=='0':
            end=temp[-1]
            return max(end,(maxlen+1)//2)
        else:
            first=temp[0]
            end=temp[-1]
            return max(first,end,(maxlen+1)//2)







    T=int(input())
    for _ in range(T):
        s=input()
        check=0
        if find(s)==0:
            print(findout(s)) 
        else:
            print(zerone(s))
            
main()            
