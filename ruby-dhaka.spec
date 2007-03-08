Summary:	Parsing library for Ruby
Name:		ruby-dhaka
Version:	0.0.4
Release:	1
License:	Ruby's
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/15507/dhaka-%{version}.gem
# Source0-md5:	d02b6c3ba4f44f5144bcbdfc9024e1f9
URL:		http://dhaka.rubyforge.org/
BuildRequires:	rake
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	setup.rb = 3.3.1
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dhaka is a set of tools for generating tokenizers, parsers and
evaluators for context-free grammars. It is written solely in Ruby
with no native extensions and no dependencies.

%prep
%setup -q -c
tar xf %{SOURCE0} -O data.tar.gz | tar xzv-
cp %{_datadir}/setup.rb .

%build
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc --op rdoc lib
rdoc --ri --op ri lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir}}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc
%{ruby_rubylibdir}/*
%{ruby_ridir}/*
