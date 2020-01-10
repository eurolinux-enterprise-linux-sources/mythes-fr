Name: mythes-fr
Summary: French thesaurus
Version: 2.3
Release: 4%{?dist}
Source: http://www.dicollecte.org/download/fr/thesaurus-v%{version}.zip
Group: Applications/Text
URL: http://www.dicollecte.org/home.php?prj=fr
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: LGPLv2+
BuildArch: noarch
Requires: mythes

%description
French thesaurus.

%prep
%setup -q -c

%build
for i in README_thes_fr.txt; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-1 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p thes_fr.dat $RPM_BUILD_ROOT/%{_datadir}/mythes/th_fr_FR_v2.dat
cp -p thes_fr.idx $RPM_BUILD_ROOT/%{_datadir}/mythes/th_fr_FR_v2.idx

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README_thes_fr.txt
%{_datadir}/mythes/*

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 2.3-4
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar 09 2012 Caolán McNamara <caolanm@redhat.com> - 2.3-1
- latest version

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Aug 17 2010 Caolán McNamara <caolanm@redhat.com> - 2.2.2-1
- latest version

* Sun Apr 04 2010 Caolán McNamara <caolanm@redhat.com> - 2.2-2
- mythes now owns /usr/share/mythes

* Thu Oct 22 2009 Caolán McNamara <caolanm@redhat.com> - 2.2-1
- latest version

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 13 2009 Caolán McNamara <caolanm@redhat.com> - 2.1-4
- tidy spec

* Sat May 23 2009 Caolán McNamara <caolanm@redhat.com> - 2.1-3
- update to new location

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 15 2009 Caolán McNamara <caolanm@redhat.com> - 2.1-1
- initial version
