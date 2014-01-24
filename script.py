#!/usr/bin/python
# -*- coding: utf-8 -*-

#Se debe correr como root
import fileinput
import random
from random import randint
from random import choice
import os
import pwd
import crypt
import string
from string import lowercase

#Funcion que dado un numero, devuelve un numero aleatorio de n cifras
def random_N_digitos(n):
	rango_ini = 10**(n-1)
	rango_fin = (10**n)-1
	return randint(rango_ini, rango_fin)

#Se crea el directorio principal
os.system('mkdir Taquirule; chmod 755 -R Taquirule')

#Se crean los subdirectorios principales
os.system('mkdir Taquirule/templo_A')   #Para este necesitas la mascara de AA 
os.system('mkdir Taquirule/templo_E')   #Para este necesitas la mascara de SB
os.system('mkdir Taquirule/templo_F')   #Para este necesitas la mascara de EP
os.system('mkdir Taquirule/templo_ET')  #Para este necesitas la mascara de GR
os.system('mkdir Taquirule/templo_MAC') #Para este... Para este... necesitas la mascara de EAS

print 'Se crea Taquirule y los templos'

#Se encriptan las claves de los usuario 
aa_passwd = crypt.crypt('chileabro','22')
sb_passwd = crypt.crypt('galleta?','22')
ep_passwd = crypt.crypt('comprooro','22')
gr_passwd = crypt.crypt('palperreo','22')
eas_passwd = crypt.crypt('soyeas','22')

#Se crean los usuarios. Estos usuarios tendran una pista en el home
#para el ultimo comando del Templo 
os.system('useradd -s /bin/bash -p '+aa_passwd +' -m AA')
os.system('useradd -s /bin/bash -p '+sb_passwd+' -m SB')
os.system('useradd -s /bin/bash -p '+ep_passwd+' -m EP')
os.system('useradd -s /bin/bash -p '+gr_passwd+' -m GR')
os.system('useradd -s /bin/bash -p '+eas_passwd+' -m EAS')

carpetas=(os.popen('ls Taquirule')).readlines()
print 'Se crean los usuarios'

#Se leen palabras de un diccionaro para crear las carpetas crap
archivo = open('/etc/dictionaries-common/words','r')
lineas = archivo.readlines()
respaldo = lineas
archivo.close()

#Se les hace suffle para que salga aleatoria mente
random.shuffle(lineas)

#Se escribe archivos basura en cada carpeta

for f in carpetas:
	for i in range(777):
		archivo = open("Taquirule/"+f.strip("\n")+"/"+(((lineas.pop()).lower()).replace("'","J")).strip("\n"),'w',0)
		archivo.close()

subcarpetas=[]
        
#ESCRIBO CARPETAS BASURA EN CADA CARPETA
for f in carpetas:
    for i in range(15):
        aux = "_"+(((lineas.pop()).upper()).replace("'","F")).strip("\n")
        aux2 = f.strip("\n")
        subcarpetas += [(aux2,aux)]
        os.system("mkdir Taquirule/"+aux2+"/"+aux+" 2> /dev/null && touch Taquirule/"+aux2+"/"+aux+"/##NOOO_AQUI_NO_ES"+aux+" && chmod +x Taquirule/"+aux2+"/"+aux+"/##NOOO_AQUI_NO_ES"+aux)
        

print 'Se llenan los templos con carpetas y archivos basura'


#templo_A
#Se garantiza que no existan estos archivos
os.system('find Taquirule/templo_A -name _ZO | xargs rm -rf')
os.system('find Taquirule/templo_A -name _DE | xargs rm -rf')
os.system('find Taquirule/templo_A -name link | xargs rm -rf')

os.system('mkdir -p Taquirule/templo_A/_ZO/_RA')
os.system('mkdir -p Taquirule/templo_A/_DE/_KU')
os.system('touch Taquirule/templo_A/_ZO/##PONME_TODO')
os.system('touch Taquirule/templo_A/_ZO/_RA/##ESO_PA_LANTE')
os.system('touch Taquirule/templo_A/_DE/##PONME_TODO')
os.system('touch Taquirule/templo_A/_DE/_KU/##ESO_PA_LANTE')

