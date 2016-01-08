%global pandoc_ver 1.16
%global pandoc_citeproc_ver 0.9

# nothing to see here
%global debug_package %{nil}

Name:           pandoc
Version:        %{pandoc_ver}
# reset only when both versioned bumped
Release:        1%{?dist}
Summary:        Conversion between markup formats

License:        GPLv2+
Url:            https://hackage.haskell.org/package/%{name}
Source0:        https://hackage.haskell.org/package/%{name}/%{version}/%{name}-%{version}.tar.gz
Source1:        https://hackage.haskell.org/package/%{name}-citeproc/%{pandoc_citeproc_ver}/%{name}-citeproc-%{pandoc_citeproc_ver}.tar.gz

BuildRequires:  ghc-Cabal-devel
#BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  alex
BuildRequires:  ghc-HTTP-devel
%if 0%{?rhel} > 6
BuildRequires:  ghc-JuicyPixels-devel
BuildRequires:  ghc-SHA-devel
BuildRequires:  ghc-aeson-devel
%endif
BuildRequires:  ghc-array-devel
%if 0%{?rhel} > 6
BuildRequires:  ghc-base64-bytestring-devel
%endif
BuildRequires:  ghc-binary-devel
%if 0%{?rhel} > 6
BuildRequires:  ghc-blaze-html-devel
BuildRequires:  ghc-blaze-markup-devel
%endif
BuildRequires:  ghc-bytestring-devel
#BuildRequires:  ghc-cmark-devel
BuildRequires:  ghc-containers-devel
%if 0%{?rhel} > 6
BuildRequires:  ghc-data-default-devel
%endif
#BuildRequires:  ghc-deepseq-generics-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-extensible-exceptions-devel
#BuildRequires:  ghc-filemanip-devel
BuildRequires:  ghc-filepath-devel
#BuildRequires:  ghc-haddock-library-devel
%if 0%{?rhel} > 6
BuildRequires:  ghc-highlighting-kate-devel
BuildRequires:  ghc-hslua-devel
%endif
#BuildRequires:  ghc-http-client-devel
#BuildRequires:  ghc-http-client-tls-devel
#BuildRequires:  ghc-http-types-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-network-devel
%if 0%{?fedora} >= 24
BuildRequires:  ghc-network-uri-devel
%endif
BuildRequires:  ghc-old-locale-devel
BuildRequires:  ghc-old-time-devel
%if 0%{?rhel} > 6
BuildRequires:  ghc-pandoc-types-devel
%endif
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-random-devel
%if 0%{?rhel} > 6
BuildRequires:  ghc-scientific-devel
%endif
BuildRequires:  ghc-syb-devel
%if 0%{?rhel} > 6
BuildRequires:  ghc-tagsoup-devel
BuildRequires:  ghc-temporary-devel
BuildRequires:  ghc-texmath-devel
%endif
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
%if 0%{?rhel} > 6
BuildRequires:  ghc-unordered-containers-devel
%endif
BuildRequires:  ghc-vector-devel
%if 0%{?rhel} > 6
BuildRequires:  ghc-xml-devel
BuildRequires:  ghc-yaml-devel
BuildRequires:  ghc-zip-archive-devel
%endif
BuildRequires:  ghc-zlib-devel
BuildRequires:  happy
%if %{with tests}
BuildRequires:  ghc-Diff-devel
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-ansi-terminal-devel
BuildRequires:  ghc-executable-path-devel
BuildRequires:  ghc-test-framework-devel
BuildRequires:  ghc-test-framework-hunit-devel
BuildRequires:  ghc-test-framework-quickcheck2-devel
%endif
# End cabal-rpm deps
BuildRequires:  cabal-install > 1.18
BuildRequires:  hsb2hs

%description
Pandoc is a Haskell library for converting from one markup format to another,
and a command-line tool that uses this library. It can read markdown and
(subsets of) HTML, reStructuredText, LaTeX, DocBook, MediaWiki markup, TWiki
markup, Haddock markup, OPML, Emacs Org-Mode, txt2tags and Textile, and it can
write markdown, reStructuredText, XHTML, HTML 5, LaTeX, ConTeXt, DocBook, OPML,
OpenDocument, ODT, Word docx, RTF, MediaWiki, DokuWiki, Textile, groff man
pages, plain text, Emacs Org-Mode, AsciiDoc, Haddock markup, EPUB (v2 and v3),
FictionBook2, InDesign ICML, and several kinds of HTML/javascript slide shows
(S5, Slidy, Slideous, DZSlides, reveal.js).

