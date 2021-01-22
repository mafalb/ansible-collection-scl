# vim: set ts=4 expandtab:

# This file is part of ansible-collection-scl
# Copyright (c) 2021 Markus Falb <markus.falb@mafalb.at>
#
# ansible-collection-scl is free software: you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# ansible-collection-scl is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with ansible-collection-scl.
# If not, see <https://www.gnu.org/licenses/>.

from __future__ import (absolute_import, division, print_function)
from ansible.module_utils.six import raise_from
from ansible.errors import AnsibleError
from ansible.module_utils._text import to_native
__metaclass__ = type


def filter_scl_vendor(scl_prefix):
    scl_prefix = str(scl_prefix)
    if (len(scl_prefix) == 0):
        raise AnsibleError('empty provider in scl_prefix')
    try:
        if (scl_prefix.count('-') == 1):
            if (len(scl_prefix.split('-')[0]) == 0):
                raise AnsibleError('empty provider in scl_prefix')
            return scl_prefix.split('-')[0]
        elif (scl_prefix.count('-') == 0):
            return 'rh'
        else:
            raise AnsibleError('Bad scl_prefix: %s' % scl_prefix)
    except Exception as e:
        raise_from(AnsibleError('Error in filter_scl_vendor: %s'
                   % to_native(e)),
                   e)


def filter_scl_name(scl_prefix):
    scl_prefix = str(scl_prefix)
    if (len(scl_prefix) == 0):
        raise AnsibleError('empty name in scl_prefix')
    try:
        if (scl_prefix.count('-') == 1):
            if (len(scl_prefix.split('-')[1]) == 0):
                raise AnsibleError('empty name in scl_prefix')
            return scl_prefix.split('-')[1]
        elif (scl_prefix.count('-') == 0):
            return scl_prefix
        else:
            raise AnsibleError('Bad scl_prefix: %s' % scl_prefix)
    except Exception as e:
        raise_from(AnsibleError('Error in filter_scl_name: %s' % to_native(e)),
                   e)


class FilterModule(object):
    def filters(self):
        return {
            'provider': filter_scl_vendor,
            'name': filter_scl_name,
        }
