Summary:	XML-RPC C library - an implementation of the xmlrpc protocol
Summary(pl.UTF-8):	Biblioteka XML-RPC C - implementacja protokołu xmlrpc
Name:		xmlrpc-c
Version:	1.26.2
Release:	1
License:	XML-RPC for C License (BSD-like)
Group:		Libraries
# svn co http://xmlrpc-c.svn.sourceforge.net/svnroot/xmlrpc-c/advanced xmlrpc-c
# Unfortunately, upstream does not tag versions so we must fetch from the branch
# and check which version was used for it
# 1.26.2 is svn r2131
Source0:	%{name}-%{version}.tar.xz
# Source0-md5:	b61e1ace6c3c69b152fbad35fa7144de
Patch0:		%{name}-fastdep.patch
Patch1:		%{name}-soname.patch
Patch2:		%{name}-cflags.patch
# patches 10+ come from Fedora
Patch10:	%{name}-cmake.patch
Patch11:	%{name}-printf-size_t.patch
Patch12:	%{name}-longlong.patch
Patch13:	%{name}-uninit-curl.patch
Patch14:	%{name}-30x-redirect.patch
Patch15:	%{name}-check-vasprintf-return-value.patch
Patch16:	%{name}-include-string_int.h.patch
URL:		http://xmlrpc-c.sourceforge.net/
BuildRequires:	cmake >= 2.6
BuildRequires:	curl-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	ncurses-devel >= 5.7-21
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
BuildRequires:	rpmbuild(macros) >= 1.577
BuildRequires:	tar >= 1:1.22
BuildRequires:	w3c-libwww-devel >= 5.4.0-11
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML-RPC is a quick-and-easy way to make procedure calls over the
Internet. It converts the procedure call into XML document, sends it
to a remote server using HTTP, and gets back the response as XML.

This library provides a modular implementation of XML-RPC for C.

%description -l pl.UTF-8
XML-RPC to szybki i łatwy w użyciu sposób wywoływania procedur poprzez
Internet. Przekształca wywołanie procedury na dokument XML, wysyła do
zdalnego serwera poprzez HTTP i odbiera odpowiedź jako XML.

Ta biblioteka udostepnia modularną implementacją XML-RPC dla języka C.

%package c++
Summary:	C++ libraries for xmlrpc-c
Summary(pl.UTF-8):	Biblioteki C++ xmlrpc-c
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Conflicts:	xmlrpc-c < 1.20.3-1

%description c++
XML-RPC is a quick-and-easy way to make procedure calls over the
Internet. It converts the procedure call into XML document, sends it
to a remote server using HTTP, and gets back the response as XML.

This library provides a modular implementation of XML-RPC for C++.

%description c++ -l pl.UTF-8
XML-RPC to szybki i łatwy w użyciu sposób wywoływania procedur poprzez
Internet. Przekształca wywołanie procedury na dokument XML, wysyła do
zdalnego serwera poprzez HTTP i odbiera odpowiedź jako XML.

Ta biblioteka udostepnia modularną implementacją XML-RPC dla języka
C++.

%package client
Summary:	C client library for xmlrpc-c
Summary(pl.UTF-8):	Biblioteka kliencka C xmlrpc-c
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Conflicts:	xmlrpc-c < 1.20.3-1

%description client
XML-RPC is a quick-and-easy way to make procedure calls over the
Internet. It converts the procedure call into XML document, sends it
to a remote server using HTTP, and gets back the response as XML.

This library provides a modular implementation of XML-RPC for C
clients.

%description client -l pl.UTF-8
XML-RPC to szybki i łatwy w użyciu sposób wywoływania procedur poprzez
Internet. Przekształca wywołanie procedury na dokument XML, wysyła do
zdalnego serwera poprzez HTTP i odbiera odpowiedź jako XML.

Ta biblioteka udostepnia modularną implementacją XML-RPC dla klientów
w języku C.

%package client++
Summary:	C++ client library for xmlrpc-c
Summary(pl.UTF-8):	Biblioteka kliencka C++ xmlrpc-c
Group:		Libraries
Requires:	%{name}-c++ = %{version}-%{release}
Requires:	%{name}-client = %{version}-%{release}
Conflicts:	xmlrpc-c < 1.20.3-1

%description client++
XML-RPC is a quick-and-easy way to make procedure calls over the
Internet. It converts the procedure call into XML document, sends it
to a remote server using HTTP, and gets back the response as XML.

