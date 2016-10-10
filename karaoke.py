#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import smallsmilhandler
import sys
import json


def print_elementos(datos):
    elem = ''
    for lista in datos:
        elem = lista[0]
        sublista = lista[1]
        for atributo in sublista:
            elem = elem + "\t" + atributo + "=" + sublista[atributo] + " "
        print(elem + "\n")


if __name__ == "__main__":

    try:
        fichero = sys.argv[1]
    except IndexError:
        sys.exit("Usage: python3 karaoke.py file.smil")

    parser = make_parser()
    cHandler = smallsmilhandler.SmallSMILHandler()
    parser.setContentHandler(cHandler)
    fich = open(sys.argv[1], 'r')
    parser.parse(fich)
    datos = cHandler.get_tags()

    print_elementos(datos)

    fich_json = open('karaoke.json', 'w')
    json.dump(datos, fich_json, sort_keys=True, indent=4, separators=(',', ':'))
    fich_json.close()
