Name: livepatch-build-tools
Summary: Xen LivePatch patch builder
Version: 0.1
Release: 1

Group: Development/Tools
License: GPLv2
URL: http://xenbits.xen.org/gitweb/?p=livepatch-build-tools.git
Patch0: 0001-Ignore-.discard-sections.patch
Patch1: 0001-Remove-section-alignment-requirement.patch
Source0: https://code.citrite.net/rest/archive/latest/projects/XSU/repos/%{name}/archive?at=2af6f1aa62334f8c3d66cf2c5043686833de6cc6&format=tar.gz&prefix=%{name}-%{version}#/%{name}-%{version}.tar.gz

Requires: binutils
BuildRequires: gcc elfutils elfutils-devel


%description
Builds live patches for Xen LivePatch. It uses the Xen source tree and a
source patch to create a live patch.


%prep
%autosetup -p1 -n livepatch-build-tools-0.1


%build
make


%install
make install PREFIX=/usr DESTDIR=%{buildroot}


%files
%{_bindir}/livepatch-build
%{_libexecdir}/livepatch-build-tools


%changelog
