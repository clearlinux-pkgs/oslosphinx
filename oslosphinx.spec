#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : oslosphinx
Version  : 3.2.0
Release  : 10
URL      : http://tarballs.openstack.org/oslosphinx/oslosphinx-3.2.0.tar.gz
Source0  : http://tarballs.openstack.org/oslosphinx/oslosphinx-3.2.0.tar.gz
Summary  : OpenStack Sphinx Extensions and Theme
Group    : Development/Tools
License  : Apache-2.0
Requires: oslosphinx-python
BuildRequires : Babel-python
BuildRequires : Jinja2
BuildRequires : Pygments
BuildRequires : Sphinx-python
BuildRequires : WebOb-python
BuildRequires : coverage-python
BuildRequires : discover-python
BuildRequires : docutils-python
BuildRequires : extras
BuildRequires : extras-python
BuildRequires : fixtures-python
BuildRequires : flake8-python
BuildRequires : hacking
BuildRequires : linecache2-python
BuildRequires : markupsafe-python
BuildRequires : mccabe-python
BuildRequires : mock-python
BuildRequires : mox3-python
BuildRequires : netaddr-python
BuildRequires : oslo.config
BuildRequires : oslo.context-python
BuildRequires : oslo.i18n-python
BuildRequires : oslosphinx-python
BuildRequires : oslotest-python
BuildRequires : pbr
BuildRequires : pbr-python
BuildRequires : pep8
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pyflakes-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python-mimeparse-python
BuildRequires : python-subunit
BuildRequires : python3-dev
BuildRequires : pytz-python
BuildRequires : requests-python
BuildRequires : requirements-parser
BuildRequires : setuptools
BuildRequires : six
BuildRequires : six-python
BuildRequires : stevedore
BuildRequires : testrepository-python
BuildRequires : testscenarios
BuildRequires : testtools
BuildRequires : testtools-python
BuildRequires : tox
BuildRequires : traceback2-python
BuildRequires : unittest2-python
BuildRequires : virtualenv

%description
OpenStack Sphinx Extensions
===========================
Theme and extension support for Sphinx documentation from the
OpenStack project.

%package python
Summary: python components for the oslosphinx package.
Group: Default

%description python
python components for the oslosphinx package.


%prep
%setup -q -n oslosphinx-3.2.0

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python2 setup.py test
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
