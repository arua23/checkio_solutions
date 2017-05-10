def checkio(expression):
    exp=list(expression)
    op={(i):exp[i] for i in range(len(exp)) if exp[i] in ["(","{","["]}
    cl={(j):exp[j] for j in range(len(exp)) if exp[j] in [")","}","]"]}
    if len(op)>0 and len(cl)>0:
        n=min(op.keys())
        start=max(op.keys())
        while start>n-1:
            start=max(op.keys())
            if op.get(start)=="(":
                end=[i for i in cl.keys() if cl[i]==")"]
                if len(end)>0:
                    pair_end=max(end)
                    del op[start]
                    del cl[pair_end]
            elif op.get(start)=="{":
                end=[i for i in cl.keys() if cl[i]=="}"]
                if len(end)>0:
                    pair_end=max(end)
                    del op[start]
                    del cl[pair_end]
            elif op.get(start)=="[":
                end=[i for i in cl.keys() if cl[i]=="]"]
                if len(end)>0:
                    pair_end=max(end)
                    del op[start]
                    del cl[pair_end]
            start-=1
    print(op)
    print(cl)
    
    
        
        
checkio("(2+1)*[3/{1-(2+1)}]")
checkio("(({[(((1)-2)+3)-3]/3}-3)")
checkio("2+3")
checkio("[1+1]+(2*2)-{3/3}")
checkio("(3+{1-1)}")
