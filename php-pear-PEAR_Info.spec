%include	/usr/lib/rpm/macros.php
%define         _class          PEAR
%define         _subclass       Info
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - Show Information about your PEAR install and its packages
Summary(pl):	%{_pearname} - pokazywanie informacji o instalacji PEAR-a i jego pakietach
Name:		php-pear-%{_pearname}
Version:	1.0.6
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
# Source0-md5:	a8d4b23e20c6648eaf3b1c3eeb520b3f
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/package/%{_pearname}/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
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

This class has in PEAR status: %{_status}.

%description -l pl
Ten pakiet generuje wyczerpuj�c� stron� informacyjn� o aktualnej
instalacji PEAR-a.
- Format strony jest podobny do formatu phpinfo() opr�cz u�ytych
  kolor�w PEAR-a.
- Ma pe�n� list� zas�ug PEAR-a (opart� na zainstalowanych pakietach).
- Pokazuje, czy jest nowsza wersja zainstalowanych klas (i jaki jest
  ich status).
- Ka�dy pakiet ma swoje zakotwiczenie w postaci pkg_NazwaPakietu -
  gdzie NazwaPakietu to nazwa pakietu PEAR-a z rozr�nieniem wielko�ci
  liter.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php