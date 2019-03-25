complete_list = []
your_list = ['a','b','c']
for current in range(5):
    a = [i for i in your_list]
    print(a)

    for y in range(current):
        b = []
        for x in a:
            for i in your_list:
                b.append(x+i)
            print(b)
            a = [i for i in b]
    complete_list = complete_list + a