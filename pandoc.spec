%global pkg_name pandoc

%global common_summary Haskell %{pkg_name} library

%global common_description Pandoc is a Haskell library for converting from one markup format to another,\
and a command-line tool that uses this library. It can read markdown and\
(subsets of) reStructuredText, HTML, and LaTeX, and it can write markdown,\
reStructuredText, HTML, LaTeX, ConTeXt, Docbook, OpenDocument, ODT, RTF,\
MediaWiki, groff man pages, EPUB, and S5 and Slidy HTML slide shows.

%global ghc_pkg_deps ghc-HTTP-devel, ghc-mtl-devel, ghc-network-devel, ghc-parsec-devel, ghc-texmath-devel, ghc-utf8-string-devel, ghc-xhtml-devel, ghc-xml-devel, ghc-zip-archive-devel

# debuginfo is not useful for ghc
%global debug_package %{nil}

Name:           %{pkg_name}
Version:        1.6.0.1
Release:        1%{?dist}
Summary:        Markup converter for markdown

Group:          Applications/Publishing
License:        GPLv2+
URL:            http://hackage.haskell.org/package/%{name}
Source0:        http://hackage.haskell.org/packages/archive/%{name}/%{version}/%{name}-%{version}.tar.gz
# fedora ghc archs:
ExclusiveArch:  %{ix86} x86_64 ppc alpha
BuildRequires:  ghc, ghc-doc, ghc-prof
BuildRequires:  ghc-rpm-macros >= 0.7.3
BuildRequires:  hscolour
%{?ghc_pkg_deps:BuildRequires:  %{ghc_pkg_deps}, %(echo %{ghc_pkg_deps} | sed -e "s/\(ghc-[^, ]\+\)-devel/\1-doc,\1-prof/g")}

%description
%{common_description}


%prep
%setup -q


%build
%ghc_lib_build


%install
%ghc_lib_install

rm $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/{BUGS,COPYRIGHT,INSTALL,README,changelog}


%{?ghc_binlib_package}


%files
%defattr(-,root,root,-)
%doc BUGS COPYING COPYRIGHT README
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/markdown2pdf
%{_datadir}/%{name}-%{version}
%{_mandir}/man1/*


%changelog
* Fri Jan 14 2011 Jens Petersen <petersen@redhat.com> - 1.6.0.1-1
- 1.6.0.1
- add description
- update to cabal2spec-0.22.4

* Fri Nov 12 2010 Jens Petersen <petersen@redhat.com> - 1.6-1
- GPLv2+
- take care of docdir files
- add dependencies

* Thu Nov 11 2010 Fedora Haskell SIG <haskell-devel@lists.fedoraproject.org> - 1.6-0
- initial packaging for Fedora automatically generated by cabal2spec-0.22.2
