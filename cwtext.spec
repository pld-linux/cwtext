Summary:	ASCII to International Morse Code converter
Summary(pl):	Konwerter ASCII do Miêdzynarodowego Kodu Morse'a
Name:		cwtext
Version:	0.93
Release:	1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/cwtext/%{name}-%{version}.tar.gz
URL:		http://cwtext.sourceforge.net/
BuildRequires:	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ASCII to International Morse Code converter.

%description -l pl
Konwerter ASCII do Miêdzynarodowego Kodu Morse'a.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install PREFIX=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%attr(755,root,root) %{_bindir}/*
