

def foreing_exchange_calculator(ammount):
    mex_to_col_rate = 145.97
    valor_euro_actual = 33.95
    valor_soles = 23.45
    return mex_to_col_rate * ammount
    return valor_euro_actual * ammount
    return valor_soles * ammount
def run():
    print ('CALCULADORA DE DIVISAS')
    print ('convierte pesos mexicanos a pesos colombianos ')
    print('')
    ammount = float(input('ingresa la cantidad:'))

    result = foreing_exchange_calculator(ammount)
    result_euros = foreing_exchange_calculator(ammount) 
    result_soles = foreing_exchange_calculator(ammount)

    print ('${} pesos mexicanos son ${} pesos colombianos y en euros son E{} soles E{} '.format(ammount,result,result_euros,result_soles))
    print ('')

if __name__ == '__main__':
    run()