Name:		ananicy
Version:	2.2.1
Release:	3
Summary:	ANother Auto NICe daemon
License:	GPLv3+
URL:		https://github.com/Nefelim4ag/Ananicy
Source0:	https://github.com/Nefelim4ag/Ananicy/archive/refs/tags/%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	systemd-rpm-macros
Requires:	schedtool

%description
ANother Auto NICe daemon.

%prep
%autosetup -n Ananicy-%{version} -p1
sed -i 's|#!/usr/bin/env python3|#!%{__python}|' ananicy.py

%build

%install
%make_install PREFIX="%{buildroot}" A_SERVICE=%{buildroot}%{_unitdir}/ananicy.service

install -d %{buildroot}%{_presetdir}
cat > %{buildroot}%{_presetdir}/86-ananicy.preset << EOF
enable ananicy.service
EOF

%post
%systemd_post ananicy.service

%preun
%systemd_preun ananicy.service

%postun
%systemd_postun_with_restart ananicy.service

%files
%dir %{_sysconfdir}/ananicy.d
%config(noreplace) %{_sysconfdir}/ananicy.d/ananicy.conf
%config %{_sysconfdir}/ananicy.d/00-*
%{_bindir}/%{name}
%{_unitdir}/ananicy.service
%{_presetdir}/86-ananicy.preset
