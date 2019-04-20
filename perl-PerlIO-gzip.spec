#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-PerlIO-gzip
Version  : 0.20
Release  : 9
URL      : https://cpan.metacpan.org/authors/id/N/NW/NWCLARK/PerlIO-gzip-0.20.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/N/NW/NWCLARK/PerlIO-gzip-0.20.tar.gz
Summary  : 'Perl extension to provide a PerlIO layer to gzip/gunzip'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-PerlIO-gzip-lib = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : pkgconfig(zlib)
BuildRequires : zlib-dev

%description
PerlIO::gzip version 0.20
=========================
A layer for the PerlIO system to transparently gzip/gunzip files.
**DON'T** trust it with your data.

%package dev
Summary: dev components for the perl-PerlIO-gzip package.
Group: Development
Requires: perl-PerlIO-gzip-lib = %{version}-%{release}
Provides: perl-PerlIO-gzip-devel = %{version}-%{release}

%description dev
dev components for the perl-PerlIO-gzip package.


%package lib
Summary: lib components for the perl-PerlIO-gzip package.
Group: Libraries

%description lib
lib components for the perl-PerlIO-gzip package.


%prep
%setup -q -n PerlIO-gzip-0.20

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/PerlIO/gzip.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/PerlIO::gzip.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/PerlIO/gzip/gzip.so
