# $Id$
# Authority: shuff
# Upstream: R. Kyle Murphy <orclev$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Convert-Bencode

Summary: Functions for converting to/from bencoded strings
Name: perl-%{real_name}
Version: 1.03
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Convert-Bencode/

Source: http://search.cpan.org/CPAN/authors/id/O/OR/ORCLEV/Convert-Bencode-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More) >= 0.45
BuildRequires: rpm-macros-rpmforge
Requires: perl

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
This module provides two functions, bencode and bdecode, which encode and
decode bencoded strings respectively.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes LICENSE INSTALL MANIFEST README
%doc %{_mandir}/man?/*
%dir %{perl_vendorlib}/Convert/
%{perl_vendorlib}/Convert/*

%changelog
* Thu Oct 29 2009 Steve Huff <shuff@vecna.org> - 1.03-1
- Initial package.
