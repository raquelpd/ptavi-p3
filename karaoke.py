#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler
import smallsmilhandler
import sys
import json
from urllib.request import urlretrieve


class KaraokeLocal(SmallSMILHandler):

    def __init__(self, fich):
        parser = make_parser()
        cHandler = smallsmilhandler.SmallSMILHandler()
        parser.setContentHandler(cHandler)
        fich = open(sys.argv[1], 'r')
        parser.parse(fich)
        self.datos = cHandler.get_tags()

    def __str__(self):
        elem = ''
        for lista in self.datos:
            elem = lista[0]
            sublista = lista[1]
            for atributo in sublista:
                elem = elem + "\t" + atributo + "=" + sublista[atributo] + " "
            print(elem + "\n")
        return(elem)

    def to_json(self, fich, new_fich=""):
        if new_fich == "":
            nf = fich[:fich.find('.')]
        else:
            nf = new_fich
        fich_json = open(nf + '.json', 'w')
        json.dump(self.datos, fich_json, sort_keys=True, indent=4, separators=(',', ':'))
        fich_json.close()

    def do_local(self):
        for lista in self.datos:
            sublista = lista[1]
            for atributo in sublista:
                if sublista[atributo][:7] == "http://":
                    urlretrieve(sublista[atributo])
                    print(sublista[atributo])
                    url = sublista[atributo].split('/')
                    sublista[atributo] = url[-1]
                    print(sublista[atributo])

if __name__ == "__main__":

    try:
        fich = sys.argv[1]
        karaoke = KaraokeLocal(fich)
        print(karaoke)
        karaoke.do_local()
        karaoke.to_json(fich)
        print(karaoke)

    except IndexError:
        sys.exit("Usage: python3 karaoke.py file.smil")
