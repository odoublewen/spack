# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Emboss(AutotoolsPackage):
    """EMBOSS is a free Open Source software analysis package specially
       developed for the needs of the molecular biology (e.g. EMBnet) user
       community"""

    homepage = "http://emboss.sourceforge.net/"
    url      = "ftp://emboss.open-bio.org/pub/EMBOSS/EMBOSS-6.6.0.tar.gz"

    version('6.6.0', 'cc3fca80cb0618deb10fa0d29fe90e4b')

    variant('without-x', default=False, description='Build without X support')
    variant('without-postgresql', default=False, description='Build without postgreSQL for Ensembl access library')

    depends_on('libxpm', when='~without-x')
    depends_on('libgd')
    depends_on('postgresql', when='~without-postgresql')

    def configure_args(self):
        args = []
        if self.spec.satisfies('+without-x'):
            args.append('--without-x')
        if self.spec.satisfies('+without-postgresql'):
            args.append('--without-postgresql')

    @run_after('configure')
    def skip_update_checks(self):
        # Delete $(bindir)/embossupdate to skip update checks
        filter_file('$(bindir)/embossupdate', '', 'Makefile', string=True)
