%global package_speccommit 03df930513dbe586efeeb0bc418820ce5eacc061
%global usver 0.1
%global xsver 3.0.2
%global xsrel %{xsver}%{?xscount}%{?xshash}
%global package_srccommit a1277bfa9c6e82ba03edd6c931672505afe75477

Name: livepatch-build-tools
Summary: Xen LivePatch patch builder
Version: 0.1
Release: %{?xsrel}%{?dist}

Group: Development/Tools
License: GPLv2
URL: http://xenbits.xen.org/gitweb/?p=livepatch-build-tools.git
Source0: livepatch-build-tools-0.1.tar.gz
Patch0: 0001-Allow-patching-files-compiled-multiple-times.patch
Patch1: 0001-create-diff-object-Mark-correlated-static-local-vari.patch

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
