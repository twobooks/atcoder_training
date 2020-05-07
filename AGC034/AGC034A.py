N,A,B,C,D = map(int,input().split())
S = "0" + input()

if C<D:
    if ("##" in S[A:C+1]) or ("##" in S[B:D+1]):
        print("No")
        exit()
    else:
        print("Yes")
        exit()
else:
    if ("##" in S[A:C+1]) or ("##" in S[B:D+1]):
        print("No")
        exit()
    else:
        if ("..." in S[B-1:D+1+1]):
            print("Yes")
            exit()
        else:
            print("No")
            exit()
