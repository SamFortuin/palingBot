from shortcuts import *
import discord
from discord.ext import commands
from discord.errors import ClientException

def grabToken():
    #grabs token from the txt containing it
    f = open('token.txt','r')
    tokenOut = f.read()
    print('succesfully grabbed token') if tokenOut != None else print('failed to get token')
    f.close()
    return tokenOut
