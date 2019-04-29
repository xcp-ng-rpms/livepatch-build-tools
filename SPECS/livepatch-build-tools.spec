Name: livepatch-build-tools
Summary: Xen LivePatch patch builder
Version: 0.1
Release: 2

Group: Development/Tools
License: GPLv2
URL: http://xenbits.xen.org/gitweb/?p=livepatch-build-tools.git

Source0: https://code.citrite.net/rest/archive/latest/projects/XSU/repos/livepatch-build-tools/archive?at=0c104573a1c168995ec553778d1d2d1ebe9c9042&format=tar.gz&prefix=livepatch-build-tools-0.1#/livepatch-build-tools-0.1.tar.gz

Patch0: 0001-Allow-patching-files-compiled-multiple-times.patch
Patch1: 0001-Xen-4.11-fix-altinstructions_group_size.patch

Provides: gitsha(https://code.citrite.net/rest/archive/latest/projects/XSU/repos/livepatch-build-tools/archive?at=0c104573a1c168995ec553778d1d2d1ebe9c9042&format=tar.gz&prefix=livepatch-build-tools-0.1#/livepatch-build-tools-0.1.tar.gz) = 0c104573a1c168995ec553778d1d2d1ebe9c9042
Provides: gitsha(https://code.citrite.net/rest/archive/latest/projects/XS/repos/livepatch-build-tools.pg/archive?at=2.0.0&format=tar#/livepatch-build-tools.pg.tar) = f43be440bf2c1b5f5982d2d1f6631ed62a36f758


Requires: binutils
BuildRequires: gcc elfutils elfutils-devel


%description
Builds live patches for Xen LivePatch. It uses the Xen source tree and a


%prep
%autosetup -p1


%build
make


%install
make install PREFIX=/usr DESTDIR=%{buildroot}


%files
%{_bindir}/livepatch-build
%{_libexecdir}/livepatch-build-tools


%changelog
