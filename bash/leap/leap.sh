#!/usr/bin/env bash

main() {
yr=$1
res=false

if [ $# -ne 1 ] || [[ -n ${yr//[0-9]} ]]; then
echo 'Usage: leap.sh <year>'
exit 1
elif [ $(expr $1 % 4) -eq 0 ] && [ $(expr $1 % 100) -ne 0 ]; then
res=true
elif [ $(expr $1 % 4) -eq 0 ] && [ $(expr $1 % 400) -eq 0 ]; then
res=true
fi

echo $res
exit 0
}

main "$@"
