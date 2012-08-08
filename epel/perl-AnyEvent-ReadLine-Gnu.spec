Name:           perl-AnyEvent-ReadLine-Gnu
Version:        1.0
Release:        1%{?dist}
Summary:        AnyEvent::ReadLine::Gnu - event-based interface to Term::ReadLine::Gnu

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            https://github.com/jelu/anyevent-readline-gnu/
Source0:        anyevent-readline-gnu-%{version}.tar.gz
Patch0:         perl-AnyEvent-ReadLine-Gnu_compat-ae-5.0.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
# Needed for test
BuildRequires:  perl(Test::Simple)

Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
The Term::ReadLine module family is bizarre (and you are encouraged not
to look at its sources unless you want to go blind). It does support
event-based operations, somehow, but it's hard to figure out.

It also has some utility functions for printing messages asynchronously,
something that, again, isn't obvious how to do.

This module has figured it all out for you, once and for all.

%package -n rltelnet
Summary: rltelnet - connect to a socket with readline frontend
Group: Applications/Communications
Version: 1.0
%description -n rltelnet
This program connects to a socket using AnyEvent::Socket::tcp_connect, prints
everything it receives from the socket and offers a readline editing interface
to send lines to the socket.

This is very remotely what telnet does when used on a non-telnet socket,
except that it uses readline and supports more types of socketsd (e.g.
unix domain sockets).


%prep
%setup -q -n anyevent-readline-gnu
%patch0 -p1


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'


%check
make test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes COPYING README
%{perl_vendorlib}/AnyEvent*
%{_mandir}/man3/*.3*

%files -n rltelnet
%{_bindir}/rltelnet
%{_mandir}/man1/*.1*


%changelog
* Tue Aug 07 2012 Jerry Lundström < lundstrom.jerry at gmail.com > - 1.0-1
- Initial package for Fedora

