text=input("Enter prices seperated by spaces: ")
pieces=text.split()

prices=[]
for p in pieces:
    prices.append(float(p))

if(len(prices)<2):
    print("Not enough values to compute.")
else:
    changes=[]
    pct_return=[]
    for i in range(1,len(prices)):
        old=prices[i-1]
        new=prices[i]
        change=new-old
        pct_change=change/old*100
        changes.append(change)
        pct_return.append(pct_change)

    print("Returns:",changes)
    print("Percentage Returns: ",[round(x,2) for x in pct_return])    

    up=0
    down=0
    unc=0
    for r in changes:
        if r>0:
            up+=1
        elif r<0:
            down+=1
        else:
            unc+=1    

    print("Profitable days=",up)
    print("Loss days=",down)
    print("Constant days=",unc)        

