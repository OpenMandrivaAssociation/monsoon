%define name monsoon
%define version 0.20
%define release %mkrel 1

Summary: Graphical Bittorrent client for Mono
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.monsoon-project.org/jaws/data/files/%version/%{name}-%{version}.tar.gz
Patch: monsoon-0.11.3-desktopentry.patch
License: MIT/X11
Group: Networking/File transfer
Url: http://monotorrent.blogspot.com/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
BuildRequires: mono-devel
BuildRequires: mono-nat
BuildRequires: monotorrent >= 0.70
BuildRequires: ndesk-dbus-glib
BuildRequires: gnome-sharp2-devel
BuildRequires: intltool
Provides: monotorrent-interface
Obsoletes: monotorrent-interface
%define _requires_exceptions lib64\\|libgtk\\|libx

%description
A fully featured bittorrent GUI supporting many advanced features such
as selective downloading, automatic port forwarding via uPnP and RSS
integration.


%prep
%setup -q
%patch -p1

%build
./configure --prefix=%_prefix
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall libdir=%buildroot%_prefix/lib
ln -sf %_prefix/lib/monotorrent/MonoTorrent.dll %_prefix/lib/mono-nat/Mono.Nat.dll %buildroot%_prefix/lib/%name

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%post 
%update_desktop_database

%postun
%clean_desktop_database

%files -f %name.lang
%defattr(-,root,root)
%doc README
%_bindir/%name
%_datadir/applications/%name.desktop
%dir %_prefix/lib/%name
%_prefix/lib/%name/icons
%_prefix/lib/%name/Monsoon.exe
%_prefix/lib/%name/Monsoon.exe.config
%_prefix/lib/%name/MonoTorrent.dll
%_prefix/lib/%name/Mono.Nat.dll
#gw TODO: replace this by a packaged version
%_prefix/lib/%name/NLog.dll
