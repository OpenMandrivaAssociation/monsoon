%define name monsoon
%define version 0.15
%define release %mkrel 2

Summary: Graphical Bittorrent client for Mono
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.monotorrent.com/Files/%version/%{name}-%{version}.tar.gz
Patch: monsoon-0.11.3-desktopentry.patch
License: MIT/X11
Group: Networking/File transfer
Url: http://monotorrent.blogspot.com/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
BuildRequires: mono-devel
#BuildRequires: monotorrent >= 0.40
BuildRequires: ndesk-dbus-glib
BuildRequires: gnome-sharp2-devel
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
#ln -sf %_prefix/lib/monotorrent/MonoTorrent.dll Monsoon/libs/

%build
./configure --prefix=%_prefix
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall libdir=%buildroot%_prefix/lib
#ln -sf %_prefix/lib/monotorrent/MonoTorrent.dll %buildroot%_prefix/lib/%name

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
#gw TODO: replace these two by packaged versions
%_prefix/lib/%name/Mono.Nat.dll
%_prefix/lib/%name/NLog.dll
