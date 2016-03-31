Name:		mg
Version:	20090107
Release:	6%{?dist}
Summary:	Tiny Emacs-like editor

Group:		Applications/Editors
License:	BSD and ISC and MirOS
URL:		http://homepage.boetes.org/software/mg/
Source0:	http://homepage.boetes.org/software/mg/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	ncurses-devel

%description
mg is a tiny, mostly public-domain Emacs-like editor included in the base 
OpenBSD system. It is compatible with Emacs because there shouldn't be any 
reason to learn more editor types than Emacs or vi.

%prep
%setup -q

%build
# configure takes no arguments and will fail if you give it any, therefore we
# do not use the configure macro here
./configure
make %{?_smp_mflags} CFLAGS="%{optflags}" LDFLAGS="%{optflags} -lncurses" libdir="%{_libdir}"

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} prefix=%{_prefix} mandir=%{_mandir} \
     INSTALL='install -p'

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README tutorial
%{_bindir}/mg
%{_mandir}/man1/mg.1.*

%changelog
* Wed Oct 6 2010 Mark McKinstry <mmckinst@nexcess.net> - 20090107-6
- update Source0 line to use macros

* Tue Oct 5 2010 Mark McKinstry <mmckinst@nexcess.net> - 20090107-4
- add libdir to build
- update license

* Sat May 8 2010 Mark McKinstry <mmckinst@nexcess.net> - 20090107-3
- switch to one style of RPM macros
- include LDFLAGS

* Wed Apr 28 2010 Mark McKinstry <mmckinst@nexcess.net> - 20090107-2
- update license
- apply patch from Terje Rosten to preserve timstamps on man page, handle
  changes in compression of man pages more robustly, include CFLAGS, and include
  debug info

* Tue Apr 27 2010 Mark McKinstry <mmckinst@nexcess.net> - 20090107-1
- initial build
