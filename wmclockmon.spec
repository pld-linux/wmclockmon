Summary:	Nice dockapp to monitor hour, date and alarms
Summary(pl):	Przyjemny aplet monitoruj±cy godziny, datê i alarmy
Name:		wmclockmon
Version:	0.7.2
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Source0:        http://tnemeth.free.fr/projets/programmes/%{name}-%{version}.tar.gz
# Source0-md5:	6478724a3543390e6f593d2bdd3db42c
Source1:        %{name}.desktop
URL:		http://tnemeth.free.fr/projets/dockapps.html
BuildRequires:	XFree86-devel
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nice digital clock with 7 different styles either in LCD style and LED
style, and that uses locales to display week-day and month names. It
also features the Internet time.

%description -l pl
Przyjemny zegar cyfrowy z 7 ró¿nymi stylami, zarówno LCD jak i LED,
u¿ywajacy locale do wy¶wietlania nazw dni tygodnia i miesiêcy. Posiada
tak¿e opcjê wy¶wietlania czasu internetowego.

%prep
%setup -q 

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}/docklets

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/docklets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog 
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/%{name}
%{_desktopdir}/docklets/*
