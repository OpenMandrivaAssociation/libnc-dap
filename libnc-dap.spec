%define lib_major       3
%define lib_name        %mklibname nc-dap %{lib_major}
%define lib_name_d      %mklibname nc-dap %{lib_major} -d
%define lib_name_d_s    %mklibname nc-dap %{lib_major} -d -s

Name:           libnc-dap
Version:        3.7.4
Release:        3
Epoch:          0
Summary:        NetCDF interface to DAP-2 from OPeNDAP
URL:            https://www.opendap.org/
Source0:        http://www.opendap.org/pub/source/libnc-dap-%{version}.tar.gz
Source1:        http://www.opendap.org/pub/source/libnc-dap-%{version}.tar.gz.sig
Patch1:		libnc-dap-3.7.4-fix-str-fmt.patch
# dncdump and netcdf headers are coverd by a BSD-like license
License:        LGPLv2+
Group:          System/Libraries
BuildRequires:  gcc-gfortran
BuildRequires:  libdap-devel >= 0:3.7.3
BuildRequires:  libdap-static-devel >= 0:3.7.3

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
Provides:       nc-dap-devel = %{epoch}:%{version}-%{release}
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
Provides:       nc-dap-static-devel = %{epoch}:%{version}-%{release}
Requires:       %{lib_name_d} = %{epoch}:%{version}-%{release}
Requires:       libdap-static-devel >= 0:3.7.0

%description -n %{lib_name_d_s}
This package contains all the files needed to develop applications that
will use libnc-dap.

%prep
%setup -q
%patch1 -p0

%build
%{configure2_5x} --disable-dependency-tracking
%{make}

%install
%{makeinstall_std} INSTALL="%{__install} -p"

%{__mv} %{buildroot}%{_bindir}/ncdump %{buildroot}%{_bindir}/dncdump

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
%{_libdir}/pkgconfig/libnc-dap.pc
%{_bindir}/ncdap-config
%{_bindir}/ncdap-config-pkgconfig
%{_includedir}/libnc-dap/
%{_datadir}/aclocal/*

%files -n %{lib_name_d_s}
%defattr(-,root,root,-)
%{_libdir}/libnc-dap.a


%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0:3.7.4-2mdv2011.0
+ Revision: 609762
- rebuild

* Mon Nov 23 2009 Funda Wang <fwang@mandriva.org> 0:3.7.4-1mdv2010.1
+ Revision: 469308
- new version 3.7.4

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sun Oct 19 2008 David Walluck <walluck@mandriva.org> 0:3.7.3-1mdv2009.1
+ Revision: 295323
- update file list
- add template patch
- 3.7.3
- fix provides

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Oct 01 2007 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 0:3.7.0-3mdv2008.0
+ Revision: 94080
- Rebuild because of missing packages on repositories (reported by David
  Walluck).

* Sun Sep 09 2007 David Walluck <walluck@mandriva.org> 0:3.7.0-2mdv2008.0
+ Revision: 83430
- fix provides
- Import libnc-dap



* Wed Jun 06 2007 David Walluck <walluck@mandriva.org> 0:3.7.0-1mdv2008.0
- release
