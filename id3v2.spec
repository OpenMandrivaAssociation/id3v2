%global debug_package %{nil}

Summary:	A command line id3v2 tag editor
Name:		id3v2
Version:	0.1.12
Release:	6
Source0:	http://prdownloads.sourceforge.net/id3v2/%{name}-%{version}.tar.bz2
License:	GPLv2+
Group:		Sound
URL:		http://id3v2.sourceforge.net/
BuildRequires:	id3lib-devel

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
install -m755 id3v2 -D $RPM_BUILD_ROOT%{_bindir}/id3v2
install -m644 id3v2.1 -D $RPM_BUILD_ROOT%{_mandir}/man1/id3v2.1

%clean

%files
%doc README INSTALL
%{_bindir}/id3v2
%{_mandir}/man1/id3v2.1*
