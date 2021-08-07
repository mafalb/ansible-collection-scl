#!/bin/bash -eu

set -eu

args=${args:=''}

if test "$#" -gt 0
then

        if test "$1" == 'requirements'
        then
        	args="--requirements"
        fi
fi


if test "$#" -gt 1
then
        if test -n "$2"
        then
        	args="$args --python $2"
        fi
fi

echo "Checking for forgotten no_log..."
! grep -r "no_log: false" .

echo "yamllint..."
yamllint -s .

echo "ansible-lint..."
ansible-lint -v
ansible-lint -v roles/*/vars/*.yml

echo "flake8..."
flake8 -v

echo "ansible-test sanity..."
if test -n "$args"
then
	echo yeah
	ansible-test sanity "$args"
else
	ansible-test sanity
fi
