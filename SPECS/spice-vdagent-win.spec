%global spice_data_dir  %{_datadir}/spice


Name: spice-vdagent-win
Version: 0.10.0
Release: 7%{?dist}
License: GPLv2+
Summary: Spice agent MSI installers for Windows guests
Group: Virtualization/Management
URL: http://www.spice-space.org

Source0: spice-vdagent-x86-0.10.0-7.msi
Source1: spice_vdagent_x64.zip
Source2: spice-vdagent-win-0.10.0-7-sources.zip
Source3: spice-vdagent-win-0.10.0-7-spec.zip
Source4: spice-vdagent-x64-0.10.0-7.msi
Source5: spice_vdagent_x86.zip

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch

%description
Spice agent MSI installers for Windows guests

%package x86
Summary: Spice agent MSI installers for Windows guests (32 bit)
Group: Virtualization/Management

%description x86
Spice agent MSI installers for Windows guests (32 bit)

%package x64
Summary: Spice agent MSI installers for Windows guests (64 bit)
Group: Virtualization/Management

%description x64
Spice agent MSI installers for Windows guests (64 bit)

%prep

%build

%install
rm -rf %{buildroot}
/usr/bin/install -d %{buildroot}%{spice_data_dir}


/bin/cp %{SOURCE0} %{buildroot}%{spice_data_dir}/
/bin/cp %{SOURCE4} %{buildroot}%{spice_data_dir}/

%clean
rm -rf %{buildroot}

%files x64
%defattr(0644,root,root,0755)
%{spice_data_dir}/spice-vdagent-x64*.msi


%files x86
%defattr(0644,root,root,0755)
%{spice_data_dir}/spice-vdagent-x86*.msi

%changelog
* Sun Feb 19 2023 Uri Lublin <uril@redhat.com> - 0.10.0-7
- Rebuilt
  Resolves: rhbz#2125276

* Tue Sep  6 2022 Uri Lublin <uril@redhat.com> - 0.10.0-6
- Rebuilt to pick mingw-zlib 1.2.8-10
  Resolves rhbz#2121122

* Thu Jun 25 2020 Uri Lublin <uril@redhat.com> - 0.10.0-5
- Rebuilt

* Wed Jun  3 2020 Uri Lublin <uril@redhat.com> - 0.10.0-4
- Reset properly state of pending large messages upon disconnection
  Resolves rhbz#1548419
- Return detailed message for file transfer
  Resolves rhbz#1520393

* Mon Dec  9 2019 Uri Lublin <uril@redhat.com> - 0.10.0-2
- First build for 8.2
- Resolves: rhbz#1641755

