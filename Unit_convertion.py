#Convertion between uM and mM
#1mM = 1000 uM
concentration=float(input('Please input concentration: '))
unit=input('Please input unit: ')
if unit=='uM': #Note: use '==',not '=' and don't forget a ':'
    print('%f uM = %f mM' % (concentration,concentration/1000))
elif unit=='mM':
    print('%f mM = %f uM' % (concentration,concentration*1000))
else:
    print('Please input a valid unit')
