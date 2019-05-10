%define majorminor  1.0
%define gstreamer   gstreamer

Name:           %{gstreamer}%{majorminor}-libav
Version:        1.16.1
Release:        1%{?dist}
Summary:        GStreamer Streaming-media framework plug-in using libav (FFmpeg).
Group:          Libraries/Multimedia
License:        LGPLv2+
URL:            http://gstreamer.freedesktop.org/
Source0:        http://gstreamer.freedesktop.org/src/gst-libav/%{name}-%{version}.tar.gz
Patch1:         0001-Fix-build-by-disabling-gtkdoc-generation-and-git-cal.patch
Patch2:         0002-aac-Reenable-AAC-encoder.patch

Requires:       gstreamer1.0
Requires:       gstreamer1.0-plugins-base

%define sonamever %(echo %{version} | cut -d '+' -f 1)

BuildRequires:  pkgconfig(gstreamer-1.0) >= %{sonamever}
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0) >= %{sonamever}
BuildRequires:  pkgconfig(orc-0.4)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  bzip2-devel
%ifarch %{ix86} x86_64
BuildRequires:  yasm
%endif

%description
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related. Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plug-ins.

This plugin contains the libav (formerly FFmpeg) codecs, containing codecs for most popular
multimedia formats.


%prep
%setup -q -n %{name}-%{version}/upstream
%patch1 -p1
# Enabling the AAC encoder here would let us drop gst-droid's aac encoder, but we should check 
# for licensing limitations (multichannel?)
#%patch2 -p1

%build
./autogen.sh --disable-static --disable-gtk-doc --libdir=/usr/lib/ --with-system-libav
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
%doc AUTHORS README COPYING
%{_libdir}/gstreamer-1.0/libgstlibav.so


