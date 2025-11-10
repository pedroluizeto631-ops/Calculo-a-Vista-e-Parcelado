p = float(input('qual é o preço do produto ? R$'))
nvp = p + (p*15/100)
nvpp = p- (p*10/100)
print('o produto que custa {} \n com parcelamento ele ficará com {} de desconto \n e a vista será {}reais'.format(p, nvp, nvpp))