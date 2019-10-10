# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Lftp(AutotoolsPackage):
    """LFTP is a sophisticated file transfer program supporting a number
       of network protocols (ftp, http, sftp, fish, torrent)."""

    homepage = "http://lftp.yar.ru/"
    url      = "https://github.com/lavv17/lftp/archive/v4.6.4.tar.gz"

    version('4.8.4', sha256='0d4e7eb59c14ad3688abde54084fc247230f144ac4afdfa421a6b29174a830dd')
    version('4.8.1', sha256='6117866215cd889dab30ff73292cd1d35fe0e12a9af5cd76d093500d07ab65a3')
    version('4.7.7', sha256='c9d45b67a5ec744e1a2e257aed77ecd3cd1f3d412d964fb1268c175b0ea72ce8')
    version('4.6.4', sha256='07f863a86e7d6e2fa73b45182bc57c5f4e77ce674de7fdaf8975a13d1848bf0e')

    depends_on('expat')
    depends_on('libiconv')
    depends_on('ncurses')
    depends_on('openssl')
    depends_on('readline')
    depends_on('zlib')

    def configure_args(self):
        return [
            '--with-expat={0}'.format(self.spec['expat'].prefix),
            '--with-libiconv={0}'.format(self.spec['libiconv'].prefix),
            '--with-openssl={0}'.format(self.spec['openssl'].prefix),
            '--with-readline={0}'.format(self.spec['readline'].prefix),
            '--with-zlib={0}'.format(self.spec['zlib'].prefix),
            '--disable-dependency-tracking',
        ]
