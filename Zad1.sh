#!/bin/bash

PLANSZA=("0" "0" "0" "0" "0" "0" "0" "0" "0")
GRACZ="2"
WYGRANA="0"

function wyswietl
{
    echo "Plansza"
    echo "${PLANSZA[0]} | ${PLANSZA[1]} | ${PLANSZA[2]}"
    echo "${PLANSZA[3]} | ${PLANSZA[4]} | ${PLANSZA[5]}"
    echo "${PLANSZA[6]} | ${PLANSZA[7]} | ${PLANSZA[8]}"
}

function zakoncz
{
  if [ $WYGRANA -eq 3 ];
	then
    echo "Koniec gry - brak zwyciezcy!"
	else
    echo "Koniec gry - wygral gracz ${GRACZ}!"
	fi
  wyswietl
}

function spawdzWygrana
{
    if [[ ${PLANSZA[0]} -eq $GRACZ && ${PLANSZA[1]} -eq $GRACZ && ${PLANSZA[2]} -eq $GRACZ ]];
    then
      WYGRANA=$GRACZ
      zakoncz
    fi
    if [[ ${PLANSZA[3]} -eq $GRACZ && ${PLANSZA[4]} -eq $GRACZ && ${PLANSZA[5]} -eq $GRACZ ]];
    then
      WYGRANA=$GRACZ
      zakoncz
    fi
    if [[ ${PLANSZA[6]} -eq $GRACZ && ${PLANSZA[7]} -eq $GRACZ && ${PLANSZA[8]} -eq $GRACZ ]];
    then
      WYGRANA=$GRACZ
      zakoncz
    fi
    if [[ ${PLANSZA[0]} -eq $GRACZ && ${PLANSZA[3]} -eq $GRACZ && ${PLANSZA[6]} -eq $GRACZ ]];
    then
      WYGRANA=$GRACZ
      zakoncz
    fi
    if [[ ${PLANSZA[1]} -eq $GRACZ && ${PLANSZA[4]} -eq $GRACZ && ${PLANSZA[7]} -eq $GRACZ ]];
    then
      WYGRANA=$GRACZ
      zakoncz
    fi
    if [[ ${PLANSZA[2]} -eq $GRACZ && ${PLANSZA[5]} -eq $GRACZ && ${PLANSZA[8]} -eq $GRACZ ]];
    then
      WYGRANA=$GRACZ
      zakoncz
    fi
    if [[ ${PLANSZA[0]} -eq $GRACZ && ${PLANSZA[4]} -eq $GRACZ && ${PLANSZA[8]} -eq $GRACZ ]];
    then
      WYGRANA=$GRACZ
      zakoncz
    fi
    if [[ ${PLANSZA[2]} -eq $GRACZ && ${PLANSZA[4]} -eq $GRACZ && ${PLANSZA[6]} -eq $GRACZ ]];
    then
      WYGRANA=$GRACZ
      zakoncz
    fi
  if [ $WYGRANA -eq "0" ];
  then
    if ! [[ ${PLANSZA[0]} -eq "0" || ${PLANSZA[1]} -eq "0" || ${PLANSZA[2]} -eq "0" || ${PLANSZA[3]} -eq "0" || ${PLANSZA[4]} -eq "0" || ${PLANSZA[5]} -eq "0" || ${PLANSZA[6]} -eq "0" || ${PLANSZA[7]} -eq "0" || ${PLANSZA[8]} -eq "0" ]];
    then
      WYGRANA="3"
      zakoncz
    fi
  fi
}

function zmienGracza
{
    if [ $GRACZ -eq 1 ];
	  then
		  GRACZ="2"
	  else
		  GRACZ="1"
	  fi
}

while [ $WYGRANA -eq "0" ]
do
  wyswietl
  zmienGracza
  echo -e "\n Które pole zaznaczyc dla zawodnika ${GRACZ}"
	read POLE

  if [ -z "$POLE" ];
  then
    echo "Pusta wartosc wpisanej zmiennej 'pole'"
		continue
  fi

  if [[ $POLE -ge 0 && $POLE -le 8 ]];
	then
		echo "Wybrano pole: ${POLE}"
	else
		echo "Wybrano pole poza zakresem"
		continue
	fi

  if [[ ${PLANSZA[POLE]} -eq "0" ]];
	then
		PLANSZA[POLE]=$GRACZ
		spawdzWygrana
	else
		echo "Wybrane pole bylo zajete"
		continue
	fi
done


