Summary:	XML-RPC C library - an implementation of the xmlrpc protocol
Summary(pl):	Biblioteka XML-RPC C - implementacja protoko³u xmlrpc
Name:		xmlrpc-c
Version:	1.03.11
Release:	1
License:	XML-RPC C Library License
Group:		Libraries
Source0:	http://dl.sourceforge.net/xmlrpc-c/%{name}-%{version}.tgz
# Source0-md5:	f360fd8c42f0c7b85ce9903a07e64d55
Patch0:		%{name}-fastdep.patch
Patch1:		%{name}-libxml2-support.patch
Patch2:		%{name}-public-dispatch.patch
Patch3:		%{name}-soname.patch
Patch4:		%{name}-link.patch
URL:		http://xmlrpc-c.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	curl-devel
BuildRequires:	libxml2-devel
BuildRequires:	w3c-libwww-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_includedir	%{_prefix}/include/%{name}

%description
XML-RPC C library - an implementation of the xmlrpc protocol.

%description -l pl
Biblioteka XML-RPC C - implementacja protoko³u xmlrpc.

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
%patch4 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure \
	--enable-abyss-server \
	--enable-cgi-server \
	--enable-cplusplus \
	--enable-libxml2-backend \
	--enable-curl-client \
	--enable-libwww-client \
	--enable-unicode \
	--enable-abyss-threads

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

ln -s oldxmlrpc.h $RPM_BUILD_ROOT%{_includedir}/%{name}/xmlrpc.h
ln -s oldcppwrapper.hpp $RPM_BUILD_ROOT%{_includedir}/%{name}/XmlRpcCpp.h
ln -s server_cgi.h $RPM_BUILD_ROOT%{_includedir}/%{name}/xmlrpc_cgi.h
ln -s client.h $RPM_BUILD_ROOT%{_includedir}/%{name}/xmlrpc_client.h
ln -s server.h $RPM_BUILD_ROOT%{_includedir}/%{name}/xmlrpc_server.h
ln -s server_abyss.h $RPM_BUILD_ROOT%{_includedir}/%{name}/xmlrpc_server_abyss.h
ln -s server_w32httpsys.h $RPM_BUILD_ROOT%{_includedir}/%{name}/xmlrpc_server_w32httpsys.h

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README doc/{COPYING,CREDITS,HISTORY,SECURITY,TESTING,TODO}
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/DEVELOPING
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_libdir}/lib*\+\+.a
%{_includedir}/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*[^\+\+].a
