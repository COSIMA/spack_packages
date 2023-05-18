# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class DomainTools(CMakePackage):
    """Code and tools to edit and manipulate ocean model grids and
    topographies."""

    homepage = "https://github.com/COSIMA/domain-tools/"
    url = "https://github.com/COSIMA/domain-tools/archive/v0.1.0.tar.gz"

    maintainers = ["micaeljtoliveira"]

    version("0.1.0", sha256="9250247712a13fa67b6b1724d16af4915a8ea3ebd7e8d49640a56ebdec73ae52")

    # FIXME: Add dependencies if required.
    depends_on("netcdf-fortran")
