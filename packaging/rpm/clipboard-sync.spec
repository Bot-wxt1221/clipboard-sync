Name:           clipboard-sync
Version:        0.2.0
Release:        1%{?dist}
Summary:        Synchronizes the clipboard across multiple X11 and wayland instances

License:        None
URL:            https://github.com/dnut/clipboard-sync
Source0:        clipboard-sync-v%{version}.tar.gz

BuildRequires:  rust >= 1.60
BuildRequires:  cargo
BuildRequires:  libxcb-devel
BuildRequires:  systemd-rpm-macros

Requires:       libxcb

%description
Synchronizes the clipboard across multiple X11 and wayland instances running 
on the same machine. This is useful for running multiple desktop sessions
or sharing clipboard content between different display environments.

%prep
%autosetup -n %{name}-v%{version}

%build
make

%install
make prefix=%{buildroot} bin=%{_bindir} user_unit_dir=%{_userunitdir} install

%files
%doc README.md
%{_bindir}/%{name}
%{_userunitdir}/clipboard-sync.service

%changelog
* Tue Sep 30 2025 - 0.2.0-1
- Initial RPM package for clipboard-sync