Pandoc extends standard markdown syntax with footnotes, embedded LaTeX,
definition lists, tables, and other features. A compatibility mode is provided
for those who need a drop-in replacement for Markdown.pl.


%package citeproc
Summary:        Supports using pandoc with citeproc
Version:        %{pandoc_citeproc_ver}
Group:          Text/Processing
License:        BSD and GPLv2+

%description citeproc
This package contains an executable: pandoc-citeproc, which works as a
pandoc filter, and also has a mode for converting bibliographic databases
a YAML format suitable for inclusion in pandoc YAML metadata.


%prep
%setup -q -a1


%build
%global cabal cabal
[ -d "$HOME/.cabal" ] || %cabal update
%cabal sandbox init
# for haddock-library hGetContents
export LANG=en_US.utf8
%cabal install -f "embed_data_files" pandoc-%{pandoc_ver} pandoc-citeproc-%{pandoc_citeproc_ver}


%install
mkdir -p %{buildroot}%{_bindir}
install -p .cabal-sandbox/bin/%{name} .cabal-sandbox/bin/%{name}-citeproc %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
# man/pandoc.1 conflicts with pandoc-common
install -p -m 644 pandoc-citeproc-%{pandoc_citeproc_ver}/man/man1/pandoc-citeproc.1 %{buildroot}%{_mandir}/man1
#install -p -m 644 man/man5/pandoc_markdown.5 %{buildroot}%{_mandir}/man5

ln -s pandoc %{buildroot}%{_bindir}/hsmarkdown


