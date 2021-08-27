list1 = list(map(int, input("Enter List of Numbers:").strip().split()))

mx = max(list1[0], list1[1])
secondMax = min(list1[0], list1[1])

n = len(list1)

for i in range(2,n):
    if list1[i]>mx:
        secondMax = mx
        mx = list1[i]

    elif list1[i] > secondMax and mx != list1[i]:
        secondMax = list1[i]

print("Second Highest Number:", secondMax)
