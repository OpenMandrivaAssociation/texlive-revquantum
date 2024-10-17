Name:		texlive-revquantum
Version:	43505
Release:	2
Summary:	Hacks to make writing quantum papers for revtex4-1 less painful
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/revquantum
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/revquantum.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/revquantum.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/revquantum.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a number of useful hacks to solve common
annoyances with the revtex4-1 package, and to define notation
in common use within quantum information. In doing so, it
imports and configures a number of commonly-available and used
packages, and where reasonable, provides fallbacks. It also
warns when users try to load packages which are known to be
incompatible with revtex4-1.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/revquantum
%{_texmfdistdir}/tex/latex/revquantum
%doc %{_texmfdistdir}/doc/latex/revquantum

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
