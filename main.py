import os
import random
import requests
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True 
    
bot = commands.Bot(command_prefix='#', intents=intents)

@bot.event
async def on_ready():
    print(f'Estamos logados como {bot.user}')

@bot.command()
async def reciclar(ctx):
    print("Ideias: Garrafa Pet = Vaso Para Plantas, Pneu = Banco, Caixa De Papelão = Brinquedos Grandes Como Avião, Carro...")

@bot.command()
async def poluicao(ctx):
    print("Coisas Que Poluem Seriamente A Natureza: Motor, Combustível, Plástico, Lixo Em Terra E Rio...")

@bot.command()
async def lixo(ctx):
    print("Lixo Que Passa Despercebido: Jogar Lixo No Chão Durante Uma Festa, Excesso de plástico comprado...")
