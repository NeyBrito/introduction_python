from datetime import date, time, datetime, timedelta

def trabalhando_com_date():
    data_atual = date.today()
    data_atual_str = data_atual.strftime('%A %B %Y %d/%m/%y')

    print(type(data_atual))
    print(data_atual_str)

def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    print(horario.strftime('%H:%M:%S'))

def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual.strftime('%d/%m/%y %H:%M:%S'))
    print(data_atual.strftime('%c'))
    print(data_atual.weekday())
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo')
    print(tupla[data_atual.weekday()])
    data_criada = datetime(2018, 6, 20, 15, 30, 20)
    print(data_criada)
    print(data_criada.strftime('%c'))
    data_string = '01/01/2019'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y')
    print(data_convertida)
    nova_data = data_convertida - timedelta(days=365, hours=2)
    print(nova_data)


if __name__ == '__main__':
    # trabalhando_com_date()
    # trabalhando_com_time()
    trabalhando_com_datetime()

# from datetime import datetime
# data_atual = datetime.now()
# resultado = data_atual.strftime('%d/%m/%Y %H:%M:%S')
# print(resultado)

# from datetime import datetime, time, timedelta
# data = datetime(1815, 12, 10, 00, 00, 00).strftime('%d/%m/%Y')
# hora = time(hour=13, minute=14, second=00)
# print('{} às {}'.format(data, hora))


# data_viagem = datetime.now() - timedelta(days=1)
# print(datetime.now().weekday()) #retornou 0
# print(data_viagem)

# from datetime import timedelta
# hour = timedelta(hours=15)
# soma = hour + 1