This library provides a modular implementation of XML-RPC for C++
clients.

%description client++ -l pl.UTF-8
XML-RPC to szybki i łatwy w użyciu sposób wywoływania procedur poprzez
Internet. Przekształca wywołanie procedury na dokument XML, wysyła do
zdalnego serwera poprzez HTTP i odbiera odpowiedź jako XML.

Ta biblioteka udostepnia modularną implementacją XML-RPC dla klientów
w języku C++.

%package apps
Summary:	Sample XML-RPC applications
Summary(pl.UTF-8):	Przykładowe aplikacje XML-RPC
Group:		Applications/Networking
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-c++ = %{version}-%{release}
Requires:	%{name}-client = %{version}-%{release}
Requires:	%{name}-client++ = %{version}-%{release}

%description apps
XML-RPC is a quick-and-easy way to make procedure calls over the
Internet. It converts the procedure call into XML document, sends it
to a remote server using HTTP, and gets back the response as XML.

This package contains some handy XML-RPC demo applications.

%description apps -l pl.UTF-8
XML-RPC to szybki i łatwy w użyciu sposób wywoływania procedur poprzez
Internet. Przekształca wywołanie procedury na dokument XML, wysyła do
zdalnego serwera poprzez HTTP i odbiera odpowiedź jako XML.

Ten pakiet zawiera kilka podręcznych aplikacji demonstracyjnych
XML-RPC.

%package devel
Summary:	Header files etc to develop XML-RPC applications
Summary(pl.UTF-8):	Pliki nagłówkowe do tworzenia aplikacji XML-RPC
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-c++ = %{version}-%{release}
Requires:	%{name}-client = %{version}-%{release}
Requires:	%{name}-client++ = %{version}-%{release}
Requires:	curl-devel
Requires:	expat-devel
Requires:	libstdc++-devel
Requires:	libxml2-devel >= 2.0
Requires:	w3c-libwww-devel
Obsoletes:	xmlrpc-c-static

%description devel
Header files etc needed to develop XML-RPC applications.

%description devel -l pl.UTF-8
Pliki nagłówkowe potrzebne do tworzenia aplikacji używających XML-RPC.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch2 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch1 -p1

%build
mkdir -p build
cd build
%cmake .. \
	-D_lib:STRING=%{_lib} \
	-DCMAKE_C_FLAGS_RELEASE="-DNDEBUG" \
	-DCMAKE_CXX_FLAGS_RELEASE="-DNDEBUG" \
	-DMUST_BUILD_CURL_CLIENT:BOOL=ON \
	-DMUST_BUILD_LIBWWW_CLIENT:BOOL=ON \
	-DBUILD_SHARED_LIBS:BOOL=ON \
	-DENABLE_TOOLS:BOOL=ON

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \

