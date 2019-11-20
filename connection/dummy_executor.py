#
# Copyright(c) 2019 Intel Corporation
# SPDX-License-Identifier: BSD-3-Clause-Clear
#

from connection.base_executor import BaseExecutor


class DummyExecutor(BaseExecutor):
    def _execute(self, command, timeout=None):
        print(command)

    def rsync(self, src, dst, delete, symlinks, exclude_list, timeout):
        print(f'COPY FROM "{src}" TO "{dst}"')
