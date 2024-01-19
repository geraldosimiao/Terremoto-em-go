## START: Set by rpmautospec
## (rpmautospec version 0.3.5)
## RPMAUTOSPEC: autorelease
%define autorelease(e:s:pb:n) %{?-p:0.}%{lua:
    release_number = 6;
    base_release_number = tonumber(rpm.expand("%{?-b*}%{!?-b:1}"));
    print(release_number + base_release_number - 1);
}%{?-e:.%{-e*}}%{?-s:.%{-s*}}%{!?-n:%{?dist}}
## END: Set by rpmautospec

# Generated by go2rpm 1.9.0
%bcond_without check

# https://github.com/geraldosimiao/Terremoto-em-go
%global goipath         github.com/geraldosimiao/Terremoto-em-go
%global commit          d3275484eac37f624f6a7b7b104c9c4020ad87d1

%gometa -f


%global common_description %{expand:
Go program to list earthquakes, above 6 degrees, that occurred in the last 30 days}

%global godocs          README.md

Name:           terremoto-em-go
Version:        0
Release:        %autorelease -p
Summary:        This Go program fetches and displas Earthquake data

License:        MIT
URL:            %{gourl}
Source:         %{gosource}

%description 
The program fetches data from the USGS Earthquake API and displays information about them, including location, magnitude, and time.

%gopkg

%prep
%goprep
%autopatch -p1

%generate_buildrequires
%go_generate_buildrequires

%build
%gobuild -o %{gobuilddir}/bin/Terremoto-em-go %{goipath}

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%doc README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Fri Jan 19 2024 Geraldo Simiao <geraldosimiao@fedoraproject.org> - 0.6
- Testing commit macro new test
* Fri Jan 19 2024 Geraldo Simiao <geraldosimiao@fedoraproject.org> - 0.5
- Added tags macro to spec and redo webhook to push
* Fri Jan 19 2024 Geraldo Simiao <geraldosimiao@fedoraproject.org> - 0.4
- Re-added commit macro to spec and regular changelog
* Fri Jan 19 2024 Geraldo Simiao <geraldosimiao@fedoraproject.org> - 0.3
- Testing github webhook
* Fri Jan 19 2024 Geraldo Simiao <geraldosimiao@fedoraproject.org> - 0.2
- Rebuild with forked sources
* Thu Jan 18 2024 Geraldo Simiao <geraldosimiao@fedoraproject.org> - 0
- Rebuild to new commit
* Wed Oct 25 2023 Geraldo Simiao <geraldosimiao@fedoraproject.org> - 0
- Initial package for fedora
