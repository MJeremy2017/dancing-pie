def summary_range(A):
    last = -100
    s = ""
    for i in range(len(A)):
        if A[i] - last > 1:
            if i == 0:
                s = s + str(A[i]) + "->"
            else:
                s = s + str(last)
                print(s)
                s = str(A[i]) + "->"
        last = A[i]
    print(s + str(last))

class C:
    def __init__(self):
        self.A = []
        
    def add_num(self, val):
        if len(self.A) == 0:
            self.A.append((val, val))
            
        n = len(self.A)
        index = 0
        for i in range(n):
            if val <= self.A[i][1] + 1:
                index = i
                break
        if index == n-1 and val > self.A[n-1][1]:
            self.A.append((val, val))
            return
        if val > self.A[index][1]:
            self.A[index][1] = val
            return
        if val < self.A[index][0]:
            self.A[index[0] = val
            return
        
                
if __name__ == "__main__":
    arr = [1, 2, 2, 3, 5, 6, 6, 8, 9, 10]
    summary_range(arr)
