%define		status		alpha
%define		pearname	Console_Color2
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - This Class allows you to easily use ANSI console colors in your application
Name:		php-pear-Console_Color2
Version:	0.1.2
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	5129750dc173eed2fe40be406e178ff2
URL:		http://pear.php.net/package/Console_Color2/
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
You can use Console_Color::convert to transform colorcodes like %r
into ANSI control codes. $console = new Console_Color2(); print
$console->convert("%rHello World!%n"); would print "Hello World" in
red, for example.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

mv docs/Console_Color2/examples .
mv docs/Console_Color2/* .
mv .%{php_pear_dir}/data/Console_Color2/composer.json .

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README LICENSE
%doc ChangeLog install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Console/Color2.php
