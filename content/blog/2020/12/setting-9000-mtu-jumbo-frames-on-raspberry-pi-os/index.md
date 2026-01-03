---
nid: 3064
title: "Setting 9000 MTU (Jumbo Frames) on Raspberry Pi OS"
slug: "setting-9000-mtu-jumbo-frames-on-raspberry-pi-os"
date: 2020-12-23T16:44:19+00:00
drupal:
  nid: 3064
  path: /blog/2020/setting-9000-mtu-jumbo-frames-on-raspberry-pi-os
  body_format: markdown
  redirects: []
tags:
  - benchmarking
  - compile
  - jumbo frame
  - kernel
  - mtu
  - networking
  - pi os
  - raspberry pi
---

Raspberry Pi OS isn't really built to be a server OS; the main goals are stability and support for educational content. But that doesn't mean people like me don't use and abuse it to do just about anything.

In my case, I've been doing a lot of network testing lately—first with an [Intel I340-T4 PCIe interface for 4.15 Gbps of networking](https://www.youtube.com/watch?v=a-0PeuPINiQ), and more recently (yesterday, in fact!) with a [Rosewill 2.5 GbE PCIe NIC](https://pipci.jeffgeerling.com/cards_network/rosewill-rc20001-25gbe.html).

And since the Pi's BCM2711 SoC is somewhat limited, it can't seem to pump through many Gbps of bandwidth without hitting IRQ limits, and queueing up packets.

In the case of the 2.5G NIC, I was seeing it max out around 1.92 Gpbs, and I just wouldn't accept that (at least not for a raw benchmark). Running `atop`, I noticed that during testing, the IRQ interrupts would max out at 99% on one CPU core—and it seems like it may be impossible to distribute interrupts across all four cores on the BCM2711.

Anyways, one quick way to get around that issue is to use 'jumbo frames'. By default, in Pi OS, the MTU ("Maximum Transmission Unit") is set to `1500`, which is pretty standard on networking devices.

But for some situations, it's nice to increase it (especially if you need to ship larger volumes of data around a network, in fewer but larger packets).

## Increasing MTU on my Mac

On my Mac, changing the MTU is as simple as going into a network interface's Advanced Hardware setting, and overriding in a dropdown menu:

{{< figure src="./increase-mtu-mac-standard-jumbo-frame-9000.png" alt="Increase MTU to 9000 Jumbo Frame on macOS Network Interface System Preferences" width="668" height="565" class="insert-image" >}}

## Increasing MTU on a Pi

But on the Raspberry Pi, there are two ways to do it, depending on the network interface you're using:

  - For external interfaces, like the 2.5 GbE card I was testing, you can run `sudo ip link set dev eth1 mtu 9000` (where `eth1` is the external interface).
  - For the Pi's internal gigabit interface, you can't do that—instead, you have to patch the Pi OS kernel and recompile it.

The only way to increase the MTU on the internal gigabit interface on a Pi 4 model B, Compute Module 4, or Pi 400, is to recompile the kernel.

I have a handy guide for recompiling the kernel here: [Raspberry Pi Cross Compile Environment VM](https://github.com/geerlingguy/raspberry-pi-pcie-devices/tree/master/extras/cross-compile).

The one thing you have to do in addition is, right after cloning the Pi kernel git repository, apply this patch to the kernel:

```
diff --git a/drivers/net/ethernet/broadcom/genet/bcmgenet.c b/drivers/net/ethernet/broadcom/genet/bcmgenet.c
index 62051e353278..81e3da888d1a 100644
--- a/drivers/net/ethernet/broadcom/genet/bcmgenet.c
+++ b/drivers/net/ethernet/broadcom/genet/bcmgenet.c
@@ -52,7 +52,7 @@
 #define GENET_Q16_TX_BD_CNT	\
 	(TOTAL_DESC - priv->hw_params->tx_queues * priv->hw_params->tx_bds_per_q)
 
-#define RX_BUF_LENGTH		2048
+#define RX_BUF_LENGTH		10240
 #define SKB_ALIGNMENT		32
 
 /* Tx/Rx DMA register offset, skip 256 descriptors */
diff --git a/include/linux/if_vlan.h b/include/linux/if_vlan.h
index 41a518336673..28cac902cb77 100644
--- a/include/linux/if_vlan.h
+++ b/include/linux/if_vlan.h
@@ -22,8 +22,8 @@
 /*
  * According to 802.3ac, the packet can be 4 bytes longer. --Klika Jan
  */
-#define VLAN_ETH_DATA_LEN	1500	/* Max. octets in payload	 */
-#define VLAN_ETH_FRAME_LEN	1518	/* Max. octets in frame sans FCS */
+#define VLAN_ETH_DATA_LEN	9000	/* Max. octets in payload	 */
+#define VLAN_ETH_FRAME_LEN	9018	/* Max. octets in frame sans FCS */
 
 #define VLAN_MAX_DEPTH	8		/* Max. number of nested VLAN tags parsed */
 
diff --git a/include/uapi/linux/if_ether.h b/include/uapi/linux/if_ether.h
index d6de2b167448..78a12dd0e542 100644
--- a/include/uapi/linux/if_ether.h
+++ b/include/uapi/linux/if_ether.h
@@ -33,8 +33,8 @@
 #define ETH_TLEN	2		/* Octets in ethernet type field */
 #define ETH_HLEN	14		/* Total octets in header.	 */
 #define ETH_ZLEN	60		/* Min. octets in frame sans FCS */
-#define ETH_DATA_LEN	1500		/* Max. octets in payload	 */
-#define ETH_FRAME_LEN	1514		/* Max. octets in frame sans FCS */
+#define ETH_DATA_LEN	9000		/* Max. octets in payload	 */
+#define ETH_FRAME_LEN	9014		/* Max. octets in frame sans FCS */
 #define ETH_FCS_LEN	4		/* Octets in the FCS		 */
 
 #define ETH_MIN_MTU	68		/* Min IPv4 MTU per RFC791	*/
```

Thanks to user [waryishe on the Pi Forums](https://www.raspberrypi.org/forums/viewtopic.php?p=1665692&sid=587e1d5ea3a34c19ba8b0b1addce0ac4#p1665692) for the suggestion.

Recompile the kernel with that patch, copy over the new kernel and modules to the Pi, and reboot, and you should have MTU 9000 available.

I don't really recommend you do this unless you (a) want to juice your benchmark numbers, or (b) know what you're doing and need to do this.
