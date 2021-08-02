import discord
from discord.ext import commands

client = commands.Bot( command_prefix = '$' )


@client.event

async def on_ready():
	print( 'BOT on' )

@client.command( pass_context = True )

async def Start( ctx ):
	author = ctx.message.author
	await ctx.send( f'Привет { author.mention } ! Я запустился и готов слушать ваши укозания сир...' )


@client.command( pass_context = True )
@client.event
@commands.has_permissions( administrator = True )
async def p( ctx , x: int ):
	author = ctx.message.author
	money = open( 'Am.txt', 'r' ).readline()
	money = int (money)
	money = sum([x,money])
	f = open('Am.txt', 'w')
	f.write(str(money))
	#await ctx.channel.purge( limit = 4 )

	await ctx.send( f'В козне после вашего добавления: { money }$' )

@client.command( pass_context = True )
@client.event
@commands.has_permissions( administrator = True )
async def m( ctx , x: int ):
	author = ctx.message.author
	money = open( 'Am.txt', 'r' ).readline()
	money = int (money)
	money = money - x
	f = open('Am.txt', 'w')
	f.write(str(money))
	#await ctx.channel.purge( limit = 4 )

	await ctx.send( f'В козне после вашего взятия: { money }$' )

@client.command( pass_context = True )
@client.event

async def s( ctx ):
	author = ctx.message.author
	money = open( 'Am.txt', 'r' ).readline()
	money = int (money)
	#await ctx.channel.purge( limit = 4 )

	await ctx.send( f'Сумма: { money }$' )



# Connect

token = open( 'token.txt', 'r' ).readline()

client.run ( token )