%global pypi_name django-appconf

Name:           python-%{pypi_name}
Version:        0.6
Release:        1%{?dist}
Summary:        A helper class for handling configuration defaults of packaged apps gracefully

License:        BSD
URL:            http://pypi.python.org/pypi/django-appconf/0.5
Source0:        http://pypi.python.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python-sphinx
#BuildRequires:  python-django-discover-runner

%if 0%{?rhel}<7 || 0%{?fedora} < 18
Requires:   Django
%else
Requires:   python-django
%endif

%description
A helper class for handling configuration
defaults of packaged Django
apps gracefully.


%prep
%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# generate html docs 
sphinx-build docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%build
%{__python} setup.py build


%install
%{__python} setup.py install --skip-build --root %{buildroot}

# checks fail in mock
#%check
#%{__python} setup.py test

%files
%doc html README.rst LICENSE
%{python_sitelib}/appconf
%{python_sitelib}/django_appconf-%{version}-py?.?.egg-info

%changelog
* Wed Mar 06 2013 Matthias Runge <mrunge@redhat.com> - 0.6-1
- update to appconf-0.6

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Sep 26 2012 Matthias Runge <mrunge@redhat.com> - 0.5-2
- also add requirement: Django/python-django

* Tue Sep 11 2012 Matthias Runge <mrunge@redhat.com> - 0.5-1
- Initial package.
