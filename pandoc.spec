%global pkg_name pandoc

%global common_summary Haskell %{pkg_name} library

%global common_description Pandoc is a Haskell library for converting from one markup format to another,\
and a command-line tool that uses this library. It can read markdown and\
(subsets of) reStructuredText, HTML, and LaTeX, and it can write markdown,\
reStructuredText, HTML, LaTeX, ConTeXt, Docbook, OpenDocument, ODT, RTF,\
MediaWiki, groff man pages, EPUB, and S5 and Slidy HTML slide shows.

Name:           %{pkg_name}
Version:        1.8.1.1
Release:        1%{?dist}
Summary:        Markup conversion tool for markdown

Group:          Applications/Publishing
License:        GPLv2+
URL:            http://hackage.haskell.org/package/%{name}
Source0:        http://hackage.haskell.org/packages/archive/%{name}/%{version}/%{name}-%{version}.tar.gz
# fedora ghc archs:
ExclusiveArch:  %{ix86} x86_64 ppc alpha sparcv9 ppc64
BuildRequires:  ghc-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  hscolour
BuildRequires:  ghc-citeproc-hs-prof, ghc-dlist-prof, ghc-HTTP-prof, ghc-json-prof, ghc-mtl-prof, ghc-network-prof, ghc-pandoc-types-prof, ghc-parsec-prof, ghc-tagsoup-prof, ghc-texmath-prof, ghc-utf8-string-prof, ghc-xhtml-prof, ghc-xml-prof, ghc-zip-archive-prof, 

%description
%{common_description}


%prep
%setup -q


%build
%ghc_lib_build


%install
%ghc_lib_install

rm %{buildroot}%{_datadir}/%{name}-%{version}/{BUGS,COPYRIGHT,INSTALL,README,changelog}


%ghc_binlib_package


%files
%defattr(-,root,root,-)
%doc BUGS COPYING COPYRIGHT README
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/markdown2pdf
%{_datadir}/%{name}-%{version}
%attr(644,root,root) %{_mandir}/man1/*


%changelog
* Sat May 28 2011 Jens Petersen <petersen@redhat.com> - 1.8.1.1-1
- update to 1.8.1.1
- update to cabal2spec-0.23: add ppc64
- new depends on citeproc-hs, dlist, json, pandoc-types, tagsoup

* Thu Mar 10 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 1.6.0.1-5
- Enable build on sparcv9

* Tue Feb 15 2011 Jens Petersen <petersen@redhat.com> - 1.6.0.1-4
- rebuild for latest zip-archive and haskell-platform-2011.1 updates

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 31 2011 Jens Petersen <petersen@redhat.com> - 1.6.0.1-2
- fix manpage perms (narasim)
- improve the summary (#652582)

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
