# cabal2spec-0.25.2
# https://fedoraproject.org/wiki/Packaging:Haskell
# https://fedoraproject.org/wiki/PackagingDrafts/Haskell

%global pkg_name pandoc

%global common_summary Haskell %{pkg_name} library

%global common_description Pandoc is a Haskell library for converting from one markup format to another,\
and a command-line tool that uses this library. It can read markdown and\
(subsets of) reStructuredText, HTML, and LaTeX, and it can write markdown,\
reStructuredText, HTML, LaTeX, ConTeXt, Docbook, OpenDocument, ODT, RTF,\
MediaWiki, groff man pages, EPUB, and S5 and Slidy HTML slide shows.

Name:           %{pkg_name}
Version:        1.9.1.1
Release:        1%{?dist}
Summary:        Markup conversion tool for markdown

Group:          Applications/Publishing
License:        GPLv2+
# BEGIN cabal2spec
URL:            http://hackage.haskell.org/package/%{name}
Source0:        http://hackage.haskell.org/packages/archive/%{name}/%{version}/%{name}-%{version}.tar.gz
ExclusiveArch:  %{ghc_arches}
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros %{!?without_hscolour:hscolour}
# END cabal2spec
BuildRequires:  ghc-base64-bytestring-prof
BuildRequires:  ghc-citeproc-hs-prof
BuildRequires:  ghc-dlist-prof
BuildRequires:  ghc-highlighting-kate-prof
BuildRequires:  ghc-HTTP-prof
BuildRequires:  ghc-json-prof
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-network-prof
BuildRequires:  ghc-pandoc-types-prof
BuildRequires:  ghc-parsec-prof
BuildRequires:  ghc-tagsoup-prof
BuildRequires:  ghc-texmath-prof
BuildRequires:  ghc-utf8-string-prof
BuildRequires:  ghc-xhtml-prof
BuildRequires:  ghc-xml-prof
BuildRequires:  ghc-zip-archive-prof
BuildRequires:  ghc-extensible-exceptions-prof
BuildRequires:  ghc-random-prof
Obsoletes:      pandoc-markdown2pdf < %{version}-%{release}
# these two patches should be removed when texlive gets updated
Patch1:         pandoc-default.latex-no-luatex.patch
#Patch2:         pandoc-1.8.2.1-texlive2007-xelatex-outputdir.patch

%description
%{common_description}


%prep
%setup -q
%patch1 -p1 -b .orig
#%%patch2 -p1 -b .orig


%build
%ghc_lib_build


%install
%ghc_lib_install

rm %{buildroot}%{_datadir}/%{name}-%{version}/{BUGS,COPYRIGHT,INSTALL,README,changelog}

%ghc_package

%ghc_description


%ghc_devel_package

%ghc_devel_description


%ghc_devel_post_postun


%files
%doc BUGS COPYING COPYRIGHT README* changelog
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}-%{version}
%attr(644,root,root) %{_mandir}/man1/pandoc.1*
%attr(644,root,root) %{_mandir}/man5/*


%ghc_files


%changelog
* Mon Feb 13 2012 Jens Petersen <petersen@redhat.com> - 1.9.1.1-1
- update to 1.9.1.1
  http://johnmacfarlane.net/pandoc/releases.html#pandoc-1.9.1.1-2012-02-11
- markdown2pdf is now handled by pandoc itself:
  add README.fedora file documenting required texlive packages
- add changelog file

* Fri Feb 10 2012 Petr Pisar <ppisar@redhat.com> - 1.8.2.1-9
- Rebuild against PCRE 8.30

* Tue Feb  7 2012 Jens Petersen <petersen@redhat.com> - 1.8.2.1-8
- rebuild

* Thu Jan 26 2012 Jens Petersen <petersen@redhat.com> - 1.8.2.1-7
- set highlighting build flag by patching instead to help dependency tracking

* Fri Jan  6 2012 Jens Petersen <petersen@redhat.com> - 1.8.2.1-6
- update to cabal2spec-0.25.2

* Thu Dec 22 2011 Jens Petersen <petersen@redhat.com> - 1.8.2.1-5
- workaround texlive-2007 xelatex outputting to current dir

* Wed Nov 30 2011 Jens Petersen <petersen@redhat.com> - 1.8.2.1-4
- add missing requires for pdflatex

* Thu Nov 17 2011 Jens Petersen <petersen@redhat.com> - 1.8.2.1-3
- disable ifluatex in default.latex for texlive-2007 (Luis Villa, #752621)
- subpackage markdown2pdf and make it require texlive-xetex

* Wed Oct 26 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.8.2.1-2.2
- rebuild with new gmp without compat lib

* Wed Oct 12 2011 Peter Schiffer <pschiffe@redhat.com> - 1.8.2.1-2.1
- rebuild with new gmp

* Mon Oct  3 2011 Jens Petersen <petersen@redhat.com> - 1.8.2.1-2
- rebuild against newer dependencies

* Thu Aug  4 2011 Jens Petersen <petersen@redhat.com> - 1.8.2.1-1
- update to 1.8.2.1
- depends on base64-bytestring

* Wed Jul 27 2011 Jens Petersen <petersen@redhat.com> - 1.8.1.2-3
- rebuild for xml-1.3.9

* Fri Jul 22 2011 Jens Petersen <petersen@redhat.com> - 1.8.1.2-2
- rebuild for highlighting-kate-0.2.10

* Thu Jul 21 2011 Jens Petersen <petersen@redhat.com> - 1.8.1.2-1
- update to 1.8.1.2

* Wed Jul 13 2011 Jens Petersen <petersen@redhat.com> - 1.8.1.1-3
- build with code highlighting support using highlighting-kate

* Wed Jun 22 2011 Jens Petersen <petersen@redhat.com> - 1.8.1.1-2
- BR ghc-Cabal-devel instead of ghc-prof and use ghc_arches (cabal2spec-0.23.2)

* Sat May 28 2011 Jens Petersen <petersen@redhat.com> - 1.8.1.1-1
- update to 1.8.1.1
- update to cabal2spec-0.23: add ppc64
- new depends on citeproc-hs, dlist, json, pandoc-types, tagsoup
- new pandoc_markdown.5 manpage

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
