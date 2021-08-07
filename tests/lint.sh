set -e

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
ansible-test sanity
