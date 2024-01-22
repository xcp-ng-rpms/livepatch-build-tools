%global package_speccommit dd1c0d7171a1fb373d48b85608e152c4a061a675
%global usver 20231113
%global xsver 1
%global xsrel %{xsver}%{?xscount}%{?xshash}
%global package_srccommit e588b7914e7afa3abb64b15a32fc2fdb57ded341

Name: livepatch-build-tools
Summary: Xen LivePatch patch builder
Version: 20231113
Release: %{?xsrel}%{?dist}

Group: Development/Tools
License: GPLv2
URL: http://xenbits.xen.org/gitweb/?p=livepatch-build-tools.git
Source0: livepatch-build-tools-20231113.tar.gz
Patch0: 0001-Allow-patching-files-compiled-multiple-times.patch
Patch1: 0001-create-diff-object-Mark-correlated-static-local-vari.patch
Patch2: revert-2142f99087e8.patch

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
