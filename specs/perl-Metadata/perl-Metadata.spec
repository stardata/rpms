# $Id$
# Authority: dries
# Upstream: Dave Beckett <dave$dajobe,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Metadata

Summary: Metadata
Name: perl-Metadata
Version: 0.24
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Metadata/

Source: http://search.cpan.org/CPAN/authors/id/D/DJ/DJBECKETT/Metadata-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This collection of modules provide an implementation of Dublin Core
compatible metadata and subclasses for IAFA Templates, SOIF (Harvest)
and should be easily extendible to similar (fairly flat) metadata
formats.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Metadata

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.24-1
- Initial package.
