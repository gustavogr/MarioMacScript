#!/usr/bin/python
# -*- coding: utf-8 -*-

#Se debe correr como root
import itertools
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

print '---Se carga el templo_A'
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
respaldo_wfms = words_from_masks


#Templo_E
os.system('rm -rf Taquirule/templo_E/tatl')
os.system('touch Taquirule/templo_E/tatl')
for i in range(99):
	str0 = "".join(choice(lowercase) for j in range(6))
	os.system('echo '+str0+' >> Taquirule/templo_E/tatl')
os.system('echo majora >> Taquirule/templo_E/tatl')     #Essta es la linea del medio
for i in range(100):
	str0 = "".join(choice(lowercase) for j in range(6))
	os.system('echo '+str0+' >> Taquirule/templo_E/tatl')


os.system('rm -rf Taquirule/templo_E/tael')
os.system('cp Taquirule/templo_E/tatl Taquirule/templo_E/tael')
os.system('chmod 000 Taquirule/templo_E/tael') 

#Archivo en el que deberan mostrar el contenido de los archivos que esten
#contenidos en el 

os.system('rm -rf Taquirule/templo_E/epona')
os.system('touch Taquirule/templo_E/epona')

for w in words_from_masks:
	os.system('echo '+ w + ' >> Taquirule/templo_E/epona')	
os.system('echo great_fairy >> Taquirule/templo_E/epona')
for i in range(800):
	os.system('echo "'+(((lineas.pop()).lower()).replace("'",":")).strip("\n")+'" >> Taquirule/templo_E/epona')
os.system('touch Taquirule/templo_E/great_fairy')
os.system('echo "Te faltan mas hadas" >> Taquirule/templo_E/great_fairy') 

#Problema de _TINGLES
os.system('rm -rf Taquirule/templo_E/_TINGLES')
os.system('mkdir Taquirule/templo_E/_TINGLES')
zelda = 'zelda'
zelda_l = map(''.join, itertools.product(*zip(zelda.upper(), zelda.lower())))
dir_zelda = ['_THE','_LEGEND','_OF','_EAS','_MAJORAS','_MAC']

for z in zelda_l:  #Se mina todo el directorio _TINGLES (nivel 1)
	os.system('touch Taquirule/templo_E/_TINGLES/'+z) 
for z in dir_zelda:
	os.system('mkdir Taquirule/templo_E/_TINGLES/'+z)	
	for a in zelda_l:  #Se minan todos los directorios del segundo nivel
		os.system('touch Taquirule/templo_E/_TINGLES/'+z+'/'+a) 
	for x in dir_zelda:
		os.system('mkdir Taquirule/templo_E/_TINGLES/'+z+'/'+x)	
		for y in dir_zelda:
			os.system('mkdir Taquirule/templo_E/_TINGLES/'+z+'/'+x+'/'+y)	
			for a in zelda_l:  #Se minan todos los directorios del cuarto nivel
				os.system('touch Taquirule/templo_E/_TINGLES/'+z+'/'+x+'/'+y+'/'+a) 

os.system('touch Taquirule/templo_E/_TINGLES/_THE/_LEGEND/zelda')
os.system('touch Taquirule/templo_E/_TINGLES/_OF/_THE/zELDa')
os.system('touch Taquirule/templo_E/_TINGLES/_EAS/_MAJORAS/ZeldA')
os.system('touch Taquirule/templo_E/_TINGLES/_MAC/_MAC/ZELDA')


#carpetas que comienzen con -
os.system('mkdir Taquirule/templo_E/_SWORD')
os.system('touch Taquirule/templo_E/_SWORD/-zora')
os.system('touch Taquirule/templo_E/-zora')
os.system('touch Taquirule/templo_E/-eas')
os.system('touch Taquirule/templo_E/-is')
os.system('touch Taquirule/templo_E/-the')
os.system('mkdir Taquirule/templo_E/-HERO')
os.system('touch Taquirule/templo_E/-HERO/-of')
os.system('touch Taquirule/templo_E/-HERO/-this')
os.system('touch Taquirule/templo_E/-HERO/-legend')

print '---Se carga el templo_E'
#Fin del templo_E 

#Templo_F 

#Genera un archivo cOsA con permisos 700 y luego una carpera Xss con permisos 777
os.system('touch Taquirule/templo_F/cOsA && chmod 700 Taquirule/templo_F/cOsA')
os.system('mkdir Taquirule/templo_F/Xss')

aux = respaldo_wfms 
for i in range(50):
    os.system('touch Taquirule/templo_F/Xss/' + aux.pop())

print '---Se carga el templo_F'
#Fin del templo_F 

#Templo GR
os.system('rm -rf Taquirule/templo_ET/_SKULL')
os.system('rm -rf Taquirule/templo_ET/_KID')
lineas = respaldo
os.system('mkdir Taquirule/templo_ET/_SKULL')
os.system('mkdir Taquirule/templo_ET/_KID')
for i in range(800):
	os.system('touch Taquirule/templo_ET/_SKULL/'+(((lineas.pop()).lower()).replace("'",":")).strip("\n"))
for i in range(600):
	os.system('touch Taquirule/templo_ET/_KID/'+(((lineas.pop()).lower()).replace("'",":")).strip("\n"))

os.system('cp -r Taquirule/templo_ET/_SKULL/ Taquirule/templo_ET/_SKULL2')
os.system('cp -r Taquirule/templo_ET/_KID/ Taquirule/templo_ET/_KID2')
	

#archivo random que tendra 30 lineas
os.system('rm -rf Taquirule/templo_ET/goron')
os.system('touch Taquirule/templo_ET/goron')
for i in range(30):
    os.system("echo The Legend of EAS >> Taquirule/templo_ET/goron")

#Colocandole 30K a un archivo
os.system('mkdir -p Taquirule/templo_ET/SKULL/KID/IS/IN/THE/')
os.system('touch Taquirule/templo_ET/SKULL/KID/IS/IN/THE/moon')
for i in range(9999):
    os.system("echo aa >> Taquirule/templo_ET/SKULL/KID/IS/IN/THE/moon")
os.system('echo "Creete que eres EAS... di: soyseas" >> Taquirule/templo_ET/SKULL/KID/IS/IN/THE/moon')


os.system('rm -rf Taquirule/templo_ET/gekko')
os.system('rm -rf Taquirule/templo_ET/snapper')

os.system('touch Taquirule/templo_ET/gekko')
os.system('touch Taquirule/templo_ET/snapper')

words_from_masks = respaldo_wfms
for w in words_from_masks:
    	os.system('echo '+ w + '>> Taquirule/templo_ET/gekko')

palabra_distinta= 'GOMA'
aux = words_from_masks + [palabra_distinta]

random.shuffle(aux)        
for w in aux:
    	os.system('echo '+ w + '>> Taquirule/templo_ET/snapper')



print '---Se carga el templo_ET'
#Fin del templo_ET


#Se cambian los permisos de las carpetas
MASCARAS = ['AA','SB','EP','GR','EAS']
TEMPLOS = ['templo_A', 'templo_E', 'templo_F', 'templo_ET', 'templo_MAC']
for i in range(5):
	str0 = 'Taquirule/'+TEMPLOS[i]
	os.system('chown -R '+MASCARAS[i]+' '+str0+' ; chmod -R 700 '+' '+str0)

os.system('chmod 000 Taquirule/templo_E/tael') #tael no tiene permisos. Es el hada maligna
os.system('chmod 777 Taquirule/templo_F/Xss') #Los permisos de la carpeta para el ejercicio 2 de F 

os.system('chmod 777 Navi.sh')


