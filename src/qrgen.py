# QR Gen by Alexander Abraham.
# Licensed under the MIT license.

import qrcode
import argparse
import colorama
colorama.init()
from qrcode import QRCode
from argparse import ArgumentParser

def version():
    version = '1.0'
    name = 'QR Gen'
    author = 'Alexander Abraham'
    license = 'MIT License'
    print(colorama.Fore.RED + name + ' ' + version + '\n' + 'by ' + author + '\nLicensed under the ' + license + colorama.Back.RESET)

def invalidArgs():
    message = 'Invalid arguments supplied.\nTry the "--help" option.'
    print(colorama.Fore.RED + message + colorama.Back.RESET)

def generator(data, name):
    qr = QRCode(version=2,box_size=10,border=0)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(name)

def cli():
    parser = ArgumentParser()
    parser.add_argument('--fname', help='the file name by qhich to save the generated QR code')
    parser.add_argument('--version', help='displays version info', action='store_true')
    args = parser.parse_args()
    if args.fname:
        data = ''
        confirm = False
        while confirm == False:
            data = input('Type the data for the QR code here: ')
            confirm = input('Are you sure? (y/n) ')
            if confirm == 'y':
                confirm = True
            else:
                confirm = False
        try:
            generator(data, args.fname)
        except Exception as error:
            print(str(error))
    elif args.version:
        version()
    else:
        invalidArgs()

def main():
    cli()

if __name__ == '__main__':
    main()
