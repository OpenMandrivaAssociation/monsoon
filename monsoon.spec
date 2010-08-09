%define name monsoon
%define version 0.21
%define svn r148377
%define release %mkrel 2.%svn.1

Summary: Graphical Bittorrent client for Mono
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.monsoon-project.org/jaws/data/files/%version/%{name}-%svn.tar.xz
Patch: monsoon-0.11.3-desktopentry.patch
#gw fix for an API change in monotorrent:
#http://anonsvn.mono-project.com/viewvc/trunk/bitsharp/src/MonoTorrent/MonoTorrent.Client/ClientEngine.cs?r1=131076&r2=137752
Patch1: monsoon-r148377-dont-wait-on-stopall.patch
License: MIT/X11
Group: Networking/File transfer
Url: http://www.monsoon-project.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
BuildRequires: mono-addins-devel
BuildRequires: mono-devel
BuildRequires: mono-nat
BuildRequires: monotorrent >= 0.80
BuildRequires: ndesk-dbus-glib-devel
#BuildRequires: nlog
BuildRequires: gnome-sharp2-devel
BuildRequires: intltool
BuildRequires: libtool
Provides: monotorrent-interface
Obsoletes: monotorrent-interface
%define _requires_exceptions lib64\\|libgtk\\|libx

%description
A fully featured bittorrent GUI supporting many advanced features such
as selective downloading, automatic port forwarding via uPnP and RSS
integration.


%prep
%setup -q -n %name
%patch -p1
%patch1
./autogen.sh

%build
./configure --prefix=%_prefix
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall libdir=%buildroot%_prefix/lib
ln -sf %_prefix/lib/monotorrent/MonoTorrent.dll %_prefix/lib/mono-nat/Mono.Nat.dll %buildroot%_prefix/lib/%name
rm -f %buildroot%_prefix/lib/%name/NLog.dll

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
