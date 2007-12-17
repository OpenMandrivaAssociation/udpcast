%define	_prel	20070218

Summary:	UDP broadcast installation
Name:		udpcast
Version:	0.0
Release:	%mkrel 0.%{_prel}.1
License:	GPL BSD
Group:		Networking/Other
Url:		http://udpcast.linux.lu/
Source0:	http://udpcast.linux.lu/download/%{name}-%{_prel}.tar.bz2
#BuildRequires:

%description
UDPcast is a file transfer tool that can send data simultaneously to many 
destinations on a LAN. This can for instance be used to install entire 
classrooms of PC's at once. The advantage of UDPcast over using other methods 
(nfs, ftp, whatever) is that UDPcast uses Ethernet's multicast abilities: 
it won't take longer to install 15 machines than it would to install just 2

%prep
%setup -qn %{name}-%{_prel}

%build
perl -pi -e "s/CFLAGS=.*/CFLAGS=%{optflags}/" Makefile
%configure2_5x \
    --prefix=%{buildroot}%{_prefix} \
    --mandir=%{buildroot}%{_mandir}

make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc Changelog.txt cmd.html COPYING *.txt
%attr(755,root,root) %{_sbindir}/udp*
%{_mandir}/man1/udp-receiver.1*
%{_mandir}/man1/udp-sender.1*


