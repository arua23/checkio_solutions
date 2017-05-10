def checkio(data):
    numerals={"I":1,"IV":4,"V":5,"IX":9,"X":10,"XL":40,"L":50,"XC":90,"C":100,"CD":400,"D":500,"CM":900,"M":1000 }
    roman=""
    while data>0:
        if data>=numerals["I"] and data<numerals["IV"]:
            roman+="I"
            data-=1
        elif data>=numerals["IV"] and data<numerals["V"]:
            roman+="IV"
            data-=4
        elif data>=numerals["V"] and data<numerals["IX"]:
            roman+="V"
            data-=5
        elif data>=numerals["IX"] and data<numerals["X"]:
            roman+="IX"
            data-=9
        elif data>=numerals["X"] and data<numerals["XL"]:
            roman+="X"
            data-=10
        elif data>=numerals["XL"] and data<numerals["L"]:
            roman+="XL"
            data-=40
        elif data>=numerals["L"] and data<numerals["XC"]:
            roman+="L"
            data-=50
        elif data>=numerals["XC"] and data<numerals["C"]:
            roman+="XC"
            data-=90
        elif data>=numerals["C"] and data<numerals["CD"]:
            roman+="C"
            data-=100
        elif data>=numerals["CD"] and data<numerals["D"]:
            roman+="CD"
            data-=400
        elif data>=numerals["D"] and data<numerals["CM"]:
            roman+="D"
            data-=500
        elif data>=numerals["CM"] and data<numerals["M"]:
            roman+="CM"
            data-=900
        else:
            roman+="M"
            data-=1000

    return roman

print(checkio(45))
print(checkio(6))
print(checkio(76))
print(checkio(499))
print(checkio(3888))