chmod +x $RPM_BUILD_ROOT%{_libdir}/*.so*

# Win32-specific
%{__rm} $RPM_BUILD_ROOT%{_includedir}/xmlrpc_server_w32httpsys.h \
	$RPM_BUILD_ROOT%{_includedir}/xmlrpc-c/server_w32httpsys.h

# why??? man is still packaged  --q
%{__rm} $RPM_BUILD_ROOT%{_bindir}/xml-rpc-api2txt

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	client -p /sbin/ldconfig
%postun client -p /sbin/ldconfig

%post	c++ -p /sbin/ldconfig
%postun	c++ -p /sbin/ldconfig

%post	client++ -p /sbin/ldconfig
%postun	client++ -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README doc/{COPYING,CREDITS,HISTORY,SECURITY,TODO}
%attr(755,root,root) %{_libdir}/libxmlrpc-c.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libxmlrpc-c.so.3
%attr(755,root,root) %{_libdir}/libxmlrpc_abyss.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libxmlrpc_abyss.so.3
%attr(755,root,root) %{_libdir}/libxmlrpc_server.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libxmlrpc_server.so.3
%attr(755,root,root) %{_libdir}/libxmlrpc_server_abyss.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libxmlrpc_server_abyss.so.3
%attr(755,root,root) %{_libdir}/libxmlrpc_server_cgi.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libxmlrpc_server_cgi.so.3
%attr(755,root,root) %{_libdir}/libxmlrpc_util.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libxmlrpc_util.so.3

%files client
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxmlrpc_client.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libxmlrpc_client.so.3

%files c++
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxmlrpc++.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libxmlrpc++.so.7
%attr(755,root,root) %{_libdir}/libxmlrpc_cpp.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libxmlrpc_cpp.so.7
%attr(755,root,root) %{_libdir}/libxmlrpc_packetsocket.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libxmlrpc_packetsocket.so.7
%attr(755,root,root) %{_libdir}/libxmlrpc_server++.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libxmlrpc_server++.so.7
%attr(755,root,root) %{_libdir}/libxmlrpc_server_abyss++.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libxmlrpc_server_abyss++.so.7
%attr(755,root,root) %{_libdir}/libxmlrpc_server_cgi++.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libxmlrpc_server_cgi++.so.7
%attr(755,root,root) %{_libdir}/libxmlrpc_server_pstream++.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libxmlrpc_server_pstream++.so.7

%files client++
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxmlrpc_client++.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libxmlrpc_client++.so.7

%files apps
%defattr(644,root,root,755)
%doc tools/xmlrpc/xmlrpc.html tools/xmlrpc_transport/xmlrpc_transport.html
%attr(755,root,root) %{_bindir}/xmlrpc
%attr(755,root,root) %{_bindir}/xmlrpc_transport
%attr(755,root,root) %{_bindir}/xml-rpc-api2cpp
%attr(755,root,root) %{_bindir}/xmlrpc_cpp_proxy
%attr(755,root,root) %{_bindir}/xmlrpc_pstream
%{_mandir}/man1/xml-rpc-api2cpp.1*
%{_mandir}/man1/xml-rpc-api2txt.1*

%files devel
%defattr(644,root,root,755)
%doc doc/{DEVELOPING,TESTING}
%attr(755,root,root) %{_bindir}/xmlrpc-c-config
# C
%attr(755,root,root) %{_libdir}/libxmlrpc-c.so
%attr(755,root,root) %{_libdir}/libxmlrpc_abyss.so
%attr(755,root,root) %{_libdir}/libxmlrpc_client.so
%attr(755,root,root) %{_libdir}/libxmlrpc_server.so
%attr(755,root,root) %{_libdir}/libxmlrpc_server_abyss.so
%attr(755,root,root) %{_libdir}/libxmlrpc_server_cgi.so
%attr(755,root,root) %{_libdir}/libxmlrpc_util.so
%{_pkgconfigdir}/xmlrpc.pc
%{_pkgconfigdir}/xmlrpc_abyss.pc
%{_pkgconfigdir}/xmlrpc_client.pc
%{_pkgconfigdir}/xmlrpc_cpp.pc
%{_pkgconfigdir}/xmlrpc_packetsocket.pc
%{_pkgconfigdir}/xmlrpc_server.pc
%{_pkgconfigdir}/xmlrpc_server_abyss.pc
%{_pkgconfigdir}/xmlrpc_server_cgi.pc
%{_pkgconfigdir}/xmlrpc_util.pc
%dir %{_includedir}/xmlrpc-c
%{_includedir}/xmlrpc-c/*.h
# legacy
%{_includedir}/xmlrpc*.h
# C++
%attr(755,root,root) %{_libdir}/libxmlrpc_client++.so
%attr(755,root,root) %{_libdir}/libxmlrpc_cpp.so
%attr(755,root,root) %{_libdir}/libxmlrpc_packetsocket.so
%attr(755,root,root) %{_libdir}/libxmlrpc_server_abyss++.so
%attr(755,root,root) %{_libdir}/libxmlrpc_server_cgi++.so
%attr(755,root,root) %{_libdir}/libxmlrpc_server_pstream++.so
%attr(755,root,root) %{_libdir}/libxmlrpc_server++.so
%attr(755,root,root) %{_libdir}/libxmlrpc++.so
%{_pkgconfigdir}/xmlrpc_client++.pc
%{_pkgconfigdir}/xmlrpc++.pc
%{_pkgconfigdir}/xmlrpc_server_abyss++.pc
%{_pkgconfigdir}/xmlrpc_server_cgi++.pc
%{_pkgconfigdir}/xmlrpc_server++.pc
%{_pkgconfigdir}/xmlrpc_server_pstream++.pc
%{_includedir}/xmlrpc-c/*.hpp
# legacy
%{_includedir}/XmlRpcCpp.h
