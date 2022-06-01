from tkinter import * # библиотека
import requests # библиотека
def get_crypt(): # функция
    """ДАННАЯ ФУНКЦИЯ ВЫПОЛНЯЕТ ПАРСИНГ КРИПТОВАЛЮТЫ С САЙТА COINMARKETCAP"""
    global info # переменная
    global metka # переменная
    metka.destroy() # удаляет метку при повторном получаении информации о криптовалюте
    lst=[] # Объявляет список
    request=requests.get(url='https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing?start=1&limit=10000').json() # API coinmarketcap в формате json
    for crypto in request['data']['cryptoCurrencyList']:
        if crypto.get('name').lower() == info.get().lower(): # сравнение поля ввода и названия криптовалюты
            info_name=crypto['name'] # название криптовалюты
            info_price=crypto['quotes'][0]['price'] # цена криптовалюты
            lst.append(info_name) # Добавляю в список название криптовалюты
            lst.append(info_price) # Добавляю в список цену криптовалюты
            metka=Label(root, text=f'Название: {lst[0]}\n' \
                                   f'Цена: {lst[1]:.3f}$', bg='#FFFFFF', fg='#060606', font=('Times New Romans', 14, 'bold')) # Метка с названием и ценой введеной пользователем криптовалюты
            metka.place(x=170,y=15)


""" Эти строки предназначены для создания окна приложения и его компонентов"""
root=Tk()
root.resizable(height=False,width=False)
root.geometry('500x500')
root.title('Парсер')
root.iconphoto(True, PhotoImage(file=('icon.png')))
root['bg']='#686868'
metka=Label(root)
info=StringVar()
vvod=Entry(root, font=('Times New Roman', 16, 'bold'), textvariable=info,justify='center', bg='#0004FF', fg='#FFFFFF')
vvod.place(x=145,y=250)
knpars=Button(root,text='Получить информацию', fg='#FFFFFF', bg='#FF0000', font=('Calibri', 12, 'bold'), command=get_crypt)
knpars.place(x=167,y=350)
root.mainloop()