
#
# todo:
# - sgml catalog files?
#

Summary:	Website DTD and XSL stylesheets
Summary(pl):	Website DTD i arkusze XSL
Name:		website
Version:	2.3
Release:	1
License:	Free
Vendor:		Norman Walsh http://nwalsh.com/
Group:		Applications/Publishing/XML
URL:		http://docbook.sourceforge.net/projects/website/index.html
Source0:	http://dl.sourceforge.net/sourceforge/docbook/%{name}-%{version}.tar.gz
# Source0-md5:	4842b6866239b81c0537953b17f82d30
Requires:	libxml2-progs >= 2.4.17-6
BuildRequires:	rpm-build >= 4.0.2-94
BuildRequires:	/usr/bin/xmlcatalog
PreReq:		libxml2
PreReq:		sgml-common
Requires(post,preun):	/usr/bin/install-catalog
Requires(post,preun):	/usr/bin/xmlcatalog
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	website_path	%{_datadir}/sgml/website
%define	dtd_path	%{website_path}/xml-dtd-%{version}
%define	xsl_path	%{website_path}/xsl-stylesheets-%{version}
%define	xmlcat_file	%{website_path}/catalog.xml
%define	sgmlcat_file	%{website_path}/catalog

%description
Website DTD and XSL stylesheets.

%description -l pl
Arkusze Website DTD i XSL.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{dtd_path},%{xsl_path},%{_examplesdir}/%{name}-%{version}}

install *.dtd *.mod $RPM_BUILD_ROOT%{dtd_path}
cp -a xsl/* $RPM_BUILD_ROOT%{xsl_path}
cp -a example/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

xmlcatalog --noout --create --add "public" \
	"-//Norman Walsh//DTD Website V%{version}//EN" \
	"http://docbook.sourceforge.net/release/website/%{version}/website.dtd" \
	$RPM_BUILD_ROOT%{xmlcat_file}

%xmlcat_add_rewrite \
	"http://docbook.sourceforge.net/release/website/%{version}" \
	file://%{dtd_path} \
	$RPM_BUILD_ROOT%{xmlcat_file}

%xmlcat_add_rewrite \
	http://docbook.sourceforge.net/release/website/xsl/%{version} \
	file://%{xsl_path} \
	$RPM_BUILD_ROOT%{xmlcat_file}

%xmlcat_add_rewrite \
	http://docbook.sourceforge.net/release/website/xsl/current \
	file://%{xsl_path} \
	$RPM_BUILD_ROOT%{xmlcat_file}

%clean
rm -rf $RPM_BUILD_ROOT

%post
if ! grep -q %{xmlcat_file} /etc/xml/catalog ; then
	%xmlcat_add %{xmlcat_file}
fi

%preun
if [ "$1" = "0" ] ; then
	%xmlcat_del %{xmlcat_file}
fi

%files
%defattr(644,root,root,755)
%doc ChangeLog README WhatsNew
%{website_path}
%{_examplesdir}/%{name}-%{version}
