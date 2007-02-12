Summary:	Nice dockapp to monitor hour, date and alarms
Summary(pl.UTF-8):	Przyjemny aplet monitorujący godziny, datę i alarmy
Name:		wmclockmon
Version:	0.8.1
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://tnemeth.free.fr/projets/programmes/%{name}-%{version}.tar.gz
# Source0-md5:	e5569e326f5542a181dd123836f652ee
Source1:	%{name}.desktop
URL:		http://tnemeth.free.fr/projets/dockapps.html
BuildRequires:	XFree86-devel
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nice digital clock with 7 different styles either in LCD style and LED
style, and that uses locales to display week-day and month names. It
also features the Internet time.

%description -l pl.UTF-8
Przyjemny zegar cyfrowy z 7 różnymi stylami, zarówno LCD jak i LED,
używajacy locale do wyświetlania nazw dni tygodnia i miesięcy. Posiada
także opcję wyświetlania czasu internetowego.

%prep
%setup -q 

%build
cp -f %{_datadir}/automake/config.sub .
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
%doc AUTHORS BUGS ChangeLog THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/%{name}
%{_desktopdir}/docklets/*
