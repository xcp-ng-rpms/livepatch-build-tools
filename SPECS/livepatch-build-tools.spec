Name: livepatch-build-tools
Summary: Xen LivePatch patch builder
Version: 0.1
Release: 2.0.2

Group: Development/Tools
License: GPLv2
URL: http://xenbits.xen.org/gitweb/?p=livepatch-build-tools.git

Source0: https://code.citrite.net/rest/archive/latest/projects/XSU/repos/livepatch-build-tools/archive?at=0c104573a1c168995ec553778d1d2d1ebe9c9042&format=tar.gz&prefix=livepatch-build-tools-0.1#/livepatch-build-tools-0.1.tar.gz

Patch0: 0001-Allow-patching-files-compiled-multiple-times.patch
Patch1: 0001-Xen-4.11-fix-altinstructions_group_size.patch
Patch2: 0001-create-diff-object-Mark-correlated-static-local-vari.patch

Provides: gitsha(https://code.citrite.net/rest/archive/latest/projects/XS/repos/livepatch-build-tools.pg/archive?at=2.0.1&format=tar#/livepatch-build-tools.pg.tar) = c47467065fc6d033e1b559e975f5418aac8e2438


Requires: binutils
BuildRequires: gcc elfutils elfutils-devel


%description
Builds live patches for Xen LivePatch. It uses the Xen source tree and a source patch to create a live patch.


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
* Wed May 15 2019 Sergey Dyasli <sergey.dyasli@citrix.com> - 0.1-2.0.2
- Fix description string

* Wed Mar 27 2019 Ross Lagerwall <ross.lagerwall@citrix.com> - 0.1-2.0.1
- CA-312246: Fix building with static variables in special sections
