%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	AJAX
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - PHP and JavaScript library for AJAX
Summary(pl):	%{_pearname} - biblioteka PHP i JavaScript dla AJAX
Name:		php-pear-%{_pearname}
Version:	0.1.4
Release:	1.1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	a44db3886d9a05f72b27befcb136962e
URL:		http://pear.php.net/package/HTML_AJAX/
BuildRequires:	rpm-php-pearprov >= 4.4.2-12
Requires:	php-common >= 3:4.3.0
Requires:	php-pear
Requires:	php-pear-PEAR >= 1:1.3.5
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

%description -l pl
Ta klasa dostarcza biblioteki PHP i JavaScript do przeprowadzania AJAX
(komunikacji z JavaScriptu do przegl±darki bez prze³adowywania
strony).

Oferuje zorientowane obiektowo proxy w JavaScripcie z zarejestrowanym
PHP lub operacje bez proxy. Serializacja danych przesy³anych pomiêdzy
PHP i JavaScriptem jest zapewniana przez model sterowników, aktualnie
dostarczone s± kodowania JSON i Null.

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
%doc docs/%{_pearname}/{docs/*,examples}
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*

%{php_pear_dir}/data/%{_pearname}
