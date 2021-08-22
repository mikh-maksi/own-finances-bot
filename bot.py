# Импортируем все необходимые библиотеки
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from datetime import datetime

# Импортируем дополнительный файл, в котором храним токен.
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

def read_categories():
    with open('./work/python/bot/bot_categ.txt', 'r') as f:
        for line in f:
            elements = line.split(' ')
    f.close()
    return elements

def write_record(msg):
    f = open('./work/python/bot/log_bot.txt', 'a')
    f.write(msg)
    now = datetime.now()
    current_dt = now.strftime("%Y-%m-%d|%H:%M:%S")
    f.write(' ')
    f.write(current_dt)
    f.write(' \n')
    f.close()

def check_digit(msg):
    elements = msg.split(' ')
    if not elements[1].isdigit():
        return False
    else:
        return True


cat_list = read_categories()
total_dict = dict.fromkeys(cat_list,0)
cats = ['eat','ent']
print(cats[1] in cat_list)

# Функция, которая вычисляет итоговое состояние
def total_costs(lst):
    global total_dict
    for d in lst:
        total_dict[d[0]] = total_dict[d[0]]+d[1]
    print(total_dict)
    return total_dict

# Старт1
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    string = '''<b>Ты подключился к боту управляния личными финанасми</b>

<b>Посмотри существующие категории расходов</b>: 
/addcat
<b>Добавляй расходы:</b> 
/eat 10 батон
<b>Смотри суммарный расход:</b> 
/total
<b>Полное описание функций:</b> 
/help
    '''
    await bot.send_message(
            message.from_user.id,
            string,
            parse_mode='HTML',
        )
# Добавляем, просматриваем и удаляем категории
@dp.message_handler(commands=['addcat'])
async def addcat_command(message: types.Message):
    global cat_list
    elements = message.text.split(' ')
    print(elements[1])
    print(cat_list)
    if (elements[1] in cat_list):
        await message.reply("Категория - существует!")
    else:
        with open('./work/python/bot/bot_categ.txt', 'w') as f:
            for el in cat_list:
                f.write(el+' ')
            f.write(elements[1])
        f.close()
        await message.reply("Категорию "+ elements[1]+" добавили!")

@dp.message_handler(commands=['cat'])
async def addcat_command(message: types.Message):
    global cat_list
    string = '\n'.join(cat_list)
    await message.reply(string)

@dp.message_handler(commands=['delcat'])
async def addcat_command(message: types.Message):
    global cat_list
    elements = message.text.split(' ')
    cat_list.pop(cat_list.index(elements[1]))
    cat_list_str = ' '.join(cat_list)
    with open('./work/python/bot/bot_categ.txt', 'w') as f:
        f.write(cat_list_str)
    f.close()
    await message.reply("Категория "+ elements[1] + " удалена")


# Обработка команд с указанием категории расходов
@dp.message_handler(commands=cat_list)
async def process_other_command(message: types.Message):    
    print(message.get_command())
    if check_digit(message.text):
        write_record(message.text)
        await message.reply("Запись зафиксировали! "+ message.text)
    else:
        await message.reply("после "+message.get_command()+" введите сумму расходов")

# Команда, которая подводит итоги
@dp.message_handler(commands=['total'])
async def process_total_command(message: types.Message):
    # ------------------
    fin_list = []
    with open('./work/python/bot/log_bot.txt', 'r') as f:
        for line in f:
            elements = line.split(' ')
            #собираем массив из элементов после первого (0 - типа траты, 1 - сумма, 2+ - описание). Но исключаем последний элемент (символ окончания строки).
            st = [elements[i] for i in range(2,len(elements)-2)]
            scr = ' '.join(st)
            lst = [elements[0][1:],int(elements[1]),scr,elements[len(elements)-2]]
            fin_list.append(lst)                  
    f.close()
    ttl_out = str(total_costs(fin_list))
    # ------------------
    await message.reply("Итого: "+ ttl_out)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    string = '''<b>Посмотреть доступные категории</b>: 
/cat
<b>Добавить категорию расходов</b>: 
/addcat <i>Название</i>
<b>Удалить категорию  расходов</b>: 
/delcat <i>Название</i>
<b>Добавить расход</b>: 
/<i>Название</i> сумма комментарии
Пример: /eat 20 Мороженное 
<b>Посмотреть суммарный расход:</b> 
/total
    '''
    await bot.send_message(
            message.from_user.id,
            string,
            parse_mode='HTML',
        )

@dp.message_handler()
async def echo_message(msg: types.Message):
     f = open('./work/python/bot/log_bot.txt', 'a')
     f.write(msg.text)
     f.write('\n')
     f.close()
     await bot.send_message(msg.from_user.id, msg.text+"просто текст")

if __name__ == '__main__':
    executor.start_polling(dp)
