s = input()
q = int(input())

query_list = []
for _ in range(q):
    query_list += [input()]


def query1(s):
    s = s[::-1]
    return s

def query2_1(letters,s):
    s = letters[4] + s
    return s

def query2_2(letters,s):
    s = s +  letters[4]
    return s

for i in range(q):
    if len(query_list[i])==1:
        s = query1(s)
        # print(s)
    else:
        if query_list[i][2]=="1":
            s = query2_1(query_list[i],s)
            # print(s)
        elif query_list[i][2]=="2":
            s = query2_2(query_list[i],s)
            # print(s)

print(s)