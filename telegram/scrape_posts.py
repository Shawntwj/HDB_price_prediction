from telethon.sync import TelegramClient
import pandas as pd

name = 'anon' 
api_id = 15623085 
api_hash = 'a57a2e8ffa94759fc13f68cd0e4cc1d1' 

#Test Group ID: 662713844
#BTO Mega Channel ID: 1001167169561
#Homeowners SG Channel ID: 1001215498593
#Stacked Homes Channel: 1001320267392

chat = 1001320267392

data = [] # stores all our data in the format SENDER_ID, MSG

async def scrape():
    async with TelegramClient(name, api_id, api_hash) as client:
        async for message in client.iter_messages(chat, limit=100):
            data.append([f'{message.date.day}/{message.date.month}/{message.date.year}', message.text])
    client.log_out()
        
scrape()

df = pd.DataFrame(data, columns=['DATE', 'MESSAGE']) # creates a new dataframe

df.to_csv('tg_messages.csv', encoding='utf-8-sig') # save to a CSV file

