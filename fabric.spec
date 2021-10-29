#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x9C29BC560041E930 (jeff@bitprophet.org)
#
Name     : fabric
Version  : 2.6.0
Release  : 15
URL      : https://files.pythonhosted.org/packages/32/61/9a26b8f3dcdb5cb17daff57c9a85be6d5963d50488f45319d64a413da762/fabric-2.6.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/32/61/9a26b8f3dcdb5cb17daff57c9a85be6d5963d50488f45319d64a413da762/fabric-2.6.0.tar.gz
Source1  : https://files.pythonhosted.org/packages/32/61/9a26b8f3dcdb5cb17daff57c9a85be6d5963d50488f45319d64a413da762/fabric-2.6.0.tar.gz.asc
Summary  : High level SSH command execution
Group    : Development/Tools
License  : BSD-2-Clause
Requires: fabric-bin = %{version}-%{release}
Requires: fabric-license = %{version}-%{release}
Requires: fabric-python = %{version}-%{release}
Requires: fabric-python3 = %{version}-%{release}
Requires: invoke
Requires: paramiko
Requires: pathlib2
Requires: python-mock
BuildRequires : buildreq-distutils3
BuildRequires : invoke
BuildRequires : paramiko
BuildRequires : pathlib2
BuildRequires : python-mock

%description
To find out what's new in this version of Fabric, please see `the changelog

%package bin
Summary: bin components for the fabric package.
Group: Binaries
Requires: fabric-license = %{version}-%{release}

%description bin
bin components for the fabric package.


%package license
Summary: license components for the fabric package.
Group: Default

%description license
license components for the fabric package.


%package python
Summary: python components for the fabric package.
Group: Default
Requires: fabric-python3 = %{version}-%{release}

%description python
python components for the fabric package.


%package python3
Summary: python3 components for the fabric package.
Group: Default
Requires: python3-core
Provides: pypi(fabric)
Requires: pypi(invoke)
Requires: pypi(paramiko)
Requires: pypi(pathlib2)

%description python3
python3 components for the fabric package.


%prep
%setup -q -n fabric-2.6.0
cd %{_builddir}/fabric-2.6.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1629183177
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/fabric
cp %{_builddir}/fabric-2.6.0/LICENSE %{buildroot}/usr/share/package-licenses/fabric/eadf0675261da2116b63962716fbf09f4cb946ca
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/fab

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/fabric/eadf0675261da2116b63962716fbf09f4cb946ca

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
