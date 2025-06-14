%define majorminor  1.0
%define gstreamer   gstreamer

%global _vpath_srcdir subprojects/gst-libav
%global _vpath_builddir subprojects/gst-libav/_build

Name:           %{gstreamer}%{majorminor}-libav
Version:        1.26.2
Release:        1
Summary:        GStreamer Streaming-media framework plug-in using libav (FFmpeg).
License:        LGPLv2+
URL:            https://github.com/sailfishos/gst-libav
Source0:        %{name}-%{version}.tar.gz
Patch1:         0001-aac-Re-enable-AAC-encoder.patch

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
BuildRequires:  meson
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
%setup -q -n %{name}-%{version}/gstreamer
# Enabling the AAC encoder here would let us drop gst-droid's aac encoder, but we should check
# for licensing limitations (multichannel?)
#%patch1 -p1

%build
%meson \
  -Dpackage-name='SailfishOS GStreamer package plugins (ffmpeg)' \
  -Dpackage-origin='http://sailfishos.org/' \
  -Ddoc=disabled

%meson_build

%install
%meson_install

%files
%license subprojects/gst-libav/COPYING
%doc subprojects/gst-libav/AUTHORS
%{_libdir}/gstreamer-1.0/libgstlibav.so
