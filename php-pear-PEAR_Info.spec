%include	/usr/lib/rpm/macros.php
%define		_class		PEAR
%define		_subclass	Info
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - show Information about your PEAR install and its packages
Summary(pl):	%{_pearname} - pokazywanie informacji o instalacji PEAR-a i jego pakietach
Name:		php-pear-%{_pearname}
Version:	1.6.0
Release:	1.1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	5a184e62f6792c13e692d0996e8226ff
URL:		http://pear.php.net/package/PEAR_Info/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package generates a comprehensive information page for your
current PEAR install.
- The format for the page is similar to that for phpinfo() except
  using PEAR colors.
- Has complete PEAR Credits (based on the packages you have
  installed).
- Will show if there is a newer version than the one presently
  installed (and what its state is).
- Each package has an anchor in the form pkg_PackageName - where
  PackageName is a case-sensitive PEAR package name.

In PEAR status of this package is: %{_status}.

%description -l pl
Ten pakiet generuje wyczerpuj±c± stronê informacyjn± o aktualnej
instalacji PEAR-a.
- Format strony jest podobny do formatu phpinfo() oprócz u¿ytych
  kolorów PEAR-a.
- Ma pe³n± listê zas³ug PEAR-a (opart± na zainstalowanych pakietach).
- Pokazuje, czy jest nowsza wersja zainstalowanych klas (i jaki jest
  ich status).
- Ka¿dy pakiet ma swoje zakotwiczenie w postaci pkg_NazwaPakietu -
  gdzie NazwaPakietu to nazwa pakietu PEAR-a z rozró¿nieniem wielko¶ci
  liter.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

# class/test -> tests
install -d ./%{php_pear_dir}/tests/%{_pearname}
mv ./%{php_pear_dir}/{%{_class}/tests/*,tests/%{_pearname}}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
