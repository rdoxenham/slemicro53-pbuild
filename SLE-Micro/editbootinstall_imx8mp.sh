#!/bin/bash
set -euxo pipefail

diskname=$1
devname="$2"
loopname="${devname%*p?}"
loopdev=/dev/${loopname#/dev/mapper/*}

#==========================================
# Installing All-in-one U-Boot/SPL
#------------------------------------------
echo "Installing All-in-one U-Boot/SPL for i.MX8MP..."
if ! dd if=boot/efi/imx-boot-sd.bin of=$loopdev bs=1K seek=32; then
	echo "Couldn't install SPL on $loopdev"
	exit 1
fi
