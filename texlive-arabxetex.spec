# revision 17470
# category Package
# catalog-ctan /macros/xetex/latex/arabxetex
# catalog-date 2010-03-06 08:51:23 +0100
# catalog-license lppl
# catalog-version v1.1.4
Name:		texlive-arabxetex
Version:	v1.1.4
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
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabicdigits.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabicdigits.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-farsi-trans-loc.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-farsi-trans-loc.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-farsi-fullvoc.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-farsi-fullvoc.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-farsi-novoc.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-farsi-novoc.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-farsi-voc.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-farsi-voc.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-fullvoc.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-fullvoc.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-kashmiri-fullvoc.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-kashmiri-fullvoc.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-kashmiri-novoc.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-kashmiri-novoc.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-kashmiri-voc.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-kashmiri-voc.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-kurdish.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-kurdish.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-maghribi-fullvoc.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-maghribi-fullvoc.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-maghribi-novoc.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-maghribi-novoc.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-maghribi-voc.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-maghribi-voc.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-malay-fullvoc.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-malay-fullvoc.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-malay-novoc.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-malay-novoc.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-malay-voc.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-malay-voc.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-novoc.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-novoc.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-pashto-fullvoc.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-pashto-fullvoc.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-pashto-novoc.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-pashto-novoc.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-pashto-voc.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-pashto-voc.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-sindhi-fullvoc.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-sindhi-fullvoc.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-sindhi-novoc.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-sindhi-novoc.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-sindhi-voc.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-sindhi-voc.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-turk-fullvoc.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-turk-fullvoc.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-turk-novoc.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-turk-novoc.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-turk-voc.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-turk-voc.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-uighur.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-uighur.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-urdu-fullvoc.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-urdu-fullvoc.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-urdu-novoc.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-urdu-novoc.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-urdu-voc.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-urdu-voc.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-voc.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-voc.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-farsi-fullvoc.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-farsi-fullvoc.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-farsi-novoc.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-farsi-novoc.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-farsi-voc.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-farsi-voc.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-fullvoc.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-fullvoc.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-kashmiri-fullvoc.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-kashmiri-fullvoc.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-kashmiri-novoc.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-kashmiri-novoc.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-kashmiri-voc.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-kashmiri-voc.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-kurdish.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-kurdish.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-maghribi-fullvoc.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-maghribi-fullvoc.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-maghribi-novoc.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-maghribi-novoc.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-maghribi-voc.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-maghribi-voc.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-malay-fullvoc.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-malay-fullvoc.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-malay-novoc.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-malay-novoc.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-malay-voc.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-malay-voc.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-novoc.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-novoc.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-pashto-fullvoc.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-pashto-fullvoc.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-pashto-novoc.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-pashto-novoc.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-pashto-voc.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-pashto-voc.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-sindhi-fullvoc.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-sindhi-fullvoc.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-sindhi-novoc.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-sindhi-novoc.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-sindhi-voc.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-sindhi-voc.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-turk-fullvoc.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-turk-fullvoc.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-turk-novoc.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-turk-novoc.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-turk-voc.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-turk-voc.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-uighur.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-uighur.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-urdu-fullvoc.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-urdu-fullvoc.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-urdu-novoc.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-urdu-novoc.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-urdu-voc.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-urdu-voc.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-voc.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-voc.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-pashto-trans-loc.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-pashto-trans-loc.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-sindhi-trans-loc.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-sindhi-trans-loc.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-trans-dmg.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-trans-dmg.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-trans-loc.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-trans-loc.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-urdu-trans-loc.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/arabtex-urdu-trans-loc.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/farsidigits.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/farsidigits.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/fixlamalif.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/fixlamalif.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/mirrorpunct.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/arabxetex/mirrorpunct.tec
%{_texmfdistdir}/tex/xelatex/arabxetex/arabxetex.sty
%doc %{_texmfdistdir}/doc/xelatex/arabxetex/README
%doc %{_texmfdistdir}/doc/xelatex/arabxetex/arabxetex.pdf
%doc %{_texmfdistdir}/doc/xelatex/arabxetex/examples/ednotes_example.pdf
%doc %{_texmfdistdir}/doc/xelatex/arabxetex/examples/ednotes_example.tex
%doc %{_texmfdistdir}/doc/xelatex/arabxetex/examples/minimal.tex
#- source
%doc %{_texmfdistdir}/source/xelatex/arabxetex/arabtex-farsi-trans-loc.map
%doc %{_texmfdistdir}/source/xelatex/arabxetex/arabtex-kurdish.maps
%doc %{_texmfdistdir}/source/xelatex/arabxetex/arabtex-pashto-trans-loc.map
%doc %{_texmfdistdir}/source/xelatex/arabxetex/arabtex-sindhi-trans-loc.map
%doc %{_texmfdistdir}/source/xelatex/arabxetex/arabtex-trans-dmg.map
%doc %{_texmfdistdir}/source/xelatex/arabxetex/arabtex-trans-loc.map
%doc %{_texmfdistdir}/source/xelatex/arabxetex/arabtex-uighur.maps
%doc %{_texmfdistdir}/source/xelatex/arabxetex/arabtex-urdu-trans-loc.map
%doc %{_texmfdistdir}/source/xelatex/arabxetex/arabtex.maps
%doc %{_texmfdistdir}/source/xelatex/arabxetex/arabxetex.dtx
%doc %{_texmfdistdir}/source/xelatex/arabxetex/makemaps.pl

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> v1.1.4-2
+ Revision: 749342
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> v1.1.4-1
+ Revision: 717849
- texlive-arabxetex
- texlive-arabxetex
- texlive-arabxetex
- texlive-arabxetex
- texlive-arabxetex

