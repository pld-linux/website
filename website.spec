Summary:	Website DTD and XSL stylesheets
Summary(pl):	Website DTD i arkusze XSL
Name:		website
%define		ver 1
%define		subver 9
Version:	%{ver}.%{subver}
Release:	1
License:	free (Copyright Norman Walsh)
Vendor:		Norman Walsh http://nwalsh.com/
Group:		Applications/Publishing/XML
Group(de):	Applikationen/Publizieren/XML
Group(es):	Aplicaciones/Editoración/XML
Group(pl):	Aplikacje/Publikowanie/XML
Group(pt_BR):	Aplicações/Editoração/XML
Source0:	http://www.nwalsh.com/website/%{version}}/ws%{ver}%{subver}.zip
URL:		http://www.nwalsh.com/website/
Requires:	sgml-common >= 0.5
Requires:	docbook-dtd412-xml
Requires:	docbook-style-xsl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch
AutoReqProv:	0

%description
Website DTD and XSL stylesheets.

%description -l pl
Arkusze Website DTD i XSL.

%prep
%setup -q -c -T
unzip -qa %{SOURCE0}
mv -f website/* .
rmdir website

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/sgml/website/xsl-stylesheets-%{version}
install -d $RPM_BUILD_ROOT%{_datadir}/sgml/website/xml-dtd-%{version}

perl -pi -e 's@"/.*docbook.xsl"@"/usr/share/sgml/docbook/xsl-stylesheets/xhtml/docbook.xsl"@' xsl/website.xsl

install *.dtd *.mod $RPM_BUILD_ROOT%{_datadir}/sgml/website/xml-dtd-%{version}
install xsl/* $RPM_BUILD_ROOT%{_datadir}/sgml/website/xsl-stylesheets-%{version}

gzip -9nf COPYRIGHT ChangeLog README WhatsNew

%clean
rm -rf $RPM_BUILD_ROOT

%post
ln -sf xsl-stylesheets-%{version} %{_datadir}/sgml/website/xsl-stylesheets

%preun
rm -f %{_datadir}/sgml/website/xsl-stylesheets

%files
%defattr(644,root,root,755)
%doc example *.gz
%{_datadir}/sgml/*
