Summary:	ASCII to International Morse Code converter
Summary(pl.UTF-8):	Konwerter ASCII do Międzynarodowego Kodu Morse'a
Name:		cwtext
Version:	0.96
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://dl.sourceforge.net/cwtext/%{name}-%{version}.tar.gz
# Source0-md5:	d5083cd92d255fba6ff425fbd68aa405
URL:		http://cwtext.sourceforge.net/index.php
BuildRequires:	python
BuildRequires:	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags_ia32	 -fomit-frame-pointer 

%description
ASCII to International Morse Code converter.

%description -l pl.UTF-8
Konwerter ASCII do Międzynarodowego Kodu Morse'a.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%attr(755,root,root) %{_bindir}/*
