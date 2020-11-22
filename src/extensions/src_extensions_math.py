import discord
from discord.ext import commands
import asyncpg
import math # this is the most important one for the bot
from datetime import datetime

# Class
class math:
    """Politics and war related commands"""
    def __init__(self, bot):
        self.bot = bot
        self.cas = bot.cardinal

    @commands.command(aliases=["add"], brief="Adds the entered values")
    async def addition(self, ctx, *, args):
        """
        Adds the entered values, can currently only handle two values.

        Usage: (pre)addition [numb 1] [numb 2]
        """
        total = 0
        numbs = []
        args = args.split(" ")
        for arg in args:
            numbs.append(f"{float(arg):,.2f}")
            total += float(arg)
        embed = discord.Embed(
                title="Math: Addition",
                color=self.cas.Utils.randColour()
            )
        embed.add_field(name="Values added", value=", ".join(numbs))
        embed.add_field(name="Total", value=total)
        embed.set_footer(text=f'Info Called by {ctx.author.name}#{ctx.author.discriminator} at {datetime.now().date()}', icon_url=ctx.author.avatar_url_as(size=256))
        await ctx.send(embed=embed)

    @commands.command(aliases=["sub"], brief="Does subtraction")
    async def subtraction(self, ctx, *, args):
        """
        Subtracts the entered values, can currently only handle two values.

        Usage: (pre)subtraction [numb 1] [numb 2]
        """
        total = 0
        numbs = []
        args = args.split(" ")
        for arg in args:
            numbs.append(f"{float(arg):,.2f}")
            total += float(arg)
        embed = discord.Embed(
                title="Math: Subtraction",
                color=self.cas.Utils.randColour()
            )
        embed.add_field(name="Values subtracted", value=", ".join(numbs))
        embed.add_field(name="Total", value=total)
        embed.set_footer(text=f'Info Called by {ctx.author.name}#{ctx.author.discriminator} at {datetime.now().date()}', icon_url=ctx.author.avatar_url_as(size=256))
        await ctx.send(embed=embed)

    @commands.command(aliases=["mult"], brief="Does multiplication")
    async def multiplication(self, ctx, a:float, b:float):
        """
        Multiplies the entered values, can currently only handle two values.

        Usage: (pre)multiplication [numb 1] [multiplier]
        """
        c = a / b
        embed = discord.embed(
            title="Math: Multiplication",
            color=self.cas.Utils.randColour()
        )
        embed.add_field(name="Original Value", values=a, inline=False)
        embed.add_field(name="Multiplier", values=b, inline=False)
        embed.add_field(name="Total", value=f"{a * b:,.2f}")
        embed.set_footer(text=f'Info Called by {ctx.author.name}#{ctx.author.discriminator} at {datetime.now().date()}', icon_url=ctx.author.avatar_url_as(size=256))
        await ctx.send(embed=embed)

    @commands.command(aliases=["div"], brief="Does division")
    async def division(self, ctx, a:float, b:float):
        """
        Divides the entered values, can currently only handle two values.

        Usage: (pre)division [numb 1] [divisor]
        """
        embed = discord.embed(
            title="Math: Division",
            color=self.cas.Utils.randColour()
        )
        embed.add_field(name="Original Value", values=a, inline=False)
        embed.add_field(name="Divisor", values=b, inline=False)
        embed.add_field(name="Total", value=f"{a / b:,.2f}")
        embed.set_footer(text=f'Info Called by {ctx.author.name}#{ctx.author.discriminator} at {datetime.now().date()}', icon_url=ctx.author.avatar_url_as(size=256))
        await ctx.send(embed=embed)

    @commands.command(aliases=["pow"], brief="Returns the power of the first value based on the second.")
    async def power(self, ctx, a:float, b:float):
        """
        Returned the result of ``numb 1`` to the power of ``numb 2``, can currently only handle two values.

        Usage: (pre)division [numb 1] [numb 2]
        """
        c = a ** b
        embed = discord.embed(
            title="Math: Power",
            color=self.cas.Utils.randColour()
        )
        await ctx.send("Nothing yet")

    @commands.command(aliases=["meval"], brief="Evaluates the equation provided")
    async def mevaluation(self, ctx, *equation):
        """
        Evaluates the passed equation

        Usage: (pre)mevaluation [equation]
        """
        await ctx.send("Nothing yet")

def setup(bot):
    bot.add_cog(math(bot))
