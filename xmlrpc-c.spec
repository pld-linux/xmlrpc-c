Summary:	XML-RPC C library - an implementation of the xmlrpc protocol
Summary(pl.UTF-8):	Biblioteka XML-RPC C - implementacja protokołu xmlrpc
Name:		xmlrpc-c
Version:	1.14.2
Release:	2
License:	XML-RPC for C License (BSD-like)
Group:		Libraries
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	cbd9675dc48819d5f745b775fca7d425
Patch0:		%{name}-fastdep.patch
Patch1:		%{name}-soname.patch
Patch2:		%{name}-cflags.patch
Patch3:		%{name}-fixed-broken-format-string-modifiers-for-size_t-type.patch  
Patch4:         %{name}-use-proper-datatypes.patch
URL:		http://xmlrpc-c.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	w3c-libwww-devel >= 5.4.0-11
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML-RPC C library - an implementation of the xmlrpc protocol.

%description -l pl.UTF-8
Biblioteka XML-RPC C - implementacja protokołu xmlrpc.

%package devel
Summary:	Header files etc to develop XML-RPC applications
Summary(pl.UTF-8):	Pliki nagłówkowe do tworzenia aplikacji XML-RPC
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	curl-devel
Requires:	expat-devel
Requires:	libstdc++-devel
Requires:	libxml2-devel >= 2.0
Requires:	w3c-libwww-devel

%description devel
Header files etc needed to develop XML-RPC applications.

%description devel -l pl.UTF-8
Pliki nagłówkowe potrzebne do tworzenia aplikacji używających XML-RPC.

%package static
Summary:	Static XML-RPC C libraries
Summary(pl.UTF-8):	Biblioteki statyczne XML-RPC C
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static XML-RPC C libraries.

%description static -l pl.UTF-8
Biblioteki statyczne XML-RPC C.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%{__libtoolize}
# hack: libtoolize removes config.* here
cp -f /usr/share/automake/{missing,config.*} .
%{__aclocal}
%{__autoconf}
OPTCFLAGS="%{rpmcflags}" ; export OPTCFLAGS
OPTCXXFLAGS="%{rpmcxxflags}" ; export OPTCXXFLAGS
%configure \
	--enable-abyss-server \
	--enable-cgi-server \
	--enable-cplusplus \
	--enable-libxml2-backend \
	--enable-curl-client \
	--enable-libwww-client \
	--with-libwww-ssl \
	--enable-abyss-threads

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT \
	LIBINST_DIR=%{_libdir}

rm $RPM_BUILD_ROOT%{_includedir}/xmlrpc_server_w32httpsys.h \
	$RPM_BUILD_ROOT%{_includedir}/xmlrpc-c/server_w32httpsys.h

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README doc/{COPYING,CREDITS,HISTORY,SECURITY,TODO}
# C
%attr(755,root,root) %{_libdir}/libxmlrpc-c.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libxmlrpc-c.so.3
%attr(755,root,root) %{_libdir}/libxmlrpc_abyss.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libxmlrpc_abyss.so.3
%attr(755,root,root) %{_libdir}/libxmlrpc_client.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libxmlrpc_client.so.3
%attr(755,root,root) %{_libdir}/libxmlrpc_server.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libxmlrpc_server.so.3
%attr(755,root,root) %{_libdir}/libxmlrpc_server_abyss.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libxmlrpc_server_abyss.so.3
%attr(755,root,root) %{_libdir}/libxmlrpc_server_cgi.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libxmlrpc_server_cgi.so.3
%attr(755,root,root) %{_libdir}/libxmlrpc_util.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libxmlrpc_util.so.3
# C++
%attr(755,root,root) %{_libdir}/libxmlrpc++.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libxmlrpc++.so.4
%attr(755,root,root) %{_libdir}/libxmlrpc_client++.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libxmlrpc_client++.so.4
%attr(755,root,root) %{_libdir}/libxmlrpc_cpp.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libxmlrpc_cpp.so.4
%attr(755,root,root) %{_libdir}/libxmlrpc_packetsocket.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libxmlrpc_packetsocket.so.4
%attr(755,root,root) %{_libdir}/libxmlrpc_server++.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libxmlrpc_server++.so.4
%attr(755,root,root) %{_libdir}/libxmlrpc_server_abyss++.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libxmlrpc_server_abyss++.so.4
%attr(755,root,root) %{_libdir}/libxmlrpc_server_pstream++.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libxmlrpc_server_pstream++.so.4

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
%dir %{_includedir}/xmlrpc-c
%{_includedir}/xmlrpc-c/*.h
# legacy
%{_includedir}/xmlrpc*.h
# C++
%attr(755,root,root) %{_libdir}/libxmlrpc++.so
%attr(755,root,root) %{_libdir}/libxmlrpc_client++.so
%attr(755,root,root) %{_libdir}/libxmlrpc_cpp.so
%attr(755,root,root) %{_libdir}/libxmlrpc_packetsocket.so
%attr(755,root,root) %{_libdir}/libxmlrpc_server++.so
%attr(755,root,root) %{_libdir}/libxmlrpc_server_abyss++.so
%attr(755,root,root) %{_libdir}/libxmlrpc_server_pstream++.so
%{_includedir}/xmlrpc-c/*.hpp
# legacy
%{_includedir}/XmlRpcCpp.h

%files static
%defattr(644,root,root,755)
# C
%{_libdir}/libxmlrpc-c.a
%{_libdir}/libxmlrpc_abyss.a
%{_libdir}/libxmlrpc_client.a
%{_libdir}/libxmlrpc_server.a
%{_libdir}/libxmlrpc_server_abyss.a
%{_libdir}/libxmlrpc_server_cgi.a
%{_libdir}/libxmlrpc_util.a
# C++
%{_libdir}/libxmlrpc++.a
%{_libdir}/libxmlrpc_client++.a
%{_libdir}/libxmlrpc_cpp.a
%{_libdir}/libxmlrpc_packetsocket.a
%{_libdir}/libxmlrpc_server++.a
%{_libdir}/libxmlrpc_server_abyss++.a
%{_libdir}/libxmlrpc_server_pstream++.a
