%define		plugin_name	sqlexplorer

Summary:	Eclipse SQL Explorer
Name:		eclipse-plugin-%{plugin_name}
Version:	3.6.1
Release:	0.1
License:	GPL v2+
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/eclipsesql/sqlexplorer_plugin-3.6.1.zip
# Source0-md5:	78ce98226de75d9b9d67119a6c232d54
URL:		http://eclipsesql.sourceforge.net
BuildRequires:	unzip
Requires:	eclipse >= 3.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugindir	%{_libdir}/eclipse/dropins/%{plugin_name}

%description
Eclipse SQL Explorer.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_plugindir}/eclipse/{features,plugins}

cp -r * $RPM_BUILD_ROOT%{_plugindir}/eclipse

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_plugindir}
%dir %{_plugindir}/eclipse
%dir %{_plugindir}/eclipse/features
%{_plugindir}/eclipse/features/*.jar
%dir %{_plugindir}/eclipse/plugins
%{_plugindir}/eclipse/plugins/net.sourceforge.sqlexplorer*.jar
