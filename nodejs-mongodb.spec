%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name mongodb

%{?nodejs_find_provides_and_requires}

Name:          %{?scl_prefix}nodejs-%{npm_name}
Version:       2.2.24
Release:       1%{?dist}
Summary:       The official MongoDB driver for Node.js
License:       ASL 2.0
URL:           https://github.com/mongodb/node-mongodb-native
Source0:       http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: %{?scl_prefix}nodejs-devel
ExclusiveArch: %{nodejs_arches} noarch
BuildArch:     noarch

%description
The MongoDB Node.js driver is the officially supported node.js driver for MongoDB.
In Spring 2012, MongoDB officially adopted the popular Node MongoDB Native Project.

%prep
%setup -q -n package
%nodejs_fixdep readable-stream
%nodejs_fixdep mongodb-core
%nodejs_fixdep es6-promise

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr index.js lib package.json conf.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

#Cleanup permissions
chmod 644 %{buildroot}%{nodejs_sitelib}/%{npm_name}/*.js
chmod 644 %{buildroot}%{nodejs_sitelib}/%{npm_name}/*.json

%nodejs_symlink_deps

%files
%doc README.md
%license LICENSE THIRD-PARTY-NOTICES
%{nodejs_sitelib}/%{npm_name}

%changelog
* Thu Feb 16 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.2.24-1
- Update
- Add third party notices

* Wed Apr 06 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.1.14-3
- Fix mongodb-core dependency

* Wed Apr 06 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.1.14-2
- Update to new upstream version (fixes RH#1317027)

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.3.19-4.2
- rebuilt

* Tue Mar 04 2014 Tomas Hrcka <thrcka@redhat.com> - 1.3.19-3.2
- Add missing nodejs_symlink_deps macro

* Mon Feb 17 2014 Tomas Hrcka <thrcka@redhat.com> - 1.3.19-3.1
- Change description

* Wed Jan 29 2014 Tomas Hrcka <thrcka@redhat.com> - 1.3.19-2.1
- fix bson dependency

* Mon Dec 16 2013 Tomas Hrcka <thrcka@redhat.com> - 1.3.19-1.1
- Enable scl support
- Invoke provides requires macro

* Thu Oct 03 2013 Troy Dawson <tdawson@redhat.com> - 1.3.19-1
- Updated to version 1.3.19

* Fri Aug 09 2013 Troy Dawson <tdawson@redhat.com> - 1.3.17-1
- Updated to version 1.3.17
- Package using the new Fedora guidelines

* Wed Jul 24 2013 Troy Dawson <tdawson@redhat.com> - 1.3.12-1
- Updated to version 1.3.12

* Wed Apr 17 2013 Haibo Lin <hlin@redhat.com> - 1.2.14-1
- Build under eng-rhel-6 and update to upstream version 1.2.14

* Thu Feb 16 2012 Troy Dawson <tdawson@redhat.com> - 0.9.9.1-1
- Initial build
