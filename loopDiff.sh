#!/bin/bash

# Compara todos os arquivos entre os diretorios DIR_PROD e DIR_HOMOL e cria o log das diferencas dentro de DIR_RESULTADO
# Ta Feio pra caralho, mas me quebrou um galho!

DIR_PROD=/Users/rafael/Documents/diretorioX
DIR_HOMOL=/Users/rafael/Documents/diretorioY
DIR_RESULTADO=/Users/rafael/Documents/resultado_diff

ls $DIR_PROD > diretorios.txt

while read DIRETORIO
do
  diff -r $DIR_PROD/$DIRETORIO $DIR_HOMOL/$DIRETORIO > $DIR_RESULTADO/$DIRETORIO.log
done < diretorios.txt
