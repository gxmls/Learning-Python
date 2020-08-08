#Note: quality=concentration*volume*Molecular Weight
print('This is a programme for calculating how much reagent you need to make a certain molar concentration solution')
def q(fc=0,fv=0,mw=0):  #fc=final concentration, fv=final volume
    return fc*fv*mw 
def transm(a=0):
    return a/1000
def transu(b=0):
    return b/1000000
FC=float(input('Please enter final concentration: '))
c_unit=input()
FV=float(input('Please enter final volume: '))
v_unit=input()
MW=float(input('Please enter Molecular Weight(g): '))
if c_unit=='M' or c_unit=='m' or v_unit=='L' or v_unit=='l':
    FC_change=FC/1
    FV_change=FV/1
elif c_unit=='mM' or v_unit=='mL' or v_unit=='ml':
    FC_change=transm(FC)
    FV_change=transm(FV)
else:
    FC_change=transu(FC)
    FV_change=transu(FV)
print(f'Add {round(q(FC_change,FV_change,MW),6)} g into {FV} {v_unit}, getting {FC} {c_unit} solution.') #Note: round(num,dig)
