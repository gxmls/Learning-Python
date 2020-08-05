#Calculating Molecular_Concentration
"""
1M = Molecular Weight(g)/L
"""
print('This is a programme for calculating how much reagent you need to make a certain molar concentration solution')
concentration=float(input('Final concentration= '))
c_unit=str(input())
volume=float(input('Final volume= '))
v_unit=str(input())
MW=float(input('Please input Molecular Weight(g)= '))
if v_unit=='L' or v_unit=='l':
    if c_unit=='M':
        print('Add %f g into %f L, getting %f M solution' % (concentration*volume*MW, volume, concentration))
    elif c_unit=='mM':
        print('Add %f g into %f L, getting %f mM solution' % (concentration/1000*volume*MW, volume, concentration))
    else:
        print('Add %f g into %f L, getting %f uM solution' % (concentration/1000000*volume*MW, volume, concentration))
elif v_unit=='mL' or v_unit=='ml':
    if c_unit=='M':
        print('Add %f g into %f mL, getting %f M solution' % (concentration*(volume/1000)*MW, volume, concentration))
    elif c_unit=='mM':
        print('Add %f g into %f mL, getting %f mM solution' % ((concentration/1000)*(volume/1000)*MW, volume, concentration))
    else:
        print('Add %f g into %f mL, getting %f uM solution' % ((concentration/1000000)*(volume/1000)*MW, volume, concentration))
elif v_unit=='uL' or v_unit=='ul':
    if c_unit=='M':
        print('Add %f g into %f uL, getting %f M solution' % (concentration*(volume/1000000)*MW, volume, concentration))
    elif c_unit=='mM':
        print('Add %f g into %f uL, getting %f mM solution' % ((concentration/1000)*(volume/1000000)*MW, volume, concentration))
    else:
        print('Add %f g into %f uL, getting %f uM solution' % ((concentration/1000000)*(volume/1000000)*MW, volume, concentration))
else:
    print('Please input valid volume unit of concentration unit!')
