Summary:	VAAPI (Video Acceleration API) utilities
Summary(pl.UTF-8):	VAAPI (Video Acceleration API) - programy narzędziowe
Name:		libva-utils
Version:	1.8.2
Release:	1
License:	MIT
Group:		Libraries
Source0:	https://www.freedesktop.org/software/vaapi/releases/libva/%{name}-%{version}.tar.bz2
# Source0-md5:	4a8edb92fb0b439f1146adbfa0fba76d
URL:		https://www.freedesktop.org/wiki/Software/vaapi
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libdrm-devel >= 2.4
BuildRequires:	libtool
BuildRequires:	libva-devel >= 1.7.3
BuildRequires:	libva-wayland-devel >= 1.7.3
BuildRequires:	libva-x11-devel >= 1.7.3
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(libva) >= 0.39.4
# wayland-client
BuildRequires:	wayland-devel >= 1.0.0
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXfixes-devel
Requires:	libva-drm >= 1.8.0
Requires:	libva-wayland >= 1.8.0
Requires:	libva-x11 >= 1.8.0
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
%attr(755,root,root) %{_bindir}/avcenc
%attr(755,root,root) %{_bindir}/h264encode
%attr(755,root,root) %{_bindir}/jpegenc
%attr(755,root,root) %{_bindir}/loadjpeg
%attr(755,root,root) %{_bindir}/mpeg2vaenc
%attr(755,root,root) %{_bindir}/mpeg2vldemo
%attr(755,root,root) %{_bindir}/putsurface
%attr(755,root,root) %{_bindir}/putsurface_wayland
%attr(755,root,root) %{_bindir}/vainfo
