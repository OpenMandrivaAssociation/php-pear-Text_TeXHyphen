%define		_class		Text
%define		_subclass	TeXHyphen
%define		upstream_name	%{_class}_%{_subclass}

%define		_requires_exceptions pear(TEXT/TeXHyphen/Pattern.php)\\|pear(Text/TeXHyphen/ObjectHash.php)\\|pear(PHPUnit.php)

Name:		php-pear-%{upstream_name}
Version:	0.1.0
Release:	%mkrel 15
Summary:	Automated word hyphenation with the TeX algorithm
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Text_TeXHyphen/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This package implements the TeX hyphenation algorithm based on
pattern.

The package can support various backends for pattern retrieval. At
this stage only flat files with TeX pattern were implemented. The
advantage of the TeX pattern is the available multi-language support.
Currently German, Oxford and American English are supported.

For speed purposes an interface for a cache of hyphenated words was
implemented.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
rm -rf %{buildroot}

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}

%post
%if %mdkversion < 201000
pear install --nodeps --soft --force --register-only \
    %{_datadir}/pear/packages/%{upstream_name}.xml >/dev/null || :
%endif

%preun
%if %mdkversion < 201000
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null || :
fi
%endif

%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/docs/*
%{_datadir}/pear/%{_class}
%{_datadir}/pear/data/%{upstream_name}
%{_datadir}/pear/packages/%{upstream_name}.xml
