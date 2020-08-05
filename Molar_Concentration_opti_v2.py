#Calculating Molecular_Concentration
"""
1M = Molecular Weight(g)/L
"""
print('This is a programme for calculating how much reagent you need to make a certain molar concentration solution')
FC=float(input('Final concentration= ')) 
c_unit=input()
while c_unit=='M' or 'mM' or'uM':
    if c_unit=='M':
        concentration=FC/1
        break
    elif c_unit=='mM':
        concentration=FC/1000
        break
    elif c_unit=='uM':
        concentration=FC/1000000  
        break
    else:
        c_unit=input('Please input valid concentration unit: ')
FV=float(input('Final volume= ')) 
v_unit=input()
while v_unit=='L' or 'l' or v_unit=='mL' or 'ml' or v_unit=='uL' or 'ul':
    if v_unit=='L' or v_unit=='l':
        volume=FV/1
        break
    elif v_unit=='mL' or v_unit=='ml':
        volume=FV/1000
        break
    elif v_unit=='uL' or v_unit=='ul':
        volume=FV/1000000
        break
    else:
        v_unit=input('Please input valid volume unit: ')
MW=float(input('Please input Molecular Weight(g): '))
print(f'Adding {round(concentration*volume*MW,6)} g into {FV} {v_unit}, getting {FC} {c_unit} solution.')

