Name:		texlive-mpattern
Version:	15878
Release:	2
Summary:	Patterns in MetaPost
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/mpattern
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mpattern.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mpattern.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A package for defining and using patterns in MetaPost, using
the Pattern Color Space available in PostScript Level 2.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/metapost/mpattern/mpattern.mp
%doc %{_texmfdistdir}/doc/metapost/mpattern/README
%doc %{_texmfdistdir}/doc/metapost/mpattern/README.PL
%doc %{_texmfdistdir}/doc/metapost/mpattern/mpattern_test.pdf
%doc %{_texmfdistdir}/doc/metapost/mpattern/mpattern_test.tex
%doc %{_texmfdistdir}/doc/metapost/mpattern/test.mp

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar metapost doc %{buildroot}%{_texmfdistdir}
