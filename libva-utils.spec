%define	libva_ver	2.1.0
Summary:	VAAPI (Video Acceleration API) utilities
Summary(pl.UTF-8):	VAAPI (Video Acceleration API) - programy narzędziowe
Name:		libva-utils
Version:	2.17.1
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/intel/libva-utils/releases
Source0:	https://github.com/intel/libva-utils/releases/download/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	5cac474af03966135c0a62849832e2ad
URL:		https://01.org/linuxmedia/vaapi
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool >= 2:2
BuildRequires:	libva-devel >= %{libva_ver}
BuildRequires:	libva-drm-devel >= %{libva_ver}
BuildRequires:	libva-wayland-devel >= %{libva_ver}
BuildRequires:	libva-x11-devel >= %{libva_ver}
BuildRequires:	pkgconfig
# VA-API version
BuildRequires:	pkgconfig(libva) >= 1.1.0
# wayland-client
BuildRequires:	wayland-devel >= 1.0.0
BuildRequires:	xorg-lib-libX11-devel
Requires:	libva-drm >= %{libva_ver}
Requires:	libva-wayland >= %{libva_ver}
Requires:	libva-x11 >= %{libva_ver}
Provides:	libva-tools = %{version}
Obsoletes:	libva-tools < 1.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utilities and tests for libva API.

%description -l pl.UTF-8
Programy narzędziowe i testowe dla API libva.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING NEWS
%attr(755,root,root) %{_bindir}/av1encode
%attr(755,root,root) %{_bindir}/avcenc
%attr(755,root,root) %{_bindir}/avcstreamoutdemo
%attr(755,root,root) %{_bindir}/h264encode
%attr(755,root,root) %{_bindir}/hevcencode
%attr(755,root,root) %{_bindir}/jpegenc
%attr(755,root,root) %{_bindir}/loadjpeg
%attr(755,root,root) %{_bindir}/mpeg2vaenc
%attr(755,root,root) %{_bindir}/mpeg2vldemo
%attr(755,root,root) %{_bindir}/putsurface
%attr(755,root,root) %{_bindir}/putsurface_wayland
%attr(755,root,root) %{_bindir}/sfcsample
%attr(755,root,root) %{_bindir}/vainfo
%attr(755,root,root) %{_bindir}/vacopy
%attr(755,root,root) %{_bindir}/vavpp
%attr(755,root,root) %{_bindir}/vp8enc
%attr(755,root,root) %{_bindir}/vp9enc
%attr(755,root,root) %{_bindir}/vpp3dlut
%attr(755,root,root) %{_bindir}/vppblending
%attr(755,root,root) %{_bindir}/vppchromasitting
%attr(755,root,root) %{_bindir}/vppdenoise
%attr(755,root,root) %{_bindir}/vpphdr_tm
%attr(755,root,root) %{_bindir}/vppscaling_csc
%attr(755,root,root) %{_bindir}/vppscaling_n_out_usrptr
%attr(755,root,root) %{_bindir}/vppsharpness
