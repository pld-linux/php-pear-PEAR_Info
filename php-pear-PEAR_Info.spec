%include	/usr/lib/rpm/macros.php
%define		_class		PEAR
%define		_subclass	Info
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - show Information about your PEAR install and its packages
Summary(pl.UTF-8):	%{_pearname} - pokazywanie informacji o instalacji PEAR-a i jego pakietach
Name:		php-pear-%{_pearname}
Version:	1.9.2
Release:	3
Epoch:		0
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	a10ff525d7edd407daba83f8a2f85b38
URL:		http://pear.php.net/package/PEAR_Info/
BuildRequires:	php-pear-PEAR >= 1:1.5.4
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:4.1.0
Requires:	php-pcre
Requires:	php-pear
Requires:	php-pear-Console_Getargs >= 1.3.3
Requires:	php-pear-PEAR >= 1:1.3.2
Suggests:	php-pear-PHPUnit
Obsoletes:	php-pear-PEAR_Info-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	pear(PHPUnit.*)

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

%description -l pl.UTF-8
Ten pakiet generuje wyczerpującą stronę informacyjną o aktualnej
instalacji PEAR-a.
- Format strony jest podobny do formatu phpinfo() oprócz użytych
  kolorów PEAR-a.
- Ma pełną listę zasług PEAR-a (opartą na zainstalowanych pakietach).
- Pokazuje, czy jest nowsza wersja zainstalowanych klas (i jaki jest
  ich status).
- Każdy pakiet ma swoje zakotwiczenie w postaci pkg_NazwaPakietu -
  gdzie NazwaPakietu to nazwa pakietu PEAR-a z rozróżnieniem wielkości
  liter.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

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
%{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/data/%{_pearname}
