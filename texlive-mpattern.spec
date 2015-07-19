# revision 15878
# category Package
# catalog-ctan /graphics/metapost/contrib/macros/mpattern
# catalog-date 2006-12-15 22:34:26 +0100
# catalog-license pd
# catalog-version undef
Name:		texlive-mpattern
Version:	20061215
Release:	10
Summary:	Patterns in MetaPost
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/mpattern
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mpattern.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mpattern.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar metapost doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20061215-2
+ Revision: 754114
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20061215-1
+ Revision: 719068
- texlive-mpattern
- texlive-mpattern
- texlive-mpattern
- texlive-mpattern

