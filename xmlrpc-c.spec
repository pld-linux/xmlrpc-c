Summary:	XML-RPC C library - an implementation of the xmlrpc protocol
Summary(pl):	Biblioteka XML-RPC C - implementacja protoko³u xmlrpc
Name:		xmlrpc-c
Version:	0.9.10
Release:	1
License:	XML-RPC C Library License
Group:		Libraries
Source0:	http://download.sourceforge.net/xmlrpc-c//%{name}-%{version}.tar.gz
# Source0-md5:	847410fae881f0fb641a186db6c8c015
Patch0:		%{name}-fastdep.patch
Patch1:		%{name}-libxml2-support.patch
Patch2:		%{name}-preinvoke.patch
Patch3:		%{name}-public-dispatch.patch
URL:		http://xmlrpc-c.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	w3c-libwww-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_includedir	%{_prefix}/include/%{name}

%description
XML-RPC C library - an implementation of the xmlrpc protocol

%package devel
Summary:	Header files etc to develop XML-RPC applications
Summary(pl):	Pliki nag³ówkowe do tworzenia aplikacji XML-RPC
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files etc needed to develop XML-RPC applications.

%description devel -l pl
Pliki nag³ówkowe potrzebne do tworzenia aplikacji u¿ywaj±cych XML-RPC.

%package static
Summary:	Static XML-RPC C libraries
Summary(pl):	Biblioteki statyczne XML-RPC C
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static XML-RPC C libraries.

%description static -l pl
Biblioteki statyczne XML-RPC C.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-cplusplus \
	--disable-abyss-server \
	--disable-cgi-server \
	--enable-libxml2-backend
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so*
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%doc COPYING NEWS README BUGS PORTING REFACTORINGS SECURITY TESTING
%{_libdir}/lib*.la
%{_includedir}

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
