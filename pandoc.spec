# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name pandoc

Name:           %{pkg_name}
Version:        1.11.1
Release:        5%{?dist}
Summary:        Markup conversion tool for markdown

License:        GPLv2+
URL:            http://hackage.haskell.org/package/%{name}
Source0:        http://hackage.haskell.org/packages/archive/%{name}/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-HTTP-devel
BuildRequires:  ghc-base64-bytestring-devel
BuildRequires:  ghc-blaze-html-devel
BuildRequires:  ghc-blaze-markup-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-citeproc-hs-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-data-default-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-extensible-exceptions-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-highlighting-kate-devel
BuildRequires:  ghc-json-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-old-locale-devel
BuildRequires:  ghc-old-time-devel
BuildRequires:  ghc-pandoc-types-devel
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-syb-devel
BuildRequires:  ghc-tagsoup-devel
BuildRequires:  ghc-temporary-devel
BuildRequires:  ghc-texmath-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-xml-devel
BuildRequires:  ghc-zip-archive-devel
BuildRequires:  ghc-zlib-devel
# End cabal-rpm deps
BuildRequires:  chrpath

%description
Pandoc is a tool and Haskell library for converting markup formats.
It can read markdown and (subsets of) HTML, reStructuredText, LaTeX, DocBook,
MediaWiki markup, and Textile, and can write markdown, reStructuredText, HTML,
LaTeX, ConTeXt, Docbook, OpenDocument, ODT, Word docx, RTF, MediaWiki, Textile,
groff man pages, plain text, Emacs Org-Mode, AsciiDoc, EPUB, FictionBook2, and
S5, Slidy and Slideous HTML slide-shows.

Pandoc extends standard markdown syntax with footnotes, embedded LaTeX,
definition lists, tables, and other features. A compatibility mode is
provided for those who need a drop-in replacement for Markdown.pl.

For pdf output please also install pandoc-pdf.


%package -n ghc-%{name}
Summary:        Haskell %{name} library

%description -n ghc-%{name}
This package provides the Haskell %{name} shared library.


%package -n ghc-%{name}-devel
Summary:        Haskell %{name} library development files
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}
Requires:       ghc-%{name} = %{version}-%{release}

%description -n ghc-%{name}-devel
This package provides the Haskell %{name} library development files.


%package pdf
Summary:        Metapackage for pandoc pdf support
Requires:       %{name} = %{version}
Requires:       texlive-collection-latex
Requires:       texlive-ec
Obsoletes:      pandoc-markdown2pdf < %{version}-%{release}
Obsoletes:      pandoc-pdf < %{version}-%{release}

%description pdf
This package pulls in the TeXLive latex package collection needed by
pandoc to generate pdf output using pdflatex.

To use --latex-engine=xelatex or lualatex, install texlive-collection-xetex
or texlive-collection-luatex respectively.


%prep
%setup -q


%build
%ghc_lib_build


%install
%ghc_lib_install

rm %{buildroot}%{_datadir}/%{name}-%{version}/{BUGS,COPYRIGHT,INSTALL,README,changelog}

ln -s pandoc %{buildroot}%{_bindir}/hsmarkdown

%ghc_fix_dynamic_rpath pandoc


%post -n ghc-%{name}-devel
%ghc_pkg_recache


%postun -n ghc-%{name}-devel
%ghc_pkg_recache


%files
%doc BUGS COPYING COPYRIGHT README* changelog
%attr(755,root,root) %{_bindir}/%{name}
%attr(-,root,root) %{_bindir}/hsmarkdown
%{_datadir}/%{name}-%{version}
%attr(644,root,root) %{_mandir}/man1/pandoc.1*
%attr(644,root,root) %{_mandir}/man5/*


%files pdf


%files -n ghc-%{name} -f ghc-%{name}.files
%doc COPYING COPYRIGHT


%files -n ghc-%{name}-devel -f ghc-%{name}-devel.files


%changelog
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
