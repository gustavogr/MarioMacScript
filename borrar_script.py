#!/usr/bin/python
# -*- coding: utf-8 -*-

#Se debe correr como root
import os
print 'Se van borrar todas las carpetas'
os.system('rm -rf Taquirule')
print 'Se borrara el home de cada usuario creado'
os.system('rm -rf /home/AA')
os.system('rm -rf /home/SB')
os.system('rm -rf /home/EP')
os.system('rm -rf /home/GR')
os.system('rm -rf /home/EAS')

print 'Se borraran los usuarios'
os.system('userdel AA')
os.system('userdel SB')
os.system('userdel EP')
os.system('userdel GR')
os.system('userdel EAS')
