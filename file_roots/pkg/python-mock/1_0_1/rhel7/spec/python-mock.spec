%if !(0%{?fedora} > 12 || 0%{?rhel} >= 7)
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%endif

%if 0%{?fedora} || 0%{?rhel} >= 7
%global with_python3 1
%endif

%global _description \
Mock is a Python module that provides a core mock class. It removes the need \
to create a host of stubs throughout your test suite. After performing an \
action, you can make assertions about which methods / attributes were used and \
arguments they were called with. You can also specify return values and set \
needed attributes in the normal way.

# Not yet in Fedora buildroot
%{!?python3_pkgversion:%global python3_pkgversion 3}

%global mod_name mock

Name:           python-mock
Version:        1.0.1
Release:        12%{?dist}
Summary:        A Python Mocking and Patching Library for Testing

License:        BSD
URL:            http://www.voidspace.org.uk/python/%{mod_name}/
Source0:        http://pypi.python.org/packages/source/m/%{mod_name}/%{mod_name}-%{version}.tar.gz
Source1:        LICENSE.txt

BuildArch:      noarch


%description %{_description}

%package -n python2-mock
Summary:    %{summary}
## BuildRequires:  python2-devel
BuildRequires:  python-devel
BuildRequires:  python-setuptools
# For tests
%if 0%{?rhel} <= 7
BuildRequires:  python-unittest2
%endif
%{?python_provide:%python_provide python-mock}
%{?python_provide:%python_provide python2-mock}

%description -n python2-mock %{_description}
Python 2 version.


%if 0%{?with_python3}
%package -n python%{python3_pkgversion}-mock
Summary:    %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
# For tests
#BuildRequires:  python%{python3_pkgversion}-unittest2
## %{?python_provide:%python_provide python%{python3_pkgversion}-mock}
Provides:       python%{python3_pkgversion}-mock

%description -n python%{python3_pkgversion}-mock %{_description}
Python %{python3_version} version.
%endif


%prep
%setup -q -n %{mod_name}-%{version}
cp -p %{SOURCE1} .


%build
%{py2_build}
%if 0%{?with_python3}
%{py3_build}
%endif

%check
%{__python2} setup.py test
# Failing
#{__python3} setup.py test


%install
%{py2_install}
%if 0%{?with_python3}
%{py3_install}
%endif

 
%files -n python2-mock
%license LICENSE.txt
%doc docs/* README.txt PKG-INFO
%{python2_sitelib}/*.egg-info
%{python2_sitelib}/%{mod_name}.py*

%if 0%{?with_python3}
%files -n python%{python3_pkgversion}-mock
%license LICENSE.txt
%doc docs/* README.txt PKG-INFO
%{python3_sitelib}/*.egg-info
%{python3_sitelib}/%{mod_name}.py*
%{python3_sitelib}/__pycache__/%{mod_name}*
%endif


%changelog
* Thu Apr 04 2019 SaltStack Packaging Team <packaging@saltstack.com> - 1.0.1-12
- Add support for Python 3.6

* Wed Feb 07 2018 SaltStack Packaging Team <packaging@saltstack.com> - 1.0.1-11
- Add support for Python 3

* Thu Jan 11 2018 SaltStack Packaging Team <packaging@saltstack.com> -1.0.1-10 
- Support for Python 3 on RHEL

* Wed Jan 6 2016 Orion Poplawski <orion@cora.nwra.com> - 1.0.1-9
- Modernize spec
- Run python2 tests, python3 failing

* Mon Nov 02 2015 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> 1.0.1-7
- Fix #1276771

* Thu Sep 18 2014 Praveen Kumar <kumarparaveen.nitdgp@gmail.com> 1.0.1-5
- Rebuild for RHEL-7
- Disable python3 features

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 09 2014 Dennis Gilmore <dennis@ausil.us> - 1.0.1-3
- rebuild for python 3.4
- disable test suite deps missing

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 11 2013 Luke Macken <lmacken@redhat.com> - 1.0.1-1
- Update to 1.0.1
- Run the test suite
- Add python-unittest2 as a build requirement

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Aug 04 2012 David Malcolm <dmalcolm@redhat.com> - 0.8.0-4
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 09 2012 Ralph Bean <rbean@redhat.com> - 0.8.0-2
- Python3 support

* Thu Mar 22 2012 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> - 0.8.0-1
- Updated to new version

* Fri Jul 22 2011 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> - 0.7.2-1
- Initial RPM release
