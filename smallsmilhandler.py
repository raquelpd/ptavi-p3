#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):

        self.etiquetas = []

        self.atributos = {'root-layout': ['width', 'height', 'background-color'],
                          'region': ['id', 'top', 'bottom', 'left', 'right'],
                          'img': ['src', 'region', 'begin', 'dur'],
                          'audio': ['src', 'begin', 'dur'],
                          'textstream': ['src', 'region']}

    def startElement(self, name, attrs):

        if name in self.atributos:
            dicc = {}
            for atributo in self.atributos[name]:
                dicc[atributo] = attrs.get(atributo, "")
            self.etiquetas.append([name, dicc])

    def get_tags(self):

        return self.etiquetas


if __name__ == "__main__":

    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
    datos = cHandler.get_tags()
    print(datos)
