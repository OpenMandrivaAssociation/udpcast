%define	_prel	20071228

Summary:	UDP broadcast installation
Name:		udpcast
Version:	0.0
Release:	%mkrel 0.%{_prel}.1
License:	GPLv2 and BSD-like
Group:		Networking/Other
Url:		http://udpcast.linux.lu/
Source0:	http://udpcast.linux.lu/download/%{name}-%{_prel}.tar.gz
#BuildRequires:
Buildroot:      %{_tmppath}/%{name}-%{version}

%description
UDPcast is a file transfer tool that can send data simultaneously to many 
destinations on a LAN. This can for instance be used to install entire 
classrooms of PC's at once. The advantage of UDPcast over using other methods 
(nfs, ftp, whatever) is that UDPcast uses Ethernet's multicast abilities: 
it won't take longer to install 15 machines than it would to install just 2

%prep
%setup -qn %{name}-%{_prel}

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%defattr(-,root,root)
%doc cmd.html COPYING *.txt
%{_sbindir}/udp-receiver
%{_sbindir}/udp-sender
%{_mandir}/man1/udp-receiver.1*
%{_mandir}/man1/udp-sender.1*
