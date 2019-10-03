# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyDrmaa(PythonPackage):
    """Distributed Resource Management Application API (DRMAA) bindings
    for Python."""

    homepage = "https://github.com/pygridtools/drmaa-python"
    url = "https://pypi.io/packages/source/D/Drmaa/drmaa-0.7.9.tar.gz"

    version('0.7.9', sha256='12540cd98afc40d5c0b2f38d7b0e46468d1c45192a2f401f41fc2eda9c9f5542')

    depends_on('py-setuptools', type='build')
