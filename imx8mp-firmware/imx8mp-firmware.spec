#
# spec file for package imx8mp-firmware
#
# Copyright (c) 2022 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

Name:           imx8mp-firmware
Version:        0.1.0
Release:        0
License:        GPL-2.0-only
Group:          System/Boot
Summary:        The U-Boot firmware and devicetree for the i.MX8M-PLUS SoC
Source1:        imx-boot-sd.bin
Source2:        imx8mp-var-dart-dt8mcustomboard.dtb
Source3:        imx8mp-var-dart-dt8mcustomboard-legacy.dtb
Source4:        imx8mp-var-som-symphony.dtb
Provides:       u-boot-loader
ExclusiveArch:  aarch64

%description
This package contains u-boot and device tree binary files built from source for imx8mp.

%prep

%build

%install
install -D -m 0644 %{SOURCE1} %{buildroot}/boot/efi/imx-boot-sd.bin
install -D -m 0644 %{SOURCE2} %{buildroot}/boot/efi/boot/imx8mp-var-dart-dt8mcustomboard.dtb
install -D -m 0644 %{SOURCE3} %{buildroot}/boot/efi/boot/imx8mp-var-dart-dt8mcustomboard-legacy.dtb
install -D -m 0644 %{SOURCE4} %{buildroot}/boot/efi/boot/imx8mp-var-som-symphony.dtb

%files
%defattr(-,root,root,-)
/boot/*

%changelog
