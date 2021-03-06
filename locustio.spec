#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : locustio
Version  : 0.14.5
Release  : 16
URL      : https://files.pythonhosted.org/packages/61/77/e5317ea9c39fc976589bd60b2fc5ce8a5eb6d27583e40bf9b896c8babfbf/locustio-0.14.5.tar.gz
Source0  : https://files.pythonhosted.org/packages/61/77/e5317ea9c39fc976589bd60b2fc5ce8a5eb6d27583e40bf9b896c8babfbf/locustio-0.14.5.tar.gz
Summary  : Website load testing framework
Group    : Development/Tools
License  : MIT
Requires: locustio-bin = %{version}-%{release}
Requires: locustio-license = %{version}-%{release}
Requires: locustio-python = %{version}-%{release}
Requires: locustio-python3 = %{version}-%{release}
Requires: ConfigArgParse
Requires: Flask
Requires: gevent
Requires: geventhttpclient-wheels
Requires: msgpack
Requires: psutil
Requires: pyzmq
Requires: requests
BuildRequires : ConfigArgParse
BuildRequires : Flask
BuildRequires : buildreq-distutils3
BuildRequires : gevent
BuildRequires : gevent-python
BuildRequires : geventhttpclient-wheels
BuildRequires : geventhttpclient-wheels-python
BuildRequires : msgpack
BuildRequires : psutil
BuildRequires : python-mock
BuildRequires : python-mock-python
BuildRequires : pyzmq
BuildRequires : requests
Patch1: 0001-Don-t-enforce-version-matches.patch

%description


%package bin
Summary: bin components for the locustio package.
Group: Binaries
Requires: locustio-license = %{version}-%{release}

%description bin
bin components for the locustio package.


%package license
Summary: license components for the locustio package.
Group: Default

%description license
license components for the locustio package.


%package python
Summary: python components for the locustio package.
Group: Default
Requires: locustio-python3 = %{version}-%{release}

%description python
python components for the locustio package.


%package python3
Summary: python3 components for the locustio package.
Group: Default
Requires: python3-core
Provides: pypi(locustio)
Requires: pypi(configargparse)
Requires: pypi(flask)
Requires: pypi(gevent)
Requires: pypi(geventhttpclient_wheels)
Requires: pypi(msgpack)
Requires: pypi(psutil)
Requires: pypi(pyzmq)
Requires: pypi(requests)

%description python3
python3 components for the locustio package.


%prep
%setup -q -n locustio-0.14.5
cd %{_builddir}/locustio-0.14.5
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1586982326
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/locustio
cp %{_builddir}/locustio-0.14.5/LICENSE %{buildroot}/usr/share/package-licenses/locustio/42e2702bdcbe7d9a8cb854d0b4d015053bb5f948
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/locust

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/locustio/42e2702bdcbe7d9a8cb854d0b4d015053bb5f948

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
