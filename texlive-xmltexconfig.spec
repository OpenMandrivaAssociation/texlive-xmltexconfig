Name:		texlive-xmltexconfig
Version:	45845
Release:	2
Summary:	configuration files for xmltex and pdfxmltex
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/xmltexconfig
License:	
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xmltexconfig.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description

%prep
%autosetup -p1 -c

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/xmltex/xmltexconfig

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
