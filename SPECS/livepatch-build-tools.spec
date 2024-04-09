%global package_speccommit 526a4253e1244533d1b797dfb69e3a04978aba30
%global usver 20240223
%global xsver 1
%global xsrel %{xsver}%{?xscount}%{?xshash}
%global package_srccommit ae65ea21e27f861ac10cebc006b9b4bbb3b3dbbc

Name: livepatch-build-tools
Summary: Xen LivePatch patch builder
Version: 20240223
Release: %{?xsrel}%{?dist}

Group: Development/Tools
License: GPLv2
URL: http://xenbits.xen.org/gitweb/?p=livepatch-build-tools.git
Source0: livepatch-build-tools-20240223.tar.gz
Patch0: 0001-Allow-patching-files-compiled-multiple-times.patch
Patch1: 0001-create-diff-object-Mark-correlated-static-local-vari.patch
Patch2: 0001-livepatch-build-tools-allow-patch-name-sizes-up-to-1.patch

Requires: binutils
BuildRequires: gcc elfutils elfutils-devel
%{?_cov_buildrequires}


%description
Builds live patches for Xen LivePatch. It uses the Xen source tree and a source patch to create a live patch.


%prep
%autosetup -p1
%{?_cov_prepare}


%build
%{?_cov_wrap} make


%install
make install PREFIX=/usr DESTDIR=%{buildroot}
%{?_cov_install}


%files
%{_bindir}/livepatch-build
%{_libexecdir}/livepatch-build-tools

%{?_cov_results_package}


%changelog
* Fri Feb 23 2024 Andrew Cooper <andrew.cooper3@citrix.com> - 20240223-1
- Fix inclusion of new object files.

* Wed Jan 31 2024 Roger Pau Monné <roger.pau@citrix.com> - 20231213-1
- Update and drop 4.13 compat reverts.
- Allow livepatch file name sizes up to 128 characters.

* Thu Jan 18 2024 Roger Pau Monné <roger.pau@citrix.com> - 20231113-2
- Add extra revert to keep Xen 4.13 ABI.

* Mon Nov 27 2023 Andrew Cooper <andrew.cooper3@citrix.com> - 20231113-1
- Fix building live patches with dev-toolset-11

* Mon Nov 27 2023 Andrew Cooper <andrew.cooper3@citrix.com> - 20191203-1
- Change versioning scheme to avoid an arbitrary 0.1.  Use the date of the
  upstream livepatch-build-tools commit.

* Tue Nov 02 2021 Igor Druzhinin <igor.druzhinin@citrix.com> - 0.1-3.0.2
- CP-38201: Enable static analysis with Coverity

* Sun Jan 17 2021 Igor Druzhinin <igor.druzhinin@citrix.com> - 0.1-3.0.1
- CP-35595: Convert patchqueue to Koji spec repo

* Thu Dec 05 2019 Sergey Dyasli <sergey.dyasli@citrix.com> - 0.1-3.0.0
- Resync with upstream

* Wed May 15 2019 Sergey Dyasli <sergey.dyasli@citrix.com> - 0.1-2.0.2
- Fix description string

* Wed Mar 27 2019 Ross Lagerwall <ross.lagerwall@citrix.com> - 0.1-2.0.1
- CA-312246: Fix building with static variables in special sections
