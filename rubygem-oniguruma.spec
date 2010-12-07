%define	oname	oniguruma

Summary:	Ruby bindings for the Onigurama regexp library
Name:		rubygem-%{oname}
Version:	1.1.0
Release:	%mkrel 2
License:	BSD
Group:		Development/Ruby
URL:		http://%{oname}.rubyforge.org/
Source0:	http://gems.rubyforge.org/gems/%{oname}-%{version}.gem
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	ruby-RubyGems ruby-devel onig-devel

%description
Ruby bindings to the Oniguruma[http://www.geocities.jp/kosako3/oniguruma/]
regular expression library.

%prep

%build

%install
rm -rf %{buildroot}
gem install --local --install-dir %{buildroot}/%{ruby_gemdir} --force %{SOURCE0}

rm -rf %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/ext

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/gems/%{oname}-%{version}
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec

