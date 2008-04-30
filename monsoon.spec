%define name monotorrent-interface
%define version 0.1
%define release %mkrel 2

Summary: Graphical Bittorrent client for Mono
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.monotorrent.com/Files/%version/%{name}-%{version}.tar.gz
Source1: MonoTorrent.Interface.exe.config
License: MIT
Group: System/Libraries
Url: http://www.monotorrent.com/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
BuildRequires: mono-devel
BuildRequires: monotorrent >= 0.20
BuildRequires: ndesk-dbus-glib
BuildRequires: gnome-sharp2
%define _requires_exceptions ^lib

%description
Monotorrent is an open source bittorrent library. This is a Gtk GUI based on
monotorrent.

%prep
%setup -q
ln -sf %_prefix/lib/mono/gac/NDesk.Dbus*/*/* MonoTorrent.Interface/libs/
ln -sf %_prefix/lib/bitsharp/MonoTorrent.dll MonoTorrent.Interface/libs/

%build
./configure --prefix=%_prefix
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall libdir=%buildroot%_prefix/lib
rm -f %buildroot%_prefix/lib/monotorrent-interface/NDesk.DBus*

ln -sf %_prefix/lib/bitsharp/MonoTorrent.dll %buildroot%_prefix/lib/monotorrent-interface/
cp %SOURCE1 %buildroot%_prefix/lib/monotorrent-interface/

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Monotorrent
Comment=Bittorrent client for Mono
Exec=monotorrent.interface
Icon=file_transfer_section
Terminal=false
Type=Application
StartupNotify=true
Categories=Network;FileTransfer;P2P;GTK;
MimeType=application/x-bittorrent;
EOF


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
%_bindir/monotorrent.interface
%_datadir/applications/mandriva-%name.desktop
%dir %_prefix/lib/monotorrent-interface
%_prefix/lib/monotorrent-interface/icons
%_prefix/lib/monotorrent-interface/MonoTorrent.dll
%_prefix/lib/monotorrent-interface/MonoTorrent.Interface.exe
%_prefix/lib/monotorrent-interface/MonoTorrent.Interface.exe.config
#gw TODO: replace these two by packaged versions
%_prefix/lib/monotorrent-interface/Mono.Nat.dll
%_prefix/lib/monotorrent-interface/NLog.dll
