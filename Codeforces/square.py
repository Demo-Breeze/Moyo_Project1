def square():
    first_number =  int(input("Total inputs:"))
    s = first_number
    answer = []
    i=0
    while first_number > 0:
        b = input("Enter your numbers to be check for validity as a square")
        answer.append(b)
        first_number-=1

    while i < s:
            k = "".join(set(answer[i])).replace(" ", "")
            if len(answer) == 4:
                if len(k) == 1:
                    print(f"{answer[i]} returns YES")
                    pass
                else:
                    print(f"{answer[i]} returns NO")
                    pass
            else:
                 print("Invalid Number")
            i+=1
x =square()