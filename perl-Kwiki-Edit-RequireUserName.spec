%define upstream_name	 Kwiki-Edit-RequireUserName
Name:		perl-%{upstream_name}
Version:	0.02
Release:	6

Summary:	Replaces Kwiki::Edit in order to require a user name to edit
License:	GPL
Group:		Development/Perl
Url:		https://metacpan.org/dist/Kwiki-Edit-RequireUserName
Source0:	https://cpan.metacpan.org/authors/id/J/JP/JPEREGR/Kwiki-Edit-RequireUserName-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Kwiki)
BuildArch:	noarch

%description
This plugin helps reduce WikiSpam by requiring that the user have a user name
before editing. The idea is that SpamBots won't take the trouble to do this. Of
course this won't prevent spam created manually.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Kwiki
%{_mandir}/*/*


%changelog
* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.20.0-1mdv2010.0
+ Revision: 403378
- rebuild using %0.02 Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.02-7mdv2009.0
+ Revision: 257438
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.02-6mdv2009.0
+ Revision: 245416
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 0.02-4mdv2008.1
+ Revision: 135856
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.02-4mdv2008.0
+ Revision: 86517
- rebuild


* Thu Aug 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.02-3mdv2007.0
- Rebuild

* Wed May 03 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.02-2mdk
- Fix According to perl Policy
	- BuildRequires
	- Source URL

* Thu Jan 19 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.02-1mdk
- first mandriva release

