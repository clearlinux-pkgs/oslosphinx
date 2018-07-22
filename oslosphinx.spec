#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x421E6472811F9A81 (infra-root@openstack.org)
#
Name     : oslosphinx
Version  : 4.18.0
Release  : 34
URL      : https://tarballs.openstack.org/oslosphinx/oslosphinx-4.18.0.tar.gz
Source0  : https://tarballs.openstack.org/oslosphinx/oslosphinx-4.18.0.tar.gz
Source99 : https://tarballs.openstack.org/oslosphinx/oslosphinx-4.18.0.tar.gz.asc
Summary  : OpenStack Sphinx Extensions and Theme
Group    : Development/Tools
License  : Apache-2.0
Requires: oslosphinx-python3
Requires: oslosphinx-license
Requires: oslosphinx-python
Requires: pbr
Requires: requests
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python3-dev
BuildRequires : setuptools

%description
OpenStack Sphinx Extensions
        =============================
        
        oslosphinx is obsolete. The openstackdocstheme package should be used
        instead. oslosphinx will be maintained for the pike, ocata, and newton
        release series and completely remove after that pike is marked
        end-of-life.
        
        The contents of this repository are still available in the Git source
        code management system.  To see the contents of this repository before
        it reached its end of life, please check out the previous commit with
        "git checkout HEAD^1", or check out one of the supported stable
        branches.
        
        For any further questions, please email
        openstack-dev@lists.openstack.org or join #openstack-oslo on Freenode.

%package license
Summary: license components for the oslosphinx package.
Group: Default

%description license
license components for the oslosphinx package.


%package python
Summary: python components for the oslosphinx package.
Group: Default
Requires: oslosphinx-python3

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
export SOURCE_DATE_EPOCH=1532269800
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/oslosphinx
cp LICENSE %{buildroot}/usr/share/doc/oslosphinx/LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/oslosphinx/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
