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
