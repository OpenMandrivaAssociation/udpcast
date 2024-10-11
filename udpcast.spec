%define debug_package %{nil}

Summary:	UDP broadcast installation
Name:		udpcast
Version:	20230924
Release:	1
License:	GPLv2+ and BSD-like
Group:		Networking/Other
Url:		https://udpcast.linux.lu/
Source0:	https://udpcast.linux.lu/download/%{name}-%{version}.tar.gz
Patch0:		udpcast-20120424-gcc4.9.patch

%description
UDPcast is a file transfer tool that can send data simultaneously to many
destinations on a LAN. This can for instance be used to install entire
classrooms of PC's at once. The advantage of UDPcast over using other methods
(nfs, ftp, whatever) is that UDPcast uses Ethernet's multicast abilities:
it won't take longer to install 15 machines than it would to install just 2

%files
%doc cmd.html COPYING *.txt
%{_sbindir}/udp-receiver
%{_sbindir}/udp-sender
%{_mandir}/man1/udp-receiver.1*
%{_mandir}/man1/udp-sender.1*

#----------------------------------------------------------------------------

%package devel
Summary:	Header files for UDPcast
Requires:	%{name} = %{EVRD}

%description devel
Header files for UDPcast

%files devel
%{_includedir}/udpcast/rateGovernor.h

#----------------------------------------------------------------------------

%prep
%setup -q
%patch 0 -p1

%build
%configure
%make_build

%install
%make_install

