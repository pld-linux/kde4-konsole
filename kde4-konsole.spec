# TODO:
# - new descriptions
#
%define		_state		stable
%define		orgname		konsole
%define		qtver		4.8.3
%define		kdeworkspacever	4.11.0

Summary:	K Desktop Environment - KDE Terminal Emulator
Summary(pl.UTF-8):	K Desktop Environment - Emulator terminala dla KDE
Name:		kde4-konsole
Version:	4.14.3
Release:	4
License:	GPL
Group:		X11/Applications
Source0:	http://download.kde.org/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	1c81a9a2c073f7992671e168b7285a2a
Patch0:		konsole-wordchars.patch
Patch1:		konsole-git.patch
URL:		http://www.kde.org/
BuildRequires:	kde4-kdebase-devel >= %{version}
BuildRequires:	kde4-kdebase-workspace-devel >= %{kdeworkspacever}
BuildRequires:	kde4-kdelibs-devel >= %{version}
Requires:	fontpostinst
Provides:	kde4-kdebase-common-konsole
Provides:	kde4-kdebase-konsole
Obsoletes:	kde4-kdebase-common-konsole
Obsoletes:	kde4-kdebase-konsole
Obsoletes:	kde4-konsole <= 4.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE Terminal Emulator.

%description -l pl.UTF-8
Emulator terminala dla KDE.

%prep
%setup -q -n %{orgname}-%{version}
%patch0 -p1
%patch1 -p1

%build
install -d build
cd build
%cmake \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_bindir}/fontpostinst misc

%postun
%{_bindir}/fontpostinst misc

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/konsole
%attr(755,root,root) %{_bindir}/konsoleprofile
%attr(755,root,root) %{_libdir}/libkdeinit4_konsole.so
%attr(755,root,root) %{_libdir}/kde4/libkonsolepart.so
%attr(755,root,root) %{_libdir}/libkonsoleprivate.so
%{_datadir}/kde4/services/ServiceMenus/konsolehere.desktop
%{_datadir}/kde4/services/ServiceMenus/konsolerun.desktop
%{_datadir}/kde4/services/konsolepart.desktop
%{_datadir}/kde4/servicetypes/terminalemulator.desktop
%{_datadir}/apps/konsole
%{_datadir}/apps/kconf_update/konsole.upd
%attr(755,root,root) %{_datadir}/apps/kconf_update/konsole*.sh
%{_datadir}/apps/kconf_update/konsole_remove_background_mode.upd
%{_desktopdir}/kde4/konsole.desktop
%{_kdedocdir}/en/konsole
