.. SPDX-FileCopyrightText: Copyright 2026 RPA Architecture Team
.. SPDX-License-Identifier: CC-BY-SA-4.0

Memory Management Unit (MMU) API
================================

Overview
--------

The MMU API provides functions for configuring page tables and managing
address translation.

Page Table Entry Format
-----------------------

Each Page Table Entry (PTE) is 64 bits. The following diagram shows the
bit field layout:

.. raw:: latex

   \begin{figure}[h]
   \centering
   \begin{bytefield}[bitwidth=1.1em]{64}
   \bitheader{0,7,8,9,10,11,12,51,52,53,54,55,56,57,58,59,60,61,62,63} \\
   \bitbox{1}{V} & \bitbox{1}{R} & \bitbox{1}{W} &
   \bitbox{1}{X} & \bitbox{1}{U} & \bitbox{1}{G} &
   \bitbox{1}{A} & \bitbox{1}{D} &
   \bitbox{2}{RSW} & \bitbox{26}{PPN[2]} &
   \bitbox{9}{PPN[1]} & \bitbox{9}{PPN[0]} &
   \bitbox{10}{Reserved}
   \end{bytefield}
   \caption{Page Table Entry (PTE) Format for Sv39}
   \end{figure}

For HTML output, see the table below:

.. list-table:: PTE Bit Field Definitions
   :widths: 10 15 75
   :header-rows: 1

   * - Bits
     - Name
     - Description
   * - 0
     - V (Valid)
     - Entry is valid
   * - 1
     - R (Readable)
     - Page is readable
   * - 2
     - W (Writable)
     - Page is writable
   * - 3
     - X (Executable)
     - Page is executable
   * - 4
     - U (User)
     - User mode access
   * - 5
     - G (Global)
     - Global mapping
   * - 6
     - A (Accessed)
     - Accessed flag
   * - 7
     - D (Dirty)
     - Dirty flag
   * - 8-9
     - RSW
     - Reserved for Software
   * - 10-53
     - PPN
     - Physical Page Number
   * - 54-63
     - Reserved
     - Must be zero

Sv39 Virtual Address Format
---------------------------

.. raw:: latex

   \begin{figure}[h]
   \centering
   \begin{bytefield}[bitwidth=1.5em]{39}
   \bitheader{0,8,9,17,18,26,27,38} \\
   \bitbox{9}{VPN[0]} & \bitbox{9}{VPN[1]} &
   \bitbox{9}{VPN[2]} & \bitbox{12}{Offset}
   \end{bytefield}
   \caption{Sv39 Virtual Address Format}
   \end{figure}

.. list-table:: Sv39 Virtual Address Fields
   :widths: 10 20 70
   :header-rows: 1

   * - Bits
     - Field
     - Description
   * - 0-11
     - Offset
     - Page offset (4 KB pages)
   * - 12-20
     - VPN[0]
     - Virtual Page Number level 0
   * - 21-29
     - VPN[1]
     - Virtual Page Number level 1
   * - 30-38
     - VPN[2]
     - Virtual Page Number level 2

API Functions
-------------

.. c:function:: int rpa_mmu_set_page_table(uint64_t root_pa)

   Set the root page table physical address.

   :param root_pa: Physical address of the root page table (must be 4KB aligned)
   :return: 0 on success, negative error code on failure

.. c:function:: int rpa_mmu_map(uint64_t va, uint64_t pa, uint64_t size, uint64_t flags)

   Create a mapping from virtual address to physical address.

   :param va: Virtual address (must be page-aligned)
   :param pa: Physical address (must be page-aligned)
   :param size: Size of the mapping in bytes
   :param flags: Protection flags (RPA_MMU_R, RPA_MMU_W, RPA_MMU_X, RPA_MMU_U)
   :return: 0 on success, negative error code on failure

.. c:function:: int rpa_mmu_unmap(uint64_t va, uint64_t size)

   Remove mappings for the given virtual address range.

   :param va: Starting virtual address
   :param size: Size of the region to unmap
   :return: 0 on success, negative error code on failure