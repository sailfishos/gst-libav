%define majorminor  1.0
%define gstreamer   gstreamer

Name:           %{gstreamer}%{majorminor}-libav
Version:        1.10.4
Release:        1%{?dist}
Summary:        GStreamer Streaming-media framework plug-in using libav (FFmpeg).
Group:          Libraries/Multimedia
License:        LGPLv2+
URL:            http://gstreamer.freedesktop.org/
Source0:        http://gstreamer.freedesktop.org/src/gst-libav/%{name}-%{version}.tar.gz
Patch0:         0001-Fix-build-by-disabling-gtkdoc-generation-and-git-cal.patch

Requires:       ffmpeg
Requires:       gstreamer1.0
Requires:       gstreamer1.0-plugins-base

BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  orc-devel
BuildRequires:  bzip2-devel
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
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


%package devel-docs
Summary: Development documentation for the libav GStreamer plug-in
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description devel-docs
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

This package contains the development documentation for the libav GStreamer
plug-in.


%prep
%setup -q -n %{name}-%{version}/upstream
%patch0 -p1

%build
./autogen.sh --disable-static --disable-gtkdoc --libdir=/usr/lib/
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
%doc AUTHORS README COPYING
%{_libdir}/gstreamer-1.0/libgstlibav.so

