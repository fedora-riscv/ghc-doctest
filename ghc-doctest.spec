# generated by cabal-rpm-1.0.0
# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name doctest
%global pkgver %{pkg_name}-%{version}

%bcond_with tests

Name:           ghc-%{pkg_name}
Version:        0.16.0.1
Release:        3%{?dist}
Summary:        Test interactive Haskell examples

License:        MIT
Url:            https://hackage.haskell.org/package/%{pkg_name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
%if %{with haddock}
BuildRequires:  ghc-doc
%endif
%if %{with ghc_prof}
BuildRequires:  ghc-prof
%endif
BuildRequires:  ghc-rpm-macros
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
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the Haskell %{pkg_name} library development files.


%if %{with haddock}
%package doc
Summary:        Haskell %{pkg_name} library documentation

%description doc
This package provides the Haskell %{pkg_name} library documentation.
%endif


%if %{with ghc_prof}
%package prof
Summary:        Haskell %{pkg_name} profiling library
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description prof
This package provides the Haskell %{pkg_name} profiling library.
%endif


%prep
# Begin cabal-rpm setup:
%setup -q -n %{pkgver}
# End cabal-rpm setup


%build
# Begin cabal-rpm build:
%ghc_lib_build
# End cabal-rpm build


%install
# Begin cabal-rpm install
%ghc_lib_install
# End cabal-rpm install


%check
%cabal_test


%files -f %{name}.files
# Begin cabal-rpm files:
%license LICENSE
# End cabal-rpm files


%files devel -f %{name}-devel.files
%doc CHANGES README.markdown example
%{_bindir}/%{pkg_name}


%if %{with haddock}
%files doc -f %{name}-doc.files
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
* Thu Aug 01 2019 Jens Petersen <petersen@redhat.com> - 0.16.0.1-3
- add doc and prof subpackages (cabal-rpm-1.0.0)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 21 2019 Jens Petersen <petersen@redhat.com> - 0.16.0.1-1
- update to 0.16.0.1
- disable testsuite (needs cabal-install)

* Sun Feb 17 2019 Jens Petersen <petersen@redhat.com> - 0.13.0-6
- refresh to cabal-rpm-0.13

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 28 2018 Jens Petersen <petersen@redhat.com> - 0.13.0-4
- rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Apr 18 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.13.0-2
- Enable tests

* Thu Apr 12 2018 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.13.0-1
- spec file generated by cabal-rpm-0.12.1
