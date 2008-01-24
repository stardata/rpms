# $Id$
# Authority: dries
# Upstream: Steven Schubiger <schubiger$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Dir-Split

Summary: Split files of a directory to subdirectories
Name: perl-Dir-Split
Version: 0.79
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Dir-Split/

Source: http://www.cpan.org/modules/by-module/Dir/Dir-Split-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
#BuildRequires: perl(Test::More)

%description
Split files of a directory to subdirectories.

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
%doc Changes INSTALL MANIFEST META.yml README TODO
%doc %{_mandir}/man3/Dir::Split.3pm*
%dir %{perl_vendorlib}/Dir/
#%{perl_vendorlib}/Dir/Split/
%{perl_vendorlib}/Dir/Split.pm

%changelog
* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 0.79-1
- Updated to release 0.79.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.78-1
- Initial package.
