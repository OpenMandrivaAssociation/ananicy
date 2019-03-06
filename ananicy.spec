Name:		ananicy
Version:	2.0.0
Release:	1
Summary:	ANother Auto NICe daemon
License:	GPLv3+
URL:		https://github.com/Nefelim4ag/Ananicy
Source0:	https://github.com/Nefelim4ag/Ananicy/archive/Ananicy-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	systemd-macros
Requires:	schedtool

%description
ANother Auto NICe daemon.

%prep
%autosetup -n Ananicy-%{version} -p1
sed -i 's|#!/usr/bin/env python3|#%{_python}|' ananicy.py

%build

%install
%make_install PREFIX="%{buildroot}"
mv "%{buildroot}/lib" "%{buildroot}%{_prefix}"

%files
%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/ananicy.d/ananicy.conf
%config %{_sysconfdir}/ananicy.d/00-*
%{_sysconfdir}/ananicy.d
%{_unitdir}/ananicy.service
