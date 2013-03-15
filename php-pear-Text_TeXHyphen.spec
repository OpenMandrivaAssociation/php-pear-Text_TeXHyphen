%define		_class		Text
%define		_subclass	TeXHyphen
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	0.1.0
Release:	17
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

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/docs/*
%{_datadir}/pear/%{_class}
%{_datadir}/pear/data/%{upstream_name}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-16mdv2012.0
+ Revision: 742291
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-15
+ Revision: 679596
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-14mdv2011.0
+ Revision: 613786
- the mass rebuild of 2010.1 packages

* Sun Nov 15 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.0-13mdv2010.1
+ Revision: 466327
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.1.0-12mdv2010.0
+ Revision: 441661
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-11mdv2009.1
+ Revision: 322679
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-10mdv2009.0
+ Revision: 237148
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Apr 20 2007 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-9mdv2008.0
+ Revision: 15503
- rule out the PHPUnit.php dep


* Sat Mar 10 2007 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-8mdv2007.1
+ Revision: 140463
- fix deps

* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-7mdv2007.0
+ Revision: 82759
- Import php-pear-Text_TeXHyphen

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-7mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-1mdk
- initial Mandriva package (PLD import)