os.system('touch Taquirule/templo_A/link')
lineas = respaldo
for i in range(50):
	os.system('echo "'+(((lineas.pop()).lower()).replace("'",":")).strip("\n")+'" >> Taquirule/templo_A/link')

for i in range(207):
	str0 = "".join(choice(lowercase) for j in range(45))
	os.system('echo ":'+str(random_N_digitos(4))+str0+'" >> Taquirule/templo_A/link')
os.system('echo ":5432accb seteacabaeltiempo" >> Taquirule/templo_A/link')

for i in range(207):
	str0 = "".join(choice(lowercase) for j in range(30))
	os.system('echo ":'+str(random_N_digitos(4))+str0+'" >> Taquirule/templo_A/link')
os.system('echo ":1322eccb acabasdeconseguirlaclaveparaSB" >> Taquirule/templo_A/link')
for i in range(207):
	str0 = "".join(choice(lowercase) for j in range(34))
	os.system('echo ":'+str(random_N_digitos(4))+str0+'" >> Taquirule/templo_A/link')
for i in range(307):
	str0 = "".join(choice(lowercase) for j in range(24))
	os.system('echo ":'+str(random_N_digitos(4))+str0+'" >> Taquirule/templo_A/link')
os.system('echo ":1352eccba aNavilegustanlasgalletas" >> Taquirule/templo_A/link')
for i in range(300):
	str0 = "".join(choice(lowercase) for j in range(27))
	os.system('echo ":'+str(random_N_digitos(4))+str0+'" >> Taquirule/templo_A/link')
for i in range(50):
	os.system('echo "'+(((lineas.pop()).lower()).replace("'",":")).strip("\n")+'" >> Taquirule/templo_A/link')

#archivo random que tendra 30 lineas
os.system('rm -rf Taquirule/templo_A/gemelos')
os.system('touch Taquirule/templo_A/gemelos')
for i in range(30):
    os.system("echo ola bale >> Taquirule/templo_A/gemelos")
#Colocandole 30K a un archivo
os.system('rm -rf Taquirule/templo_A/luna')
os.system('touch Taquirule/templo_A/luna')
for i in range(9999):
    os.system("echo aa >> Taquirule/templo_A/luna")
print '---Cosas necesarias para templo_A: OK'
#Fin del templo AA


#Cosas de la pregunta 7
masks=['keaton','skull','spooky','bunny','truth','goron','zora', 'gerudo',\
	       'fiercedeity','blast','brenen', 'circus']
words_from_masks = []
for i in range(1,300):
	for m in masks:	
		num = i % 5
        if num != 0:
		words_from_masks.append(m + str(random_N_digitos(int(num))))

words_from_masks = list(set(words_from_masks))

for w in words_from_masks:
    	os.system('echo '+ w + '>> a1')

random.shuffle(words_from_masks)        
for w in words_from_masks:
    	os.system('echo '+ w + '>> a2')

palabra_distinta= 'CANALIZAR'
os.system('echo '+ palabra_distinta + '>> a2')




#Templo de SB
os.system('rm -rf Taquirule/templo_E/tael')
os.system('touch Taquirule/templo_E/tael')
for i in range(100):
	str0 = "".join(choice(lowercase) for j in range(6))
	os.system('echo '+str0+' >> Taquirule/templo_E/tael')
os.system('echo majora >> Taquirule/templo_E/tael'     #Essta es la linea del medio
for i in range(100):
	str0 = "".join(choice(lowercase) for j in range(6))
	os.system('echo '+str0+' >> Taquirule/templo_E/tael')


#Fin del templo SB

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
#os.system('find Taquirule -name taquilla | xargs rm -rf')
#os.system('find Taquirule -name mac | xargs rm -rf')
#os.system('find Taquirule -name vaca | xargs rm -rf')
#os.system('find Taquirule -name soy | xargs rm -rf')
#os.system('find Taquirule -name servidores | xargs rm -rf')
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
