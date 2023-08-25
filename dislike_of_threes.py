t = int(input())
int_arr = []

integers = 1
while len(int_arr) <= 1000:
    if integers % 3 != 0 and str(integers)[-1] != "3":
        int_arr.append(integers)
    integers += 1

for _ in range(t):
    k = int(input())
    print(int_arr[k-1])
