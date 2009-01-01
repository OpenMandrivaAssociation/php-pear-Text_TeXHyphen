%define		_class		Text
%define		_subclass	TeXHyphen
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

%define		_requires_exceptions pear(TEXT/TeXHyphen/Pattern.php)\\|pear(Text/TeXHyphen/ObjectHash.php)\\|pear(PHPUnit.php)

Summary:	%{_pearname} - automated word hyphenation with the TeX algorithm
Name:		php-pear-%{_pearname}
Version:	0.1.0
Release:	%mkrel 11
License:	PHP License
Group:		Development/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tar.bz2
URL:		http://pear.php.net/package/Text_TeXHyphen/
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	dos2unix
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This package implements the TeX hyphenation algorithm based on
pattern.

The package can support various backends for pattern retrieval. At
this stage only flat files with TeX pattern were implemented. The
advantage of the TeX pattern is the available multi-language support.
Currently German, Oxford and American English are supported.

For speed purposes an interface for a cache of hyphenated words was
implemented.

In PEAR status of this package is: %{_status}.

%prep

%setup -q -c

find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;

for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -rf $i; fi >&/dev/null
done

# strip away annoying ^M
find -type f | grep -v ".gif" | grep -v ".png" | grep -v ".jpg" | xargs dos2unix -U

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/{PatternDB,WordCache}

install -m0644 %{_pearname}-%{version}/%{_class}/*.php %{buildroot}%{_datadir}/pear/%{_class}
install -m0644 %{_pearname}-%{version}/%{_class}/%{_subclass}/*.php %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}
install -m0644 %{_pearname}-%{version}/%{_class}/%{_subclass}/PatternDB/*.php %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/PatternDB
install -m0644 %{_pearname}-%{version}/%{_class}/%{_subclass}/WordCache/*.php %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/WordCache

install -d %{buildroot}%{_datadir}/pear/packages
install -m0644 package.xml %{buildroot}%{_datadir}/pear/packages/%{_pearname}.xml

%post
if [ "$1" = "1" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear install --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi
if [ "$1" = "2" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear upgrade -f --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi

%preun
if [ "$1" = 0 ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear uninstall --nodeps -r %{_pearname}
	fi
fi

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/{data,docs,tests}
%{_datadir}/pear/%{_class}/*.php
%{_datadir}/pear/%{_class}/%{_subclass}
%{_datadir}/pear/packages/%{_pearname}.xml
