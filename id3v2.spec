%define	name	id3v2
%define	version	0.1.12
%define	release %mkrel 2

Summary:	A command line id3v2 tag editor
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://prdownloads.sourceforge.net/id3v2/%{name}-%{version}.tar.bz2
License:	GPLv2+
Group:		Sound
URL:		http://id3v2.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	libid3-devel

%description
id3v2 is a command line id3v2 tag editor.
You can add/modifiy/delete id3v2 tags and convert
id3v1 tags to id3v2 tags.

%prep
%setup -q

%build
%make clean
%make

%install
rm -rf $RPM_BUILD_ROOT
install -m755 id3v2 -D $RPM_BUILD_ROOT%{_bindir}/id3v2
install -m644 id3v2.1 -D $RPM_BUILD_ROOT%{_mandir}/man1/id3v2.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README INSTALL
%{_bindir}/id3v2
%{_mandir}/man1/id3v2.1*


%changelog
* Mon Jul 11 2011 Götz Waschk <waschk@mandriva.org> 0.1.12-2mdv2011
+ Revision: 689503
- rebuild

* Sat Jul 10 2010 Götz Waschk <waschk@mandriva.org> 0.1.12-1mdv2011.0
+ Revision: 550360
- fix build
- new version
- drop patch
- update license

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.1.11-9mdv2009.0
+ Revision: 247199
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Oct 23 2007 Götz Waschk <waschk@mandriva.org> 0.1.11-7mdv2008.1
+ Revision: 101493
- fix bug 34944 (double free crash)

* Wed Jul 25 2007 Götz Waschk <waschk@mandriva.org> 0.1.11-6mdv2008.0
+ Revision: 55235
- Import id3v2



* Thu Jul 20 2006 Götz Waschk <waschk@mandriva.org> 0.1.11-1mdv2007.0
- Rebuild

* Mon Feb 06 2006 Götz Waschk <waschk@mandriva.org> 0.1.11-5mdk
- Rebuild
- use mkrel

* Mon Feb 07 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.1.11-4mdk
- even better description:p

* Sat Feb 05 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.1.11-3mdk
- better description
- cosmetics

* Tue Jun 15 2004 GØtz Waschk <waschk@linux-mandrake.com> 0.1.11-2mdk
- rebuild for new g++

* Wed May  5 2004 GØtz Waschk <waschk@linux-mandrake.com> 0.1.11-1mdk
- drop prefix
- add source url
- new version

* Fri Apr  4 2003 GØtz Waschk <waschk@linux-mandrake.com> 0.1.9-2mdk
- new id3lib

* Tue Feb 25 2003 GØtz Waschk <waschk@linux-mandrake.com> 0.1.9-1mdk
- drop patch
- new version

* Mon Feb 24 2003 GØtz Waschk <waschk@linux-mandrake.com> 0.1.8-1mdk
- patch in missing namespace to make it compile
- new version

* Sat Dec 28 2002 GØtz Waschk <waschk@linux-mandrake.com> 0.1.7-2mdk
- arrgh, don't use the included binaries

* Fri Dec 27 2002 GØtz Waschk <waschk@linux-mandrake.com> 0.1.7-1mdk
- new version

* Mon Nov 25 2002 GØtz Waschk <waschk@linux-mandrake.com> 0.1.5-6mdk
- rebuild with new id3lib

* Mon Nov  4 2002 GØtz Waschk <waschk@linux-mandrake.com> 0.1.5-5mdk
- rebuild with new id3lib

* Fri Aug 16 2002 GØtz Waschk <waschk@linux-mandrake.com> 0.1.5-4mdk
- gcc 3.2-0.3mdk build

* Mon Jul 29 2002 GØtz Waschk <waschk@linux-mandrake.com> 0.1.5-3mdk
- gcc3.2

* Tue May 28 2002 GØtz Waschk <waschk@linux-mandrake.com> 0.1.5-2mdk
- gcc3.1

* Mon Feb 18 2002 GØtz Waschk <waschk@linux-mandrake.com> 0.1.5-1mdk
- initial package
