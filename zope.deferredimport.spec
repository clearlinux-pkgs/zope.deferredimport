#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : zope.deferredimport
Version  : 4.3.1
Release  : 11
URL      : https://files.pythonhosted.org/packages/b9/74/6eb2dcf013fac35d086abef2435b5a6621435c2b0c166ef5b63a1b51e91d/zope.deferredimport-4.3.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/b9/74/6eb2dcf013fac35d086abef2435b5a6621435c2b0c166ef5b63a1b51e91d/zope.deferredimport-4.3.1.tar.gz
Summary  : zope.deferredimport allows you to perform imports names that will only be resolved when used in the code.
Group    : Development/Tools
License  : ZPL-2.1
Requires: zope.deferredimport-license = %{version}-%{release}
Requires: zope.deferredimport-python = %{version}-%{release}
Requires: zope.deferredimport-python3 = %{version}-%{release}
Requires: setuptools
Requires: zope.proxy
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv
BuildRequires : zope.proxy

%description
``zope.deferredimport``
        =========================

%package license
Summary: license components for the zope.deferredimport package.
Group: Default

%description license
license components for the zope.deferredimport package.


%package python
Summary: python components for the zope.deferredimport package.
Group: Default
Requires: zope.deferredimport-python3 = %{version}-%{release}

%description python
python components for the zope.deferredimport package.


%package python3
Summary: python3 components for the zope.deferredimport package.
Group: Default
Requires: python3-core
Provides: pypi(zope.deferredimport)
Requires: pypi(setuptools)
Requires: pypi(zope.proxy)

%description python3
python3 components for the zope.deferredimport package.


%prep
%setup -q -n zope.deferredimport-4.3.1
cd %{_builddir}/zope.deferredimport-4.3.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603409494
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/zope.deferredimport
cp %{_builddir}/zope.deferredimport-4.3.1/LICENSE.txt %{buildroot}/usr/share/package-licenses/zope.deferredimport/a0b53f43aab58b46bf79ba756c50771c605ab4c5
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/zope.deferredimport/a0b53f43aab58b46bf79ba756c50771c605ab4c5

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
