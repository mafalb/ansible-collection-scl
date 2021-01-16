# vim: set ts=4 expandtab:

# BSD 3-Clause License
#
# Copyright (c) 2021 Markus Falb <markus.falb@mafalb.at>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF
# THE POSSIBILITY OF SUCH DAMAGE.

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
