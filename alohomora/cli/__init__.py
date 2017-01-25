# -*- encoding: utf-8 -*-

import click
# using Fun as alias to help me type short and funny ;)
from alohomora import Alohomora as Fun

@click.command()
@click.option('-s', default=None, help='Collection of letters. ')
@click.option('-w', default=None, help='Word to compare all the letters in it with the already given one. ')
def magic(s, w):
    fun = Fun(s, w)
    flag = fun.magic()
    fmt = 'Yes, "{}" can be created.' if flag else 'No, "{}" cannot be created.'
    print(fmt.format(w))


@click.command()
@click.option('-s', default=None, help='Collection of stupid letters.')
def longest(s):
    fun = Fun(s)
    print(fun.longest())
