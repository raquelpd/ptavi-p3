#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import smallsmilhandler
import sys

#def __init__(Self, fichero):
#    
#    parser = make_parser()
#    cHandler = smallsmilhandler.SmallSMILHandler()
#    parser.setContentHandler(cHandler)
#    parser.parse(fich)
#    datos = cHandler.get_tags()

def elems(datos):
    elem =''
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
        
    elems(datos)
     

   
   
