# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyCosmosWfm(PythonPackage):
    """COSMOS is a Python library for workflow management that allows
    formal description of pipelines and partitioning of jobs."""

    homepage = "https://mizzou-cbmi.github.io/"
    url = "https://pypi.io/packages/source/C/Cosmos-wfm/cosmos-wfm-2.8.27.tar.gz"

    version('2.8.27', sha256='4204472fd9e4141042fade5d3dbf5039d6ea6bdd55aa39ff916d239bfb80e642')

    depends_on('py-setuptools', type='build')
    depends_on('py-flask', type=('build','run'))
    depends_on('py-funcsigs', type=('build','run'))
    depends_on('py-blinker', type=('build','run'))
    depends_on('py-sqlalchemy', type=('build','run'))
    depends_on('py-networkx@2.0:', type=('build','run'))
    depends_on('py-six', type=('build','run'))
    depends_on('py-drmaa', type=('build','run'))
    depends_on('py-more-itertools', type=('build','run'))
    depends_on('py-decorator', type=('build','run'))
    depends_on('py-python-dateutil', type=('build','run'))
    depends_on('py-subprocess32', type=('build','run'), when='^python@2:2.999')
    depends_on('py-enum34', type=('build','run'), when='^python@2:3.5.999')
