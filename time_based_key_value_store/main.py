# class TimeMap:
#     def __init__(self):
#         self.keyStore = {}
         

#     def set(self, key: str, value: str, timestamp: int) -> None:
#         if key not in self.keyStore:
#             self.keyStore[key] = []
#         self.keyStore[key].append([value,timestamp])
        

#     def get(self, key: str, timestamp: int) -> str:
#         res, values = "", self.keyStore.get(key, [])
#         l, r = 0, len(values) - 1
#         while l <= r:
#             m = (l + r) // 2
#             if values[m][1] <= timestamp:
#                 res = values[m][0]
#                 l = m + 1
#             else:
#                 r = m - 1
#         return res
        












class TimeMap:
    def __init__(self):
        self.keyStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        # binary search and keep minimum
        values = self.keyStore.get(key,[])
        res = ""
        l, r = 0,len(values) - 1
        while l <= r:
            c = l + (r - l) // 2
            if values[c][0] <= timestamp:
                res = values[c][1]
                l = c + 1
            else:
                r = c - 1
        return res



test =  TimeMap()

test.set("alice","happy",1)
test.set("alice","sad",10)
print(test.get("alice", 111))









