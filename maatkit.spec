%include	/usr/lib/rpm/macros.perl
Summary:	Essential command-line utilities for MySQL
Name:		maatkit
Version:	1877
Release:	0.1
License:	GPL
Group:		Applications/Databases
URL:		http://sourceforge.net/projects/maatkit/
Source0:	http://dl.sourceforge.net/maatkit/%{name}-%{version}.tar.gz
# Source0-md5:	5c52b18a5eb8e510f48c4b9a1f6df71d
BuildRequires:	perl-ExtUtils-MakeMaker
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-DBD-MySQL >= 1.0
Requires:	perl-DBI >= 1.13
Requires:	perl-TermReadKey >= 2.10
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This toolkit contains essential command-line utilities for MySQL, such
as a table checksum tool and query profiler. It provides missing
features such as checking slaves for data consistency, with emphasis
on quality and scriptability.

%prep
%setup -q

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} pure_install \
	PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/auto/maatkit/.packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc INSTALL Changelog*
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/maatkit.pm
%{perl_vendorlib}/maatkitdsn.pm
%{_mandir}/man1/*.1*
%{_mandir}/man3/*.3*
