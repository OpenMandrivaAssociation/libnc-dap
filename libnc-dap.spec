%define lib_major       3
%define lib_name        %mklibname nc-dap %{lib_major}
%define lib_name_d      %mklibname nc-dap %{lib_major} -d
%define lib_name_d_s    %mklibname nc-dap %{lib_major} -d -s

Name:           libnc-dap
Summary:        NetCDF interface to DAP-2 from OPeNDAP
Version:        3.7.0
Release:        %mkrel 1
Epoch:          0
URL:            http://www.opendap.org/
Source0:        ftp://ftp.unidata.ucar.edu/pub/opendap/source/libnc-dap-%{version}.tar.gz 
# dncdump and netcdf headers are coverd by a BSD-like license
License:        LGPL
Group:          System/Libraries
BuildRequires:  gcc-gfortran
BuildRequires:  libdap-devel >= 0:3.7.3
BuildRequires:  libdap-static-devel >= 0:3.7.3
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
The libnc-dap library is a call-for-call replacement for netcdf. It can 
read and write to and from netcdf files on the local machine and it can 
read from DAP2 compatible data servers running on local or remote 
machines. Data served using DAP2 need not be stored in netcdf files 
to be read using this replacement library.
Also included in this package is the ncdump utility, also bundled with the
original netcdf library, renamed dncdump, relinked with the library and 
thus able to read from DAP2 compatible servers.

%package -n %{lib_name}
Summary:        NetCDF interface to DAP-2 from OPeNDAP
Group:          System/Libraries

%description -n %{lib_name}
NetCDF interface to DAP-2 from OPeNDAP.

%package -n %{lib_name_d}
Summary:        Development files and header files from libnc-dap
Group:          Development/C
Provides:       %{name}-devel = %{epoch}:%{version}-%{release}
Provides:       %{_lib}%{name}-devel = %{epoch}:%{version}-%{release}
Provides:       lib%{name}-devel = %{epoch}:%{version}-%{release}
Requires:       %{lib_name} = %{epoch}:%{version}-%{release}
Requires:       libdap-devel >= 0:3.7.0
# for /usr/share/aclocal owning
Requires:       automake

%description -n %{lib_name_d}
This package contains all the files needed to develop applications that
will use libnc-dap.

%package -n %{lib_name_d_s}
Summary:        Static development files from libnc-dap
Group:          Development/C
Provides:       %{name}-static-devel = %{epoch}:%{version}-%{release}
Provides:       %{_lib}%{name}-static-devel = %{epoch}:%{version}-%{release}
Provides:       lib%{name}-static-devel = %{epoch}:%{version}-%{release}
Requires:       %{lib_name_d} = %{epoch}:%{version}-%{release}
Requires:       libdap-static-devel >= 0:3.7.0

%description -n %{lib_name_d_s}
This package contains all the files needed to develop applications that
will use libnc-dap.

%prep
%setup -q
%{__rm} -rf netcdf/.svn

%build
%{configure2_5x} --disable-dependency-tracking
%{make}

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std} INSTALL="%{__install} -p"

%{__mv} %{buildroot}%{_bindir}/ncdump %{buildroot}%{_bindir}/dncdump

%clean
%{__rm} -rf %{buildroot}

%post -n %{lib_name} -p /sbin/ldconfig

%postun -n %{lib_name} -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_bindir}/dncdump

%files -n %{lib_name}
%defattr(-,root,root,-)
%doc README README.translation NEWS COPYRIGHT COPYING netcdf
%{_libdir}/libnc-dap.so.*

%files -n %{lib_name_d}
%defattr(-,root,root,-)
%{_libdir}/libnc-dap.so
%{_libdir}/libnc-dap.la
%{_bindir}/ncdap-config
%{_includedir}/libnc-dap/
%{_datadir}/aclocal/*

%files -n %{lib_name_d_s}
%defattr(-,root,root,-)
%{_libdir}/libnc-dap.a
