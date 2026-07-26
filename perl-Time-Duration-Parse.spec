%define upstream_name    Time-Duration-Parse
Name:		perl-%{upstream_name}
Version:	0.11
Release:	4

Summary:	Parse string that represents time duration

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Time/%{upstream_name}-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Exporter::Lite)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Time::Duration)
BuildArch:	noarch

%description
Time::Duration::Parse is a module to parse human readable duration strings
like _2 minutes and 3 seconds_ to seconds.

It does the opposite of _duration_exact_ function in Time::Duration and is
roundtrip safe. So, the following is always true.

  use Time::Duration::Parse;
  use Time::Duration;

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*


