> [!IMPORTANT]  
> **This repository has been archived and is read-only. Spack packages from this repo are maintained at https://github.com/ACCESS-NRI/spack-packages**

# COSIMA Spack packages

This is a spack package repository maintained by COSIMA for packages that are not available by default in spack.

The namespace of the pacakge repository is cosima.

## How to utilise this package repository

By default you have a single package repository (`builtin`) when you clone spack
```bash
$ spack repo list
==> 1 package repository.
builtin    $SPACK_ROOT/var/spack/repos/builtin
```
(note `$SPACK_ROOT` is substituted in all paths to make the description installation independent)

And the package is not available:
```
$ spack list domain-tools
==> 0 packages
```

To use the packages in this repository first clone the repo to a path of your choosing (represented here as `$PACKAGE_PATH`)
```
git clone git@github.com:COSIMA/spack_packages.git $PACKAGE_PATH/spack_packages
```
and then add the location of the repository to your spack instance
```
git repo add $PACKAGE_PATH/spack_packages
```
and then confirm it is has been added correctly:
```
$ spack repo list
==> 2 package repositories.
cosima        $PACKAGE_PATH/spack_packages
builtin       $SPACK_ROOT/var/spack/repos/builtin
```
Now the `domain-tools` package should be available to install
```
$ spack list domain-tools
domain-tools
==> 1 packages
```

## More information

For more information see the extensive [spack documentation](https://spack.readthedocs.io/en/latest/repositories.html) on how to utilise repository files. 
