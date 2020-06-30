Name: livepatch-build-tools
Summary: Xen LivePatch patch builder
Version: 0.1
Release: 3.0.0%{?dist}

Group: Development/Tools
License: GPLv2
URL: http://xenbits.xen.org/gitweb/?p=livepatch-build-tools.git

Source0: https://code.citrite.net/rest/archive/latest/projects/XSU/repos/livepatch-build-tools/archive?at=a1277bfa9c6e82ba03edd6c931672505afe75477&format=tar.gz&prefix=livepatch-build-tools-0.1#/livepatch-build-tools-0.1.tar.gz

Patch0: 0001-Allow-patching-files-compiled-multiple-times.patch
Patch1: 0001-create-diff-object-Mark-correlated-static-local-vari.patch

Provides: gitsha(https://code.citrite.net/rest/archive/latest/projects/XS/repos/livepatch-build-tools.pg/archive?at=3.0.0&format=tar#/livepatch-build-tools.pg.tar) = dd420b9013f901cbea99b3db30bed3d4651ba646


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
* Thu Dec 05 2019 Sergey Dyasli <sergey.dyasli@citrix.com> - 0.1-3.0.0
- Resync with upstream

* Wed May 15 2019 Sergey Dyasli <sergey.dyasli@citrix.com> - 0.1-2.0.2
- Fix description string

* Wed Mar 27 2019 Ross Lagerwall <ross.lagerwall@citrix.com> - 0.1-2.0.1
- CA-312246: Fix building with static variables in special sections
