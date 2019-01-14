# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------

from spack import *


class RLeafcutter(RPackage):
    """Leafcutter quantifies RNA splicing variation using short-read RNA-seq data."""

    homepage = "http://davidaknowles.github.io/leafcutter/"
    url      = "https://github.com/davidaknowles/leafcutter/archive/v0.2.7.tar.gz"

    version('0.2.7', sha256='0e70ebce6be4b25bfabc0d489cbefa92ddede80380b1bbf4ec3a84182d10d1bd')

    depends_on('samtools', type=('run'))
    depends_on('python@2:', type=('build', 'run'))
    depends_on('r@3.3.3:', type=('build', 'run'))

    depends_on('r-rcpp', type=('build', 'run'))
    depends_on('r-rstan', type=('build', 'run'))
    depends_on('r-foreach', type=('build', 'run'))
    depends_on('r-ggplot2', type=('build', 'run'))
    depends_on('r-utils', type=('build', 'run'))
    depends_on('r-gridextra', type=('build', 'run'))
    depends_on('r-reshape2', type=('build', 'run'))
    depends_on('r-hmisc', type=('build', 'run'))
    depends_on('r-dplyr', type=('build', 'run'))
    depends_on('r-domc', type=('build', 'run'))
    depends_on('r-optparse', type=('build', 'run'))
    depends_on('r-shiny', type=('build', 'run'))
    depends_on('r-intervals', type=('build', 'run'))
    depends_on('r-shinycssloaders', type=('build', 'run'))
    depends_on('r-dt', type=('build', 'run'))
    depends_on('r-gtables', type=('build', 'run'))


    def configure_args(self, spec, prefix):
        # FIXME: Add arguments to pass to install via --configure-args
        # FIXME: If not needed delete this function
        args = []
        return args
