def q(c,v,mw):
    return c*v*mw
def jud(num,unit):
    if unit[0]=='m':
        num=float(num)/1000
    elif unit[0]=='u':
        num=float(num)/1000000
    else:
        num=float(num)
    return float(num)
FC=float(input('Please enter final concentration: '))
c_unit=input()
FV=float(input('Please enter final volume： '))
v_unit=input()
MW=float(input('Please enter Molecular Weight(g): '))
print(f'Adding {round(q(jud(FC,c_unit),jud(FV,v_unit),MW),6)} g into {FV} {v_unit}, getting {FC} {c_unit} solution.')

