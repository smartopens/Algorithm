h, m = map(int, input().split())

totalTime = h*60 + m
totalTime -= 45

if totalTime < 0:
    totalTime = 24*60 + totalTime
newHour =  totalTime // 60
newMin = totalTime % 60

print(newHour, newMin)