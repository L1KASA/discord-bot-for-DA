"""
добавить функцию рандом из всех фильмов, предлагает рандомный фильм
функция рандом среди текущего списка
возможность поставить оценку фильму (желательно меню с тыками сделать)
добавить кинопоиск api
добавить модальные окна
связать бд с кинопоиском
добавить проверки на отправку и прочее
____
начальная версия:
в бота можно добавить фильм
"""
import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
import aiosqlite 
from discord.ext.commands import Bot

load_dotenv()

guild_ids=[os.getenv("SERVER_ID")]

intents = discord.Intents.default()
intents.message_content = True

bot=commands.Bot(intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} готов к работе!")

greetings = ['hello', 'hi', 'дарова', 'приветик', 'привет', 'хола', 'hola', 'пиривет', 'здлавствуйте', 'здарова', 'здравствуйте']

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    for hehe in greetings:
        if str.lower(message.content).startswith(hehe):
            await message.channel.send('Привет!')

@bot.slash_command(name='close', description='Выключить бота', guild_ids=guild_ids)
async def close(ctx):
    #await ctx.delete()
    #await ctx.channel.send('bb')
    #await ctx.defer()
    await ctx.respond('bb')
    await bot.close()

@bot.slash_command(name='select_meadiabase', description='Вывести медиатеку', guild_ids=guild_ids)
async def select_meadiabase(ctx):
    # Устанавливаем соединение с базой данных
    db = await aiosqlite.connect("mediabase.db")
    
    try:
        # Создаем курсор
        cursor = await db.cursor()

        # Выполняем SQL-запрос
        await cursor.execute('SELECT * FROM MEADIABASE')
        
        # Получаем результаты запроса
        data = await cursor.fetchall()

        # Получаем описания столбцов
        columns = [description[0] for description in cursor.description]
        
        # Создаем список для хранения результатов
        result_list = []

        # Фильтруем записи и сохраняем результаты в списке
        for record in data:
            filtered_record = {columns[i]: value for i, value in enumerate(record) if value is not None}
            
            if filtered_record:
                result_list.append(filtered_record)

        # Выводим результаты
        await ctx.respond(str(result_list))

    finally:
        # Закрываем курсор и соединение с базой данных
        await cursor.close()
        await db.close()

class MyModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label="Название медиа"))
        self.add_item(discord.ui.InputText(label="Тип (фильм/сериал)"))

    async def callback(self, interaction: discord.Interaction):
        embed = discord.Embed(title="Информация о медиа")
        embed.add_field(name="Название медиа", value=self.children[0].value)
        embed.add_field(name="Тип (фильм/сериал)", value=self.children[1].value)
        
        async with aiosqlite.connect("mediabase.db") as db:
        
            async with db.cursor() as cursor:
                await cursor.execute('INSERT INTO MEADIABASE (MEDIA_NAME, TYPE) VALUES (?, ?)', \
                                     (self.children[0].value, self.children[1].value))
            await db.commit()
            await db.close()
        
        await interaction.response.send_message(embeds=[embed])

@bot.slash_command(name='add_media', description='Пополнить медиатеку', guild_ids=guild_ids)
async def add_meadia(ctx: discord.ApplicationContext):
    modal = MyModal(title="Оформление медиа")

    await ctx.send_modal(modal)

if __name__ == "__main__":
    bot.run(os.getenv("TOKEN"))