#!/bin/bash -eu

set -e

if test "$1" == 'requirements'
then
	args=requirements
fi

if test -n "$2"
then
	args="$args --python $2"
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

echo "ansible-test sanity"
ansible-test sanity $args
