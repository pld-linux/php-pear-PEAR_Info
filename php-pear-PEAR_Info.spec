%include	/usr/lib/rpm/macros.php
%define		_class		PEAR
%define		_subclass	Info
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - show Information about your PEAR install and its packages
Summary(pl):	%{_pearname} - pokazywanie informacji o instalacji PEAR-a i jego pakietach
Name:		php-pear-%{_pearname}
Version:	1.5.2
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	394548409e74b7fe207ec617025bf1fe
URL:		http://pear.php.net/package/PEAR_Info/
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
%doc %{_pearname}-%{version}/tests
%{php_pear_dir}/%{_class}/*.php