%files
%doc BUGS COPYING COPYRIGHT README changelog
%doc .cabal-sandbox/share/doc/* man/pandoc.1
%{_bindir}/%{name}
%{_bindir}/hsmarkdown
#%%{_mandir}/man1/pandoc.1*


%files citeproc
%doc pandoc-citeproc-%{pandoc_citeproc_ver}/README.md
%doc .cabal-sandbox/share/doc/*
%{_bindir}/%{name}-citeproc
%{_mandir}/man1/pandoc-citeproc.1*


%changelog
* Fri Jan  8 2016 Jens Petersen <petersen@redhat.com> - 1.16-1
- update to pandoc-1.16 and pandoc-citeproc-0.9

* Wed Nov 18 2015 Jens Petersen <petersen@redhat.com> - 1.15.2.1-1
- update to pandoc-1.15.2.1 and pandoc-citeproc-0.8.1.3

* Mon Oct 26 2015 Jens Petersen <petersen@redhat.com> - 1.15.1.1-2
- add el6 BR conditions

* Wed Oct 21 2015 Jens Petersen <petersen@redhat.com> - 1.15.1.1-1
- update to pandoc-1.15.1.1 and pandoc-citeproc-0.8.0.1

* Tue Oct  6 2015 Jens Petersen <petersen@redhat.com> - 1.15.0.6-3
- revert the obsoletes
- move manpage to docdir to avoid conflict with pandoc-common

* Tue Oct  6 2015 Jens Petersen <petersen@fedoraproject.org> - 1.15.0.6-2
- obsoletes pandoc-common and pandoc-static

* Sun Oct  4 2015 Jens Petersen <petersen@fedoraproject.org> - 1.15.0.6-1
- pandoc-1.15.0.6 and pandoc-citeproc-0.7.4

* Tue Jun 23 2015 Jens Petersen <petersen@redhat.com> - 1.14.0.4-2
- embed data files with hsb2hs
- add pandoc-citeproc subpackage

* Mon Jun  8 2015 Jens Petersen <petersen@redhat.com> - 1.14.0.4-1
- update to 1.14.0.4

* Wed Dec  3 2014 Jens Petersen <petersen@redhat.com> - 1.13.1-1
- drop epoch
- update deps
- use cabal sandbox instead of cabal-dev
- build with yaml < 0.8.10
- install manpages by hand

* Tue Jul 15 2014 Jens Petersen <petersen@fedoraproject.org> - 1:1.12.3.3-4.1
- Epoch 1 for copr
- statically link against Haskell libraries
- turn off shared and prof libs and do not package static lib
- turn off haddock
- no pdf subpackage

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 26 2014 Adam Williamson <awilliam@redhat.com> - 1.12.3.3-3
- rebuild for new ghc-scientific

* Tue May 13 2014 Jens Petersen <petersen@redhat.com> - 1.12.3.3-2
- fix building on ARM (llvm) by using -O1 (#992430)

* Thu May 08 2014 Jens Petersen <petersen@redhat.com> - 1.12.3.3-1
- update to 1.12.3.3

* Wed Jan 22 2014 Jens Petersen <petersen@redhat.com> - 1.12.3.1-1
- update to 1.12.3.1
- disable http-conduit

* Wed Aug 28 2013 Jens Petersen <petersen@redhat.com> - 1.11.1-6
- temporarily exclude armv7hl since build with ghc-7.6.3 and llvm-3.3 hanging
  mysteriously (#992430)

* Tue Aug 06 2013 Adam Williamson <awilliam@redhat.com> - 1.11.1-5
- rebuild for new libbibutils

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 10 2013 Jens Petersen <petersen@redhat.com>
- update to new simplified Haskell Packaging Guidelines

* Wed May  1 2013 Jens Petersen <petersen@redhat.com> - 1.11.1-2
- pandoc-pdf now requires texlive-collection-latex and texlive-ec (#957876)

* Fri Mar 22 2013 Jens Petersen <petersen@redhat.com> - 1.11.1-1
- update to 1.11.1

* Sun Mar 10 2013 Jens Petersen <petersen@redhat.com> - 1.10.1-1
- update to 1.10.1
- allow blaze-html-0.6

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.4.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Nov 21 2012 Jens Petersen <petersen@redhat.com> - 1.9.4.5-4
- rebuild

* Mon Nov 19 2012 Jens Petersen <petersen@redhat.com> - 1.9.4.5-3
- rebuild

* Wed Oct 31 2012 Jens Petersen <petersen@redhat.com> - 1.9.4.5-2
- drop the latex template patch for old TeXLive

* Fri Oct 26 2012 Jens Petersen <petersen@redhat.com> - 1.9.4.5-1
- update to 1.9.4.5
- refresh with cabal-rpm

* Fri Oct 26 2012 Jens Petersen <petersen@redhat.com> - 1.9.4.2-6
- disable threaded rts with upstream patch copied from Debian (#862543)

* Tue Oct  2 2012 Jens Petersen <petersen@redhat.com> - 1.9.4.2-5
- add a files section for the pdf subpackage so it is actually created

* Tue Oct  2 2012 Jens Petersen <petersen@redhat.com> - 1.9.4.2-4
- add a pdf meta-subpackage for the texlive packages needed for pdf output

* Fri Sep 28 2012 Jens Petersen <petersen@redhat.com> - 1.9.4.2-3
- also disable luatex in the default.beamer template (#861300)

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jul 15 2012 Jens Petersen <petersen@redhat.com> - 1.9.4.2-1
- update to 1.9.4.2
- add hsmarkdown symlink
- change prof BRs to devel

* Thu Jun 21 2012 Jens Petersen <petersen@redhat.com> - 1.9.4.1-2
- rebuild

* Sun Jun 10 2012 Jens Petersen <petersen@redhat.com> - 1.9.4.1-1
- update to 1.9.4.1

* Wed Apr 25 2012 Jens Petersen <petersen@redhat.com> - 1.9.2-1
- update to 1.9.2

* Wed Mar 21 2012 Jens Petersen <petersen@redhat.com> - 1.9.1.2-1
- update to 1.9.1.2

* Wed Mar  7 2012 Jens Petersen <petersen@redhat.com> - 1.9.1.1-2
- rebuild

* Mon Feb 13 2012 Jens Petersen <petersen@redhat.com> - 1.9.1.1-1
- update to 1.9.1.1
  http://johnmacfarlane.net/pandoc/releases.html#pandoc-1.9-2012-02-05
- new depends on blaze-html, temporary, zlib
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
