# $Id$
# Authority: dries
# Upstream: Greg Bacon <gbacon$hiwaay,net>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name News-Scan

Summary: Gather and report Usenet newsgroup statistics
Name: perl-News-Scan
Version: 0.53
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/News-Scan/

Source: http://search.cpan.org/CPAN/authors/id/G/GB/GBACON/News-Scan-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This distribution provides a mechanism for collecting articles from a
set of Usenet newsgroups and then creating statistical reports about
those groups.

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
%{perl_vendorlib}/News/Scan.pm
%{perl_vendorlib}/News/Scan

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.53-1
- Initial package.
