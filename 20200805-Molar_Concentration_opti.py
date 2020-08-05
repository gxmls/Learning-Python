#Calculating Molecular_Concentration
"""
1M = Molecular Weight(g)/L
"""
print('This is a programme for calculating how much reagent you need to make a certain molar concentration solution')
concentration=float(input('Final concentration= '))
c_unit=input()
volume=float(input('Final volume= '))
v_unit=input()
MW=float(input('Please input Molecular Weight(g)= '))
if v_unit=='L' or v_unit=='l':
    if c_unit=='M':
        print(f'Add {concentration*volume*MW} g into {volume} L, getting {concentration} M solution')
    elif c_unit=='mM':
        print(f'Add {concentration/1000*volume*MW} g into {volume} L, getting {concentration} mM solution')
    else:
        print(f'Add {concentration/1000000*volume*MW} g into {volume} L, getting {concentration} uM solution')
elif v_unit=='mL' or v_unit=='ml':
    if c_unit=='M':
        print(f'Add {concentration*(volume/1000)*MW} g into {volume} mL, getting {concentration} M solution')
    elif c_unit=='mM':
        print(f'Add {(concentration/1000)*(volume/1000)*MW} g into {volume} mL, getting {concentration} mM solution')
    else:
        print(f'Add {(concentration/1000000)*(volume/1000)*MW} g into {volume} mL, getting {concentration} uM solution')
elif v_unit=='uL' or v_unit=='ul':
    if c_unit=='M':
        print(f'Add {concentration*(volume/1000000)*MW} g into {volume} uL, getting {concentration} M solution')
    elif c_unit=='mM':
        print(f'Add {(concentration/1000)*(volume/1000000)*MW} g into {volume} uL, getting {concentration} mM solution')
    else:
        print(f'Add {(concentration/1000000)*(volume/1000000)*MW} g into {volume} uL, getting {concentration} uM solution')
else:
    print('Please input valid volume unit of concentration unit!')
