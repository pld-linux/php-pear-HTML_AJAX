%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	AJAX
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - PHP and JavaScript library for AJAX
Summary(pl.UTF-8):	%{_pearname} - biblioteka PHP i JavaScript dla AJAX
Name:		php-pear-%{_pearname}
Version:	0.5.6
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	7c48eed37ae5730d144098f17c5676c4
URL:		http://pear.php.net/package/HTML_AJAX/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-12
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:4.3.0
Requires:	php-pear
Requires:	php-pear-PEAR-core >= 1:1.3.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides PHP and JavaScript libraries for performing AJAX
(Communication from JavaScript to your browser without reloading the
page).

Offers OO proxies in JavaScript of registered PHP or proxyless
operation. Serialization of data sent between PHP and JavaScript is
provided by a driver model, currently JSON and Null encodings are
provided.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ta klasa dostarcza biblioteki PHP i JavaScript do przeprowadzania AJAX
(komunikacji z JavaScriptu do przeglądarki bez przeładowywania
strony).

Oferuje zorientowane obiektowo proxy w JavaScripcie z zarejestrowanym
PHP lub operacje bez proxy. Serializacja danych przesyłanych pomiędzy
PHP i JavaScriptem jest zapewniana przez model sterowników, aktualnie
dostarczone są kodowania JSON i Null.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

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
%doc docs/%{_pearname}/{docs/*,examples}
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*
%{php_pear_dir}/data/%{_pearname}

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/%{_pearname}
