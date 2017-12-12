#!/bin/bash
export TERM=xterm-256color

tput sgr0; # reset colors
bold=$(tput bold);
reset=$(tput sgr0);
black=$(tput setaf 67);
blue=$(tput setaf 25);
green=$(tput setaf 44);
pyword=$(tput setaf 61);
white=$(tput setaf 15);
yellow=$(tput setaf 178);

pylogo=(
"              .SSSSSSSSSS.              "
"            .SS´´SSSSSSSSSS.            "
"            SSS··SSSSSSSSSSS            "
"            ´´´´´´´´SSSSSSSS            "
"    .SSSSSSSSSSSSSSSSSSSSSSS iiiiiii,   "
" .SSSSSSSSSSSSSSSSSSSSSSSSSS iiiiiiiii. "
" SSSSSSSSSSSSSSSSSSSSSSSSSSS iiiiiiiiii "
" SSSSSSSSSSSSSSSSSSSSSSSSSSS iiiiiiiiii "
" SSSSSSSSSS ,,,,,,,,,,,,,,,,,iiiiiiiiii "
" SSSSSSSSSS iiiiiiiiiiiiiiiiiiiiiiiiiii "
" ·SSSSSSSSS iiiiiiiiiiiiiiiiiiiiiiiiii· "
"    ·SSSSSS iiiiiiiiiiiiiiiiiiiiiii·    "
"            iiiiiiii,,,,,,,,            "
"            iiiiiiiiiii··iii            "
"            ·iiiiiiiiii,,ii·            "
"              ·iiiiiiiiii·              "
)

function etiqueta {
  entrada="${yellow}$1${white}: $2"
  i=${entrada// /_}
  echo $i
}

ITER=0
arrayName=(
"${yellow}arteagamarcelo${white}@${yellow}gmail.com${reset}"
"${white}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~${reset}"
"${white}> ${black}MARCELO ${black}ARTEAGA"
""
"${green}[~]#_linux"
"${pyword} ____        _   _                 "
"${pyword}|  _ \ _   _| |_| |__   ___  _ __  "
"${pyword}| |_) | | | | __| '_ \ / _ \| '_ \ "
"${pyword}|  __/| |_| | |_| | | | (_) | | | |"
"${pyword}|_|    \__, |\__|_| |_|\___/|_| |_|"
"${pyword}       |___/                       "
)

echo ""
for i in "${pylogo[@]}"
do
  i=$i'\t'${arrayName[$ITER]}
  i=${i// /\=}
  i=${i/\.\S/$blue\.\S}
  i=${i/\·\S/$blue\·\S}
  i=${i/\S/$blue\S}
  i=${i/\´/$blue\´}
  i=${i/\S/$blue\S}
  i=${i/\·\i/$yellow\·\i}
  i=${i/\i/$yellow\i}
  i=${i/\,/$yellow\,}
  i=${i//\=/$reset $pyword}
  # echo -e $i '\t' ${arrayName[$ITER]}
  echo -e $i
  ITER=${ITER}+1
done
echo "${reset}"

