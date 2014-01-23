#!/usr/bin/python
# -*- coding: utf-8 -*-

import fileinput
import random
import os


#CREANDO LOS DIRECTORIOS DE LA TAREA
os.system('mkdir Taquirule; chmod 755 -R Taquirule')

for i in range(4):
    os.system('mkdir TAREA/p'+str(i))

#carpetas=(os.popen('ls TAREA')).readlines()
#
##ME LEO PALABRAS DE UN DICCIONARIO PARA CREAR ARCHIVOS Y CARPETAS BASURA
#archivo = open('/etc/dictionaries-common/words','r')
#lineas = archivo.readlines()
#archivo.close()
#
##ME LAS SHUFFLEO PARA QUE SALGAN ALEATORIAMENTE
#random.shuffle(lineas)
#
##ESCRIBO ARCHIVOS BASURA EN CADA CARPETA
#for h in carpetas:
#    for i in range(777):
#
#        archivo=open("TAREA/"+h.strip("\n")+"/"+(((lineas.pop()).lower()).replace("'","H")).strip("\n"),'w',0)
#        archivo.close()
#
#
#subcarpetas=[]
#        
##print carpetas[0].strip("\n")
##ESCRIBO CARPETAS BASURA EN CADA CARPETA
#for h in carpetas:
#    for i in range(15):
#        aux="_"+(((lineas.pop()).upper()).replace("'","U")).strip("\n")
#        aux2=h.strip("\n")
#        subcarpetas+=[(aux2,aux)]
#        os.system("mkdir TAREA/"+aux2+"/"+aux+" 2> /dev/null && touch TAREA/"+aux2+"/"+aux+"/##ESTE_NO_ES"+aux+" && chmod +x TAREA/"+aux2+"/"+aux+"/##ESTE_NO_ES"+aux)
#        
#
##METER EL EQUIPO DE LODUDO en p1
#lodudo=["Lezama","Giuseppe","Jon","Yoshi","Erick","Isaac","Fundaro","Javier"]
#lodudo2=[".O",".d",".u",".D",".o",".L"]
#
#for i in lodudo+lodudo2:
#    os.system("touch TAREA/p0/"+i)
#
#for i in range(6):
#    os.system('touch --date="2011-10-2"'+str(i)+" TAREA/p0/"+lodudo2[i])
#
#
#
##METO PREGUNTAS GAY EN P1
#os.system('touch TAREA/p0/"^alexandra es la profesora encargada del LDAC"')
#os.system('touch TAREA/p0/"^violetta es la ingeniero de mantenimiento del LAB. F"')
#os.system('touch TAREA/p0/"^Saruman fue el antiguo jefe del LAB. F (Hoy en dia es Carolina Chang)"')
#
##COLOCANDO DIRECTORIOS Q PIDIO SOFIA
#os.system('mkdir TAREA/p0/vaca; mkdir TAREA/p0/vaca/pollito; mkdir TAREA/p2/soy; mkdir TAREA/p2/soy/la; mkdir TAREA/p2/soy/la/comadreja')
#
##GARANTIZANDO QUE CIERTOS DIRECTORIOS NO SE CREARON POR AZAR DESDE EL DICCIONARIO
#os.system('find TAREA -name taquilla | xargs rm -rf')
#os.system('find TAREA -name mac | xargs rm -rf')
#os.system('find TAREA -name vaca | xargs rm -rf')
#os.system('find TAREA -name soy | xargs rm -rf')
#os.system('find TAREA -name servidores | xargs rm -rf')
#
#
#
##METIENDO COSAS EN UN DIRECTORIO RANDOM
#dir="TAREA/"+(subcarpetas[0])[0]+"/"+(subcarpetas[0])[1]
#os.system("touch "+dir+"/taquilla")
#
##COLOCANDO EN DICHO ARCHIVO LAS BENDITAS 30 LINEAS
#for i in range(30):
#    os.system("echo a >> "+dir+"/taquilla")
#
##CREANDO OTRO DIR Q PIDIO SOFIA
#os.system("mkdir TAREA/p0/mac")
#
##COLOCANDOLE CASI 30K DE PURO SEXO Y ALCOHOL A UN ARCHIVO
#for i in range(9999):
#    os.system("echo aa >> TAREA/p0/mac/30k")
#
##COLOCANDOLE LA GOTA QUE DERRAMO EL VASO AL ARCHIVO ANTERIOR
#os.system("echo SB >> TAREA/p0/mac/30k")
#
##COLOCANDO UN ARCHIVO EJECUTABLE CON UN PATRON DADO QUE REVELA QUIEN TRAJO EL TREN DE CHOCOLATE AL MAC
#os.system('touch TAREA/p3/##CH_fue_quien_trajo_el_tren_de_chocolate_al_mac && chmod +x TAREA/p3/##CH_fue_quien_trajo_el_tren_de_chocolate_al_mac')
#
#
##LLENANDO EL ARCHIVO DE JON
#servidores=["PISCIS","ADVERICK","HAGEN","CANCER","MIME","LEO","VIRGO","CAPRICORNIO","GHOST","PIKACHU"]
#
#for i in range(89):
#    random.shuffle(servidores)
#    os.system("echo "+servidores[0]+" >> TAREA/p2/servidores")
#
#os.system("echo PISCIS >> TAREA/p2/servidores")
#
#for i in range(120):
#    random.shuffle(servidores)
#    os.system("echo "+servidores[0]+" >> TAREA/p2/servidores")
#
#
#os.system("mkdir TAREA/p3/nolee && cp -R TAREA/p2 TAREA/p3/nolee && man ps >> TAREA/p3/nolee/ps && chmod 000 TAREA/p3/nolee")
#
#text1="Un elder, es como una vaina loca que te lleva a la gloria"
#text2="Un elder, es como windows pero que no es chimbo"
#text3="Un elder, es como chuck nurris cuando estaba chiquito"
#text4="Un elder, es como novich pero sin que te clave en lenguajes"
#text5="Un elder, puede estar en japon, en suecia o viviendo en tu misma ciudad"
#text6="Un elder, puede ser un borrachito chevere o un activista politico"
#text7="Un elder puede hacerte imaginar que tu no eres tu, sino que eres tu barba o shakira"
#text8='"Un elder es (para dejar de jalar tanta bola) un ex-miembro del mac que se graduo siendo parte del mac y que dejo una marca en nuestra historia"'
#
#os.system("touch TAREA/leeteste")
#for i in ["TAREA/p0/elder1","TAREA/p0/elder2"]:
#    os.system("echo "+i+" >> TAREA/leeteste")
#    os.system("touch "+i)
#    
#
#for i in [text1,text2,text3,text4]:
#    os.system("echo "+i+" >> TAREA/p0/elder1")
#
#for i in [text5,text6,text7,text8]:
#    os.system("echo "+i+" >> TAREA/p0/elder2")
#    
#
#
#
#
#
#
#
