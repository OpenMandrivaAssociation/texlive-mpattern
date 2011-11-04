# revision 15878
# category Package
# catalog-ctan /graphics/metapost/contrib/macros/mpattern
# catalog-date 2006-12-15 22:34:26 +0100
# catalog-license pd
# catalog-version undef
Name:		texlive-mpattern
Version:	20061215
Release:	1
Summary:	Patterns in MetaPost
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/mpattern
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mpattern.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mpattern.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A package for defining and using patterns in MetaPost, using
the Pattern Color Space available in PostScript Level 2.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/metapost/mpattern/mpattern.mp
%doc %{_texmfdistdir}/doc/metapost/mpattern/README
%doc %{_texmfdistdir}/doc/metapost/mpattern/README.PL
%doc %{_texmfdistdir}/doc/metapost/mpattern/mpattern_test.pdf
%doc %{_texmfdistdir}/doc/metapost/mpattern/mpattern_test.tex
%doc %{_texmfdistdir}/doc/metapost/mpattern/test.mp
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar metapost doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
