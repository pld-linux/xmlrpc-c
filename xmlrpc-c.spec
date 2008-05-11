Summary:	XML-RPC C library - an implementation of the xmlrpc protocol
Summary(pl.UTF-8):	Biblioteka XML-RPC C - implementacja protokołu xmlrpc
Name:		xmlrpc-c
Version:	1.14.2
Release:	0.1
License:	XML-RPC C Library License
Group:		Libraries
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	cbd9675dc48819d5f745b775fca7d425
Patch0:		%{name}-fastdep.patch
Patch1:		%{name}-soname.patch
Patch2:		%{name}-cflags.patch
Patch3:		%{name}-syntax-fix.patch
Patch4:		%{name}-fixed-broken-format-string-modifiers-for-size_t-type.patch  
Patch5:         %{name}-use-proper-datatypes.patch
URL:		http://xmlrpc-c.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	w3c-libwww-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_includedir	%{_prefix}/include/%{name}

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
Requires:	libxml2-devel
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
#%patch1 -p1
%patch2 -p1
#%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
rm -f missing
%{__libtoolize}
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
	--enable-unicode \
	--enable-abyss-threads

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README doc/{COPYING,CREDITS,HISTORY,SECURITY,TESTING,TODO}
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%ghost %attr(755,root,root) %{_libdir}/lib*.so.[0-9]

%files devel
%defattr(644,root,root,755)
%doc doc/DEVELOPING
%attr(755,root,root) %{_libdir}/lib*.so
#%{_libdir}/lib*.la
%{_includedir}

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
