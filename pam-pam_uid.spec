%define 	modulename pam_uid
Summary:	PAM module to authenticate users by their UID
Summary(pl.UTF-8):	Moduł PAM uwierzytelniający użytkowników na podstawie UID
Name:		pam-%{modulename}
Version:	0.1
Release:	1
License:	GPL
Group:		Base
Source0:	ftp://ftp.feep.net/pub/software/PAM/%{modulename}/%{modulename}-%{version}.tar.gz
# Source0-md5:	ef191e7eadba6f370952d55d4e2d044c
URL:		http://www.feep.net/PAM/pam_uid/
BuildRequires:	pam-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The pam_uid module provides UID-based authentication to PAM-aware
applications.

%description -l pl.UTF-8
Moduł pam_uid zapewnia aplikacjom korzystającym z PAM uwierzytelnianie
użytkowników na podstawie numeru UID.

%prep
%setup -q -n %{modulename}-%{version}

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -D pam_uid.so.1 $RPM_BUILD_ROOT/%{_lib}/security/pam_uid.so
install -D pam_uid.5 $RPM_BUILD_ROOT%{_mandir}/man5/pam_uid.5

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) /%{_lib}/security/pam_uid.so
%{_mandir}/man*/*
