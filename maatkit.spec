%include	/usr/lib/rpm/macros.perl
Summary:	Essential command-line utilities for MySQL
Name:		maatkit
Version:	7486
Release:	1
License:	GPL v2
Group:		Applications/Databases
Source0:	http://maatkit.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	09cfee182e14fc6e16ec33aa681ffb47
Source1:	%{name}.conf
URL:		http://www.maatkit.org/
BuildRequires:	perl-ExtUtils-MakeMaker
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-DBD-mysql >= 1.0
Requires:	perl-DBI >= 1.13
Requires:	perl-Term-ReadKey >= 2.10
Obsoletes:	mysqldumpgrants
Obsoletes:	mysqltoolkit
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Maatkit makes MySQL easier and safer to manage. It provides simple,
predictable ways to do things you cannot otherwise do. It would be
nice if these features were included with MySQL, but they are not.

You can use Maatkit to prove replication is working correctly, fix
corrupted data, automate repetitive tasks, speed up your servers, and
much, much more.

This toolkit contains essential command-line utilities for MySQL, such
as a table checksum tool and query profiler. It provides missing
features such as checking slaves for data consistency, with emphasis
on quality and scriptability.

Each utility is completely stand-alone, without dependencies other
than core Perl and the DBI drivers needed to connect to MySQL.

%description -l pl.UTF-8
MySQL Toolkit to zbiór ważnych narzędzi uruchamianych z linii poleceń
dla MySQL-a. Każde z nich jest w pełni samodzielne, bez zależności
większych niż podstawowa instalacja Perla i terowniki DBI potrzebne do
połączenia z bazą MySQL.

%prep
%setup -q

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
%{__make} pure_install \
	PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

cp -a %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/auto/%{name}/.packlist
%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/%{name}.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog
%dir %{_sysconfdir}/%{name}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/%{name}.conf
%attr(755,root,root) %{_bindir}/mk-*
%{_mandir}/man1/maatkit.1p*
%{_mandir}/man1/mk-*
