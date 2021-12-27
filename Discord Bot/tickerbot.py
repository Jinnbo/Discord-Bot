import discord
import assetprices
import graphs

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content.lower()

    if message.content.startswith("$price"):
        ticker = msg.split("$price ",1)[1]
        price = assetprices.close_price(ticker.upper())
        await message.channel.send(f"{ticker.upper()} Price: ${price:.2f}")

    if message.content.startswith("$sharperatio"):
        sr_ticker = msg.split("$sharperatio ",1)[1]
        sharperatio = assetprices.sr(sr_ticker.upper())
        await message.channel.send(f"{sr_ticker.upper()} Sharpe Ratio: {sharperatio:.2f}")

    if message.content.startswith("$history"):
        sr_ticker = msg.split("$history ",1)[1]
        history = assetprices.ticker_detail(sr_ticker.upper())
        await message.channel.send(f"{history}")

    if message.content.startswith("$dailychart"):
        sr_ticker = msg.split("$dailychart ",1)[1]
        graphs.daily_graph(sr_ticker)
        await message.channel.send(file=discord.File(f'{sr_ticker}daily.png'))

    if message.content.startswith("$weeklychart"):
        sr_ticker = msg.split("$weeklychart ",1)[1]
        graphs.weekly_graph(sr_ticker)
        await message.channel.send(file=discord.File(f'{sr_ticker}weekly.png'))

    if message.content.startswith("$alert"):
        alert = msg.split(" ")
        alert_ticker = alert[1]
        alert_price = alert[2]

        await message.channel.send(f"{alert_ticker.upper()} alert created for ${alert_price}")


    if message.content.startswith("$commands"):
        await message.channel.send(f"$price [ticker] Shows closing price "
                                   f"\n$sharperatio [ticker] Shows Sharpe Ratio "
                                   f"\n$history [ticker] Shows history"
                                   f"\n$dailychart [ticker] Shows daily timeframe chart"
                                   f"\n$weeklychart [ticker] Shows weekly timeframe chart"
                                   )




client.run('ODIxMjMyNjE0MjQ5NDYzODI5.YFAueQ.CYKjtXlMGhn7jVzbMtR3fSbHDdc')
