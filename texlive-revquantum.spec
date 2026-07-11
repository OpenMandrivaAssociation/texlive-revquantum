%global tl_name revquantum
%global tl_revision 43505

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.11
Release:	%{tl_revision}.1
Summary:	Hacks to make writing quantum papers for revtex4-1 less painful
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/revquantum
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/revquantum.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/revquantum.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/revquantum.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a number of useful hacks to solve common
annoyances with the revtex4-1 package, and to define notation in common
use within quantum information. In doing so, it imports and configures a
number of commonly-available and used packages, and where reasonable,
provides fallbacks. It also warns when users try to load packages which
are known to be incompatible with revtex4-1.

