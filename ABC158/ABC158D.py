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

true_position = True
left = ""
right = ""

for i in range(q):
    if len(query_list[i])==1:
        true_position = not true_position
        # print(s)
    else:
        if query_list[i][2]=="1":
            if true_position:
                left = query_list[i][4] + left
            else:
                right = right + query_list[i][4]
        elif query_list[i][2]=="2":
            if true_position:
                right = right + query_list[i][4]
            else:
                left = query_list[i][4] + left

if true_position:
    ans = left + s + right
else:
    ans = right[::-1]+s[::-1]+left[::-1]

print(ans)