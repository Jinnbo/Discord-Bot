import discord
import assetprices
import graphs

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# store token from token.txt
with open('token.txt') as f:
    TOKEN = f.read()


# Initialization
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

# Messages
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

        # Check if ticker is listed
        try:
            price = assetprices.close_price(ticker)
        except:
            print("Ticker not avaiable")
            await message.channel.send(f'{ticker} is not avaiable')
            return

        price = assetprices.close_price(ticker.upper())
        await message.channel.send(f"{ticker.upper()} Price: ${price:.2f}")

    # Sharpe Ratio 
    if message.content.startswith("$sharperatio"):
        
        sr_ticker = msg.split("$sharperatio ",1)[1]

        # Check if ticker is listed
        try:
            price = assetprices.close_price(sr_ticker)
        except:
            print("Ticker not avaiable")
            await message.channel.send(f'{sr_ticker} is not avaiable')
            return

        sharperatio = assetprices.sr(sr_ticker.upper())
        await message.channel.send(f"{sr_ticker.upper()} Sharpe Ratio: {sharperatio:.2f}")

    # Daily Chart
    if message.content.startswith("$dailychart"):
        sr_ticker = msg.split("$dailychart ",1)[1]

        # Check if ticker is listed
        try:
            price = assetprices.close_price(sr_ticker)
        except:
            print("Ticker not avaiable")
            await message.channel.send(f'{sr_ticker} is not avaiable')
            return


        # Message graph in channel
        graphs.daily_graph(sr_ticker)
        await message.channel.send(file=discord.File(f'{sr_ticker}daily.png'))

        # Delete graph
        graphs.deleteGraph(sr_ticker)

    # Weekly Chart
    if message.content.startswith("$weeklychart"):
        sr_ticker = msg.split("$weeklychart ",1)[1]

        # Check if ticker is listed
        try:
            price = assetprices.close_price(sr_ticker)
        except:
            print("Ticker not avaiable")
            await message.channel.send(f'{sr_ticker} is not avaiable')
            return

        # Message graph in channel
        graphs.weekly_graph(sr_ticker)
        await message.channel.send(file=discord.File(f'{sr_ticker}weekly.png'))

        # Delete graph
        graphs.deleteGraph(sr_ticker)

# Run bot with Token from token.txt
client.run(TOKEN)
