%{?_javapackages_macros:%_javapackages_macros}
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-marshalling
Version:          1.4.1
Release:          1.0%{?dist}
Summary:          JBoss Marshalling
License:          LGPLv2+
URL:              http://www.jboss.org/jbossmarshalling
BuildArch:        noarch

Source0:          https://github.com/jboss-remoting/jboss-marshalling/archive/%{namedversion}.tar.gz

BuildRequires:    maven-local
BuildRequires:    jboss-parent
BuildRequires:    jboss-modules
BuildRequires:    maven-injection-plugin
BuildRequires:    apiviz

%description
JBoss Marshalling is an alternative serialization API that fixes many
of the problems found in the JDK serialization API while remaining
fully compatible with java.io.Serializable and its relatives, and adds
several new tunable parameters and additional features, all of which
are pluggable via factory configuration (externalizers, class/instance
lookup tables, class resolution, and object replacement, to name a
few).

%package javadoc
Summary:          API documentation for %{name}

%description javadoc
This package contains %{summary}.

%prep
%setup -q -n %{name}-%{namedversion}

%pom_remove_plugin :maven-shade-plugin
%pom_disable_module tests
%pom_disable_module osgi

# Compat symlinks.  TODO: remove once jboss-as is rebuilt to use the
# new JAR names.
%mvn_file :{*} %{name}/@1 @1

# Conditionally remove dependency on apiviz
if [ %{?rhel} ]; then
    %pom_remove_plugin :maven-javadoc-plugin
fi

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc COPYING.txt

%files javadoc -f .mfiles-javadoc
%doc COPYING.txt

%changelog
* Tue Oct 08 2013 Marek Goldmann <mgoldman@redhat.com> - 1.4.1-1
- Upstream release 1.4.1.Final

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.13-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 18 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3.13-8
- Remove unneeded BRs
- Use better descriptions
- Update to current packaging guidelines

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.3.13-6
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Mon Oct 15 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3.13-5
- Conditionally remove dependency on apiviz

* Mon Oct 15 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3.13-4
- Remove unneeded BR: gdata-java, maven-surefire-provider-testng, testng

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Apr 20 2012 Marek Goldmann <mgoldman@redhat.com> 1.3.13-2
- Added missing BR

* Sat Apr 20 2012 Marek Goldmann <mgoldman@redhat.com> 1.3.13-1
- Upstream release 1.3.13.GA

* Thu Feb 23 2012 Marek Goldmann <mgoldman@redhat.com> 1.3.9-2
- Relocated jars to _javadir

* Thu Feb 23 2012 Marek Goldmann <mgoldman@redhat.com> 1.3.9-1
- Upstream release 1.3.9.GA
- Changed java devel build requirement to 6 or above, RHBZ#796464

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 07 2011 Marek Goldmann <mgoldman@redhat.com> 1.3.4-1
- Upstream release 1.3.4.GA

* Fri Oct 07 2011 Marek Goldmann <mgoldman@redhat.com> 1.3.0-2
- Cleaned spec file

* Mon Aug 01 2011 Marek Goldmann <mgoldman@redhat.com> 1.3.0-1
- Initial packaging

