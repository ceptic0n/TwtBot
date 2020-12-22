import tweepy
import time
import discord
import random
from quotes import *
from badWords import *
from discord.ext import commands

client = commands.Bot(command_prefix='=')


#keys access for the twitter bot
auth = tweepy.OAuthHandler("VmEQC9aqQGFXBDDEJu6Q1vRW3", "1ytaKdiPcf4ouLTk76PxZdKouW3DATj15rRJ4sYXJK3oS401VR")
auth.set_access_token("1282720174676688896-SktSgWRd6gcqyHkH0iJ5Yh1g1tFDjb", "O7E4WTgExi7q9lQtrXxPiTYWfB6jf1QG3VObyoKrjk5Ek")
api = tweepy.API(auth)

#current_Servers = len(client.servers)

client.remove_command('help')

# Event that states in the console that bot is ready
@client.event
async def on_ready():
    print("Bot is ready")
# print("Currently active in " + current_Servers + " servers")

@client.command()
async def poggers(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/725104269673365574/744763641894797392/video0.mp4")

@client.command()
async def ari(ctx):
    await ctx.send("ari is so cool, sub to her patreon <https://www.patreon.com/user/posts?u=29078712&filters%5Btag%5D=cute%20girls>")

@client.command()
async def pix(ctx):
    await ctx.send("good vibes only ty - pixie")

@client.command()
async def sam(ctx):
    await ctx.send("pls put on a shirt")

@client.command()
async def jenna(ctx):
    await ctx.send("1  this bitch is so annoying, she needa give it up")
    time.sleep(1)
    await ctx.send("2 her relationship with sam, that shit so corrupt")
    time.sleep(1)
    await ctx.send("3 I see her playin the sims all day")
    time.sleep(1)
    await ctx.send("4 why are all her sims so gay")

@client.command()
async def vic(ctx):
    await ctx.send("too good for this world!")

@client.command()
async def dawn(ctx):
    await ctx.send("my b")

@client.command()
async def piku(ctx):
    await ctx.send("muah :sparkles: ")

@client.command()
async def surprise(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/738847181057818706/745764446311415909/743290805564735539.gif")

@client.command()
async def bee(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/690944063888687114/736602866235473930/beemovie.mp4")

@client.command()
async def shrek(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/652269241730465805/745844802112847922/shreksmaller1new.mp4")

@client.command()
async def twoMad (ctx):
    await ctx.send("bababooey")

@client.command()
async def mmm(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/701926295222878288/752037621689090108/image0.png")

@client.command()
async def jihye(ctx):
    await ctx.send("best dancer :relieved:")

@client.command()
async def ona(ctx):
    await ctx.send("peng asf")

@client.command()
async def ket(ctx):
    await ctx.send("indecisive 6’5 swoll non binary hermaphrodite indian gamer")

@client.command()
async def alex(ctx):
    await ctx.send("i'm not racist")
    time.sleep(3)
    await ctx.send("but")

@client.command()
async def whoSmart(ctx):
	await ctx.send("YA BOI NATHAN YAYAYAYAYAYA")

#WHERE THE DEMONS GO PERSONAL COMMANDS

#Takes custom quotes from quotes.py and returns a random quote
def getQuote(userQuote):
	rand = random.randint(0, len(userQuote) -1)
	quote = userQuote[rand]
	return quote

@client.command()
async def theavy(ctx):
	await ctx.send(getQuote(theavyQuotes))

@client.command()
async def liyah(ctx):
        await ctx.send(getQuote(liyahQuotes))

@client.command()
async def alexis(ctx):
	await ctx.send(getQuote(alexisQuotes))

@client.command() 
async def gus(ctx):
	await ctx.send(getQuote(gusQuotes))

@client.command()
async def jackie(ctx):
	await ctx.send(getQuote(jackieQuotes))

@client.command()
async def himay(ctx):
	await ctx.send(getQuote(jaimeQuotes))

@client.command()
async def carlos(ctx):
	await ctx.send(getQuote(carlosQuotes)) 

@client.command()
async def rohi(ctx):
	await ctx.send(getQuote(rohiQuotes))

@client.command()
async def ritik(ctx):
	await ctx.send(getQuote(ritikQuotes))

@client.command()
async def nathan(ctx):
	await ctx.send(getQuote(nathanQuotes))

#WTDG Special Commands

@client.command()
async def gusPR(ctx):
        gusPR = random.randint(1, 10)
        if gusPR < 8:
                gusPR = random.randint(1, 150)
                await ctx.send("gus can only bench " + str(gusPR) + " lbs")
        elif gusPR >= 8:
                gusPR = random.randint(150, 235)
                await ctx.send("gus can only bench " + str(gusPR) + " lbs")

@client.command()
async def ignored(ctx):
	await ctx.send("alexis")
	time.sleep(1)
	await ctx.send("aaaLEXISSSSS")
	time.sleep(2)
	await ctx.send("UHHHLEXISSSSS")
	time.sleep(1)
	await ctx.send("...")
	time.sleep(1)
	await ctx.send("||well fuck me and my glow stars i guess||")

#TwtBot main function

@client.command()
async def twt(ctx, *, input):
    try:
        tweet, signature = input.split('-')
        tweetLength = tweet + signature
        if len(tweetLength) > 277:
            await ctx.send("Error! Tweet too long")
        else:
            censored_tweet = censor(tweet)
            censored_signature = censor(signature)
            api.update_status(censored_tweet + " - " + censored_signature)
            await ctx.send("Tweet Sent! <https://www.twitter.com/DisTweet3>")
    except:
        await ctx.send("Error! Tweet - Signature")

def censor(text):
    badwords = arrBad
    sentence = text.split()
    for index, word in enumerate(sentence):
        if any(badword in word for badword in badwords):
            sentence[index] = "".join(['*' if c.isalpha() else c for c in word])
    return " ".join(sentence)

#token for discord bot
client.run("NzMyMjk0NDE4NDA0NDc0ODgx.Xw0dAQ.dbBBJ73yv-QoA8nA7HgttmYEEng")
