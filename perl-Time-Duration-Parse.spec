%define upstream_name    Time-Duration-Parse
%define upstream_version 0.11

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Parse string that represents time duration

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Time/%{upstream_name}-%{upstream_version}.tar.gz

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
%setup -q -n %{upstream_name}-%{upstream_version}

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


