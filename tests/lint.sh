#!/bin/bash -eu

set -e

args=()

if test "$#" -gt 0
then

        if test "$1" == 'requirements'
        then
        	args[0]=--requirements
		shift
        fi
fi


if test "$#" -gt 0
then
        if test -n "$1"
        then
        	args+=(--python)
        	args+=("$1")
		shift
        fi
fi

echo "Checking for forgotten no_log..."
grep -qr "no_log: false\s*$" . && exit 1

echo "yamllint..."
yamllint -s .

echo "ansible-lint..."
ansible-lint -v
ansible-lint -v roles/*/vars/*.yml

echo "flake8..."
flake8 -v

echo "ansible-test sanity..."
# shellcheck disable=SC2068
ansible-test sanity ${args[@]}
