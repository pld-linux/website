
#
# todo:
# - catalog files...
#

Summary:	Website DTD and XSL stylesheets
Summary(pl):	Website DTD i arkusze XSL
Name:		website
Version:	2.2
Release:	1
License:	Free
Vendor:		Norman Walsh http://nwalsh.com/
Group:		Applications/Publishing/XML
URL:		http://docbook.sourceforge.net/projects/website/index.html
Source0:	http://telia.dl.sourceforge.net/sourceforge/docbook/%{name}-%{version}.tar.gz
Requires:	libxml2-progs >= 2.4.17-6
BuildRequires:	rpm-build >= 4.0.2-94
BuildRequires:	/usr/bin/xmlcatalog
PreReq:		libxml2
PreReq:		sgml-common
Requires(post,preun):   /usr/bin/install-catalog
Requires(post,preun):   /usr/bin/xmlcatalog
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define website_path	%{_datadir}/sgml/website
%define dtd_path		%{website_path}/xml-dtd-%{version}
%define xsl_path		%{website_path}/xsl-stylesheets-%{version}
%define	xmlcat_file		%{dtd_path}/catalog.xml
%define	sgmlcat_file	%{dtd_path}/catalog

%description
Website DTD and XSL stylesheets.

%description -l pl
Arkusze Website DTD i XSL.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d
$RPM_BUILD_ROOT{%{dtd_path},%{xsl_path},%{_examplesdir}/%{name}-%{version}}

install *.dtd *.mod $RPM_BUILD_ROOT%{dtd_path}
install xsl/* $RPM_BUILD_ROOT%{xsl_path}
cp -a example/* %{_examplesdir}/%{name}-%{version}


%clean
rm -rf $RPM_BUILD_ROOT

%post
ln -sf xsl-stylesheets-%{version} %{_datadir}/sgml/website/xsl-stylesheets

%preun
rm -f %{_datadir}/sgml/website/xsl-stylesheets

%files
%defattr(644,root,root,755)
%doc ChangeLog README WhatsNew
%{website_path}
