%include	/usr/lib/rpm/macros.perl
Summary:	Essential command-line utilities for MySQL
Name:		maatkit
Version:	2152
Release:	1
License:	GPL v2
Group:		Applications/Databases
URL:		http://www.maatkit.org/
Source0:	http://maatkit.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	2ab216169f323f432d557d20cd7b9cdb
BuildRequires:	perl-ExtUtils-MakeMaker
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-DBD-mysql >= 1.0
Requires:	perl-DBI >= 1.13
Requires:	perl-Term-ReadKey >= 2.10
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Maatkit makes MySQL easier and safer to manage. It provides simple,
predictable ways to do things you cannot otherwise do. It would be
nice if these features were included with MySQL, but they are not.

You can use Maatkit to prove replication is working correctly, fix
corrupted data, automate repetitive tasks, speed up your servers, and
much, much more.

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
