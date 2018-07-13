# generated by cabal-rpm-0.12.1
# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name doctest
%global pkgver %{pkg_name}-%{version}

%bcond_without tests

Name:           ghc-%{pkg_name}
Version:        0.13.0
Release:        3%{?dist}
Summary:        Test interactive Haskell examples

License:        MIT
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  chrpath
BuildRequires:  ghc-base-compat-devel
BuildRequires:  ghc-code-page-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-ghc-devel
BuildRequires:  ghc-ghc-paths-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-syb-devel
BuildRequires:  ghc-transformers-devel
%if %{with tests}
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-mockery-devel
BuildRequires:  ghc-setenv-devel
BuildRequires:  ghc-silently-devel
BuildRequires:  ghc-stringbuilder-devel
BuildRequires:  ghc-with-location-devel
%endif
# End cabal-rpm deps

%description
The doctest program checks examples in source code comments. It is modeled
after doctest for Python (<https://docs.python.org/library/doctest.html>).

Documentation is at <https://github.com/sol/doctest#readme>.


%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the Haskell %{pkg_name} library development files.


%prep
%setup -q -n %{pkgver}


%build
%ghc_lib_build


%install
%ghc_lib_install
%ghc_fix_rpath %{pkgver}


%check
%cabal_test


%post devel
%ghc_pkg_recache


%postun devel
%ghc_pkg_recache


%files -f %{name}.files
%license LICENSE


%files devel -f %{name}-devel.files
%doc example
%{_bindir}/%{pkg_name}


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Apr 18 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.13.0-2
- Enable tests

* Thu Apr 12 2018 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.13.0-1
- spec file generated by cabal-rpm-0.12.1
