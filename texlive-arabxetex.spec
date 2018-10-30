Name:		texlive-arabxetex
Version:	1.2.1
Release:	2
Summary:	An ArabTeX-like interface for XeLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/xetex/latex/arabxetex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arabxetex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arabxetex.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arabxetex.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
ArabXeTeX provides a convenient ArabTeX-like user-interface for
typesetting languages using the Arabic script in XeLaTeX, with
flexible access to font features. Input in ArabTeX notation can
be set in three different vocalization modes or in roman
transliteration. Direct UTF-8 input is also supported. The
parsing and converting of ArabTeX input to Unicode is done by
means of TECkit mappings. Version 1.0 provides support for
Arabic, Maghribi Arabic, Farsi (Persian), Urdu, Sindhi,
Kashmiri, Ottoman Turkish, Kurdish, Jawi (Malay) and Uighur.
The documentation (not yet complete) covers topics such as
typesetting the Holy Quran, typesetting bidirectional critical
editions (with ednotes), and information on various recommended
OpenType fonts for the Arabic script and for transliterating
Oriental languages.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex
%{_texmfdistdir}/tex/xelatex/arabxetex/arabxetex.sty
%doc %{_texmfdistdir}/doc/xelatex/arabxetex
#- source
%doc %{_texmfdistdir}/source/xelatex/arabxetex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
