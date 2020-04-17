# coding: utf-8
import click
from progress.bar import ShadyBar

@click.command()
@click.argument('input_file', type=click.File('rb'))
def f(input_file):
    """ 
        XORing 32 bit raw data: [i] ^ [i+1], 
        where i is 4 byte data  
    """

    key = bytearray([0x00,0x00,0x00,0x00])
    l = len(key)
    bytes = bytearray(input_file.read())
    # for i in range(0,len(bytes)):
    #     key[i % l] ^= bytes[i]

    # with progress bar (much slower)
    with ShadyBar('Calculating...', suffix='%(percent)d%%', max=len(bytes)) as bar:
        for i in range(0,len(bytes)):
            key[i % l] ^= bytes[i]
            bar.next()
    bar.finish()

    click.secho('XOR value of file is ', nl=False)  
    click.secho('0x' + key.hex().upper(), fg="green")
        