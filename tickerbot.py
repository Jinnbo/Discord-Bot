# This example requires the 'message_content' intent.

import discord
import assetprices
import graphs

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):

    # Ignore messages from the yourself (bot)
    if message.author == client.user:
        return

    msg = message.content.lower()

    # Commands
    if message.content.startswith("$commands"):
        await message.channel.send(f"$price [ticker] Shows closing price "
                                   f"\n$sharperatio [ticker] Shows Sharpe Ratio "
                                   f"\n$history [ticker] Shows history"
                                   f"\n$dailychart [ticker] Shows daily timeframe chart"
                                   f"\n$weeklychart [ticker] Shows weekly timeframe chart"
                                   )

    # Current price
    if message.content.startswith("$price"):
        ticker = msg.split("$price ",1)[1]
        price = assetprices.close_price(ticker.upper())
        await message.channel.send(f"{ticker.upper()} Price: ${price:.2f}")

    # Sharpe Ratio 
    if message.content.startswith("$sharperatio"):
        sr_ticker = msg.split("$sharperatio ",1)[1]
        sharperatio = assetprices.sr(sr_ticker.upper())
        await message.channel.send(f"{sr_ticker.upper()} Sharpe Ratio: {sharperatio:.2f}")

    # Daily Chart
    if message.content.startswith("$dailychart"):
        sr_ticker = msg.split("$dailychart ",1)[1]

        # Message graph
        graphs.daily_graph(sr_ticker)
        await message.channel.send(file=discord.File(f'{sr_ticker}daily.png'))

        # Delete graph

    # Weekly Chart
    if message.content.startswith("$weeklychart"):
        sr_ticker = msg.split("$weeklychart ",1)[1]
        graphs.weekly_graph(sr_ticker)
        await message.channel.send(file=discord.File(f'{sr_ticker}weekly.png'))





client.run('ODIxMjMyNjE0MjQ5NDYzODI5.YFAueQ.CYKjtXlMGhn7jVzbMtR3fSbHDdc')

