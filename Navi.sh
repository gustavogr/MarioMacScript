MENSAJE_READ="[Enter para continuar] "

function trapear {
    trap insultar SIGHUP
    trap insultar SIGINT
    trap insultar SIGQUIT
    trap insultar SIGILL
    trap insultar SIGTRAP
    trap insultar SIGABRT
    trap insultar SIGBUS
    trap insultar SIGFPE
#
    trap insultar SIGUSR1
    trap insultar SIGSEGV
    trap insultar SIGUSR2
    trap insultar SIGPIPE
    trap insultar SIGALRM
    trap insultar SIGTERM
    # trap insultar SIGSTKFLT
    # trap insultar SIGCHLD
    # trap insultar SIGCONT
    trap insultar SIGSTOP
    trap insultar SIGTSTP
    # trap insultar SIGTTIN
    # trap insultar SIGTTOU
    # trap insultar SIGURG
    # trap insultar SIGXCPU
    # trap insultar SIGXFSZ
    # trap insultar SIGVTALRM
    # trap insultar SIGPROF
    # trap insultar SIGWINCH
    # trap insultar SIGIO
    # trap insultar SIGPWR
    # trap insultar SIGSYS
    # trap insultar SIGRTMIN
    # trap insultar SIGRTMIN+1
    # trap insultar SIGRTMIN+2
    # trap insultar SIGRTMIN+3
    # trap insultar SIGRTMIN+4
    # trap insultar SIGRTMIN+5
    # trap insultar SIGRTMIN+6
    # trap insultar SIGRTMIN+7
    # trap insultar SIGRTMIN+8
    # trap insultar SIGRTMIN+9
    # trap insultar SIGRTMIN+10
    # trap insultar SIGRTMIN+11
    # trap insultar SIGRTMIN+12
    # trap insultar SIGRTMIN+13
    # trap insultar SIGRTMIN+14
    # trap insultar SIGRTMIN+15
    # trap insultar SIGRTMAX-14
    # trap insultar SIGRTMAX-13
    # trap insultar SIGRTMAX-12
    # trap insultar SIGRTMAX-11
    # trap insultar SIGRTMAX-10
    # trap insultar SIGRTMAX-9
    # trap insultar SIGRTMAX-8
    # trap insultar SIGRTMAX-7
    # trap insultar SIGRTMAX-6
    # trap insultar SIGRTMAX-5
    # trap insultar SIGRTMAX-4
    # trap insultar SIGRTMAX-3
    # trap insultar SIGRTMAX-2
    # trap insultar SIGRTMAX-1
    # trap insultar SIGRTMAX
    echo ""
}

function inicio {
    clear
    cat dibujos/navi.txt
    printf "\n\n\n"
    read -p "$MENSAJE_READ"
    clear
    cat dialogos/dialogo_inicio.txt
    printf "\n\n\n"
    read -p "$MENSAJE_READ"
    clear
    cat dialogos/dialogo_inicio2.txt
    printf "\n\n\n"
    read -p "$MENSAJE_READ"
    clear
    cat dibujos/navi.txt
}

function dormir {
    for i in `seq 1 100000`
    do
	echo ""
    done
}

function go_evil {
    cat dibujos/majora.txt
    sleep 0.3
    for i in `seq 1 50`
    do
	sleep 0.1
	printf "\n"
    done
    clear
    cat dibujos/ganondorf.txt
    trapear    
    while true
    do
	p=""
    done
}

function insultar {
    clear
    cat dialogos/dialogo.txt
    sleep 1
    cat dibujos/ganondorf.txt
}

function final {
    clear 
    cat dialogos/dialogo_fintemplos.txt
    printf "\n\n\n"
    read -p "$MENSAJE_READ"
    clear
    cat dibujos/majora.txt
    sleep 5
    while true
    do
	clear
	cat dialogos/dialogo_ponersemascara.txt
	printf "\n\n\n"
	read -p "[SI/NO para continuar] " respuesta

	if [ $respuesta = "NO" -o  $respuesta = "no" ]
	then
	    clear
	    cat dialogos/dialogo_ponersemascara_no.txt
	    printf "\n\n\n"
	    read -p "$MENSAJE_READ"       
	    break
	elif [  $respuesta = "SI" -o $respuesta = "si" ]
	then
	    break
	else
	    clear
	    echo $respuesta
	    printf "\n\nNo entiendo lo que dices..."
	    printf "\n\n\n"
	    read -p "$MENSAJE_READ"       
	fi
    done
    clear
    printf "\n\nNavi se puso la mascara y se esta transformando!"
    printf "\n\n\n"
    read -p "$MENSAJE_READ"
    go_evil
}

function entregar_mascara {
    printf "\nListen!\n"
    case $1 in 
	"palabra1 palabra2 palabra3" )
	    echo "tomatu vaina"
	    ;;
	"palabra4 palabra5" )
	    echo "tomatu vaina"
	    ;;	
	"palabra6 palabra7" )
	    echo "tomatu vaina"
	    ;;	
	"palabra8 palabra9" )
	    echo "tomatu vaina"
	    ;;	
	"g" )
	    final
	    ;;
	* )
	    echo "Lo siento, no te entiendo. Esa frase no corresponde a ninguna mascara"
	    echo "Gente del mac: esto todavia no esta implementado, para saltarse al final pongan la letra g solamente"
	    ;;
    esac
}

inicio

while true ;
do
    printf "\n\n\n[Dime una frase para conseguir tu mascara] "
    read -t 30 pregunta
    if [ ! -z $pregunta ]
	then
	entregar_mascara $pregunta
	continue
    else
	clear
	printf "\n\n\n Whhhhuuuuuuusssshhhh..."
	kill -20 $$ 
	cat dibujos/navi.txt
    fi
done