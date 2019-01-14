# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RShinycssloaders(RPackage):
    """Create a lightweight Shiny wrapper for the css-loaders.  Wrapping a Shiny output will 
    automatically show a loader when the output is (re)calculating.
    """

    homepage = "https://cran.r-project.org/web/packages/shinycssloaders/index.html"
    url      = "https://cran.r-project.org/src/contrib/shinycssloaders_0.2.0.tar.gz"

    version('0.2.0', sha256='e4890ceeea49c9186cf2edc98c4ca55bbc562ab9cde240a53666b0534fd5ffae')
    version('0.1.0', sha256='7cdfcff40609f50708cd871fe845f0122701ce50f5ad2aa9f6b23b31215c560d')

    depends_on('r-digest', type=('run'))
    depends_on('r-glue', type=('run'))
    depends_on('r-shiny', type=('run'))

