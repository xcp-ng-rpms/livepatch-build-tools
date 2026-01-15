%global package_speccommit 862b6008ca947f324ea43c1af4b789be3650bfe1
%global usver 20250729
%global xsver 2
%global xsrel %{xsver}%{?xscount}%{?xshash}
%global package_srccommit 07043f274059e1575008ba9db1db02bffa4fc169

Name: livepatch-build-tools
Summary: Xen LivePatch patch builder
Version: 20250729
Release: %{?xsrel}%{?dist}

Group: Development/Tools
License: GPLv2
URL: http://xenbits.xen.org/gitweb/?p=livepatch-build-tools.git
Source0: livepatch-build-tools-20250729.tar.gz
Patch0: 0001-Allow-patching-files-compiled-multiple-times.patch
Patch1: 0001-create-diff-object-Mark-correlated-static-local-vari.patch
Patch2: 001-Use-new-original-xen-syms
Patch3: CP-50319-implement-livepatch-signing.patch
Patch4: 0001-common-allow-function-symbols-with-offsets-inside-se.patch

%if "%{dist}" == ".xs8~2_1"
# Xen 4.13 compat
Patch1000: revert-2142f99087e8.patch
Patch1001: revert-615a7786d1d2.patch
%endif

Requires: binutils
Requires: perl-interpreter
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
%{_bindir}/livepatch-sign
%{_libexecdir}/livepatch-build-tools

%{?_cov_results_package}


%changelog
* Mon Sep 08 2025 Roger Pau Monné <roger.pau@citrix.com> - 20250729-2
- Support functions that have offsets from the section start

* Tue Jul 29 2025 Frediano Ziglio <frediano.ziglio@cloud.com> - 20250729-1
- Allows dynamic sizes for build IDs.

* Thu Apr 17 2025 Gerald Elder-Vass <geraldl.elder-vass@cloud.com> - 20250121-4
- CP-51534: Update signing to work with HSM

* Mon Apr 14 2025 Ross Lagerwall <ross.lagerwall@citrix.com> - 20250121-3
- CP-50319: Implement livepatch signing

* Thu Mar 06 2025 Ross Lagerwall <ross.lagerwall@citrix.com> - 20250121-2
- Add perl as a runtime dependency

* Tue Jan 21 2025 Roger Pau Monné <roger.pau@citrix.com> - 20250121-1
- Fix handling of .cold symbols and related secions.
- Fix possible segmentation fault when using hook sections.

* Wed Apr 10 2024 Alejandro Vallejo <alejandro.vallejo@cloud.com> - 20240223-3
- Branched off livepatch-build-tools-20240223-2.xs8
- Revert ABI breakages on Xen 4.13

* Mon Apr 08 2024 Alejandro Vallejo <alejandro.vallejo@cloud.com> - 20240223-2
- Make the tooling use a locally compiled "xen-syms" rather than the originally
  archived one

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
