%define major 2
%define libname %mklibname ccfits %{major}
%define develname %mklibname ccfits -d

Name:		ccfits
Version:	2.4
Release:	1
Summary:	A C++ interface for cfitsio

Group:		System/Libraries
License:	BSD
URL:		http://heasarc.gsfc.nasa.gov/docs/software/fitsio/ccfits
Source0:	http://heasarc.gsfc.nasa.gov/docs/software/fitsio/ccfits/CCfits-%{version}.tar.gz
BuildRequires:	cfitsio-devel = 3.290
Patch0:		CCfits-1.6-removerpath.patch

%description
CCfits is an object oriented interface to the cfitsio library. It is designed 
to make the capabilities of cfitsio available to programmers working in C++. 
It is written in ANSI C++ and implemented using the C++ Standard Library 
with namespaces, exception handling, and member template functions.

%package -n	%libname
Summary:	A C++ interface for cfitsio
Group:		System/Libraries
Provides:	ccfits = %{version}-%{release}

%package -n	%develname
Summary:	Headers for developing programs that will use %{name}
Group:		Development/C
Requires:	cfitsio-devel >= 3.280
Requires:	ccfits-doc = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
%description -n %develname
These are the header files and libraries needed to develop a %{name} 
application.

%package	doc
Summary:	Documentation for %{name}, includes full API docs
Group:		Development/C
BuildArch:	noarch
Provides:	ccfits-doc = %{version}-%{release}
 
%description doc
This package contains the full API documentation for %{name}.

%prep
%setup -q -n CCfits
%patch0 -p1
rm -rf %{_builddir}/%{name}/html/*.pl

%build
./configure --prefix=%{_prefix} --exec-prefix=%{_prefix} --bindir=%{_bindir} --sbindir=%{_sbindir} --sysconfdir=%{_sysconfdir} --datadir=%{_datadir} --includedir=%{_includedir} --libdir=%{_libdir} --libexecdir=%{_libexecdir} --localstatedir=%{_localstatedir} --mandir=%{_mandir} --with-cfitsio-include=%{_includedir}/cfitsio/ --with-cfitsio=%{_libdir}

%make

%install
%makeinstall_std
rm -rf %{buildroot}%{_bindir}/cookbook

%files -n %libname
%doc License.txt
%{_libdir}/*so.*

%files -n %develname
%doc CHANGES 
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*

%files doc
%doc License.txt html
