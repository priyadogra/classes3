x = [-5,-4,-3,2,3,4]

main =[]
positive = []
negative = []

for i in x:
    if i>=0:
        positive.append(i)
    else:
        negative.append(i)


for i in negative:
    neg = i
    for i in range(len(positive)-2):
        num = positive[i]+positive[i+1]

    if neg + num == 0:
        main.append([neg,positive[i],positive[i+1]])


print(main)


