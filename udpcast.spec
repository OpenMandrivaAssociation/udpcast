%define	_prel	20090830

Summary:	UDP broadcast installation
Name:		udpcast
Version:	0.0
Release:	%mkrel -c %{_prel} 2
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
%{_includedir}/udpcast/rateGovernor.h
%{_mandir}/man1/udp-receiver.1*
%{_mandir}/man1/udp-sender.1*


%changelog
* Sat Apr 16 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0-0.20090830.2mdv2011.0
+ Revision: 653315
- rebuild

* Thu Sep 10 2009 Frederik Himpe <fhimpe@mandriva.org> 0.0-0.20090830.1mdv2010.0
+ Revision: 437534
- Update to new version 20090830

* Tue Nov 25 2008 Frederik Himpe <fhimpe@mandriva.org> 0.0-0.20081116.1mdv2009.1
+ Revision: 306744
- Update to new version 20081116

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.0-0.20071228.3mdv2009.0
+ Revision: 269445
- rebuild early 2009.0 package (before pixel changes)

* Tue Apr 22 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0-0.20071228.2mdv2009.0
+ Revision: 196394
+ rebuild (emptylog)

* Tue Apr 22 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0-0.20071228.1mdv2009.0
+ Revision: 196393
- fix permissions for executables (bug #40247)

* Tue Feb 05 2008 Frederik Himpe <fhimpe@mandriva.org> 0.0-0.20071228.1mdv2008.1
+ Revision: 162869
- New upstream version

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.0-0.20070218.1mdv2008.1
+ Revision: 140924
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Feb 21 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0-0.20070218.1mdv2007.0
+ Revision: 123436
- new version

* Wed Feb 07 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0-0.20070205.1mdv2007.1
+ Revision: 117334
- Import udpcast

