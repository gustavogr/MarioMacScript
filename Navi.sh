MENSAJE_READ="[Enter para continuar] "

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
    break
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
	elif [ $respuesta = "SI" -o $respuesta = "si"]
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