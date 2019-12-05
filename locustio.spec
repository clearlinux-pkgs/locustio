#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : locustio
Version  : 0.9.0
Release  : 11
URL      : https://files.pythonhosted.org/packages/e6/88/2d56405c715df8c4c94850857c581007d39fe50dfe9dbcac91e378a8f24f/locustio-0.9.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/e6/88/2d56405c715df8c4c94850857c581007d39fe50dfe9dbcac91e378a8f24f/locustio-0.9.0.tar.gz
Summary  : Website load testing framework
Group    : Development/Tools
License  : MIT
Requires: locustio-bin = %{version}-%{release}
Requires: locustio-python = %{version}-%{release}
Requires: locustio-python3 = %{version}-%{release}
Requires: Flask
Requires: gevent
Requires: msgpack
Requires: pyzmq
Requires: requests
Requires: six
BuildRequires : Flask
BuildRequires : buildreq-distutils3
BuildRequires : gevent
BuildRequires : msgpack
BuildRequires : python-mock
BuildRequires : pyzmq
BuildRequires : requests
BuildRequires : six
Patch1: 0001-The-send_file-returns-response-with-proper-content-l.patch

%description


%package bin
Summary: bin components for the locustio package.
Group: Binaries

%description bin
bin components for the locustio package.


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

%description python3
python3 components for the locustio package.


%prep
%setup -q -n locustio-0.9.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1568876251
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/locust

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
