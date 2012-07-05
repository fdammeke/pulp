# -*- coding: utf-8 -*-

# Copyright © 2010-2011 Red Hat, Inc.
#
# This software is licensed to you under the GNU General Public
# License as published by the Free Software Foundation; either version
# 2 of the License (GPLv2) or (at your option) any later version.
# There is NO WARRANTY for this software, express or implied,
# including the implied warranties of MERCHANTABILITY,
# NON-INFRINGEMENT, or FITNESS FOR A PARTICULAR PURPOSE. You should
# have received a copy of GPLv2 along with this software; if not, see
# http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.

import logging

from pulp.server.db.model import Consumer, Repo

_log = logging.getLogger('pulp')


version = 19

def migrate():
    _log.info('migration to data model version %d started' % version)
    _migrate_repos()
    _log.info('migration to data model version %d complete' % version)

def _migrate_repos():
    #
    # update repo: Add a new preserve_metadata option 
    #
    collection = Repo.get_collection()
    for repo in collection.find():
        modified = False
        if 'preserve_metadata' not in repo:
            repo['preserve_metadata'] = False
            modified = True
        if modified:
            collection.save(repo, safe=True)