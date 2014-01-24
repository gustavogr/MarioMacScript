import curses
import time
import os

#Se inicializa la pantalla 
pantalla = curses.initscr()
pantalla.erase()
pantalla.scrollok(True)

#Se obtienen las dimensiones de la pantalla
maxx, maxy = pantalla.getmaxyx()

#Se oculta el cursor
curses.curs_set(0)

#Se obtienen los creditos
credFile = open('creditos.txt')
lineas = credFile.readlines()
lineas.reverse()
credFile.close()
numlineas = len(lineas)

# # #Se crea un pad para mostrar los creditos
# cpad = curses.newpad(20,20)
# cpad.border(0)
# cpad.scrollok(True)
# cpad.idlok(True)

# cpad.refresh(0,0, 3,5, 20,20)



# for linea in lineas:
#     cpad.addstr(18,1,linea)
#     cpad.scroll(1)
#     time.sleep(1)
#     cpad.refresh(0,0, 3,5, 20,20)
# cpad.getch()
try:
    os.system("timidity Title01.mid > /dev/null 2>/dev/null &")
    for i in range(0,numlineas+maxx):
        pantalla.refresh()
        pantalla.scroll(1)
        if lineas:
            linea = lineas.pop()
            linea = linea[:-1]
            pantalla.addstr(maxx-1, (maxy-1-linea.__len__())/2, linea)
        time.sleep(0.3)
    os.system("killall timidity > /dev/null 2>/dev/null ")    
except KeyboardInterrupt:
    curses.endwin()

# pad = curses.newpad(40,60)
# pad_pos = 0
# pad.refresh(pad_pos, 0, 5, 5, 10, 60)

# time.sleep(2)


curses.endwin()


