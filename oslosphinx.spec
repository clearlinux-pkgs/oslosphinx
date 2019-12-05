#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x421E6472811F9A81 (infra-root@openstack.org)
#
Name     : oslosphinx
Version  : 4.18.0
Release  : 39
URL      : https://tarballs.openstack.org/oslosphinx/oslosphinx-4.18.0.tar.gz
Source0  : https://tarballs.openstack.org/oslosphinx/oslosphinx-4.18.0.tar.gz
Source99 : https://tarballs.openstack.org/oslosphinx/oslosphinx-4.18.0.tar.gz.asc
Summary  : OpenStack Sphinx Extensions and Theme
Group    : Development/Tools
License  : Apache-2.0
Requires: oslosphinx-license = %{version}-%{release}
Requires: oslosphinx-python = %{version}-%{release}
Requires: oslosphinx-python3 = %{version}-%{release}
Requires: pbr
Requires: requests
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : pbr

%description
=============================
OpenStack Sphinx Extensions
=============================

%package license
Summary: license components for the oslosphinx package.
Group: Default

%description license
license components for the oslosphinx package.


%package python
Summary: python components for the oslosphinx package.
Group: Default
Requires: oslosphinx-python3 = %{version}-%{release}

%description python
python components for the oslosphinx package.


%package python3
Summary: python3 components for the oslosphinx package.
Group: Default
Requires: python3-core

%description python3
python3 components for the oslosphinx package.


%prep
%setup -q -n oslosphinx-4.18.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1551035379
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/oslosphinx
cp LICENSE %{buildroot}/usr/share/package-licenses/oslosphinx/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/oslosphinx/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
