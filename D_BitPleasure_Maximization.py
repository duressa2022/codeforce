class TrieNode:
    def __init__(self,length):
        self.childern=[0 for _ in range(length)]
        self.is_end=False
class Trie:
    def __init__(self,length):
        self.root=TrieNode(length)
    def insert(self,num,length):
        cur=self.root
        index=0
        while num>0:
            if cur.childern[index]==0:
                cur.childern[index]=num|(1<<length)
            cur=cur.childern[index]
            index=index+1
            num=num<<1
        cur.is_end=True
    def search(self,num,length):
        cur=self.root
        result=0
        index=0
        while num>0:
            if num&(1<<length) in cur.childern:
                result|=(1<<length)
            cur=cur.childern[index]
            index=index+1
            length=length-1
            num=num<<1
class Solution:
    def compute_prefix(self,array):
        runnig=0
        prefix=[runnig]
        for num  in array:
            runnig^=num
            prefix.append(runnig)
        return prefix
    def compute_suffix(self,array):
        running=0
        suffix=[running]
        for num in reversed(array):
            running^=num
            suffix.append(running)
        return suffix
    def build_Trie(self,prefix):
        max_number=max(prefix)
        length=max_number.bit_length()
        root=Trie(length)
        for cur in prefix:
            root.insert(cur,length)
        return root
def solver():
    n=int(input())
    nums=list(map(int,input().split()))
    solution=Solution()
    prefix=solution.compute_prefix(nums)
    suffix=solution.compute_suffix(nums)
    trie=solution.build_Trie(prefix)
    length=max(prefix).bit_length()
    ans=0
    for suf in suffix:
        ans=max(ans,trie.search(suf,length))
    return ans
print(solver())


    









        

