.. SPDX-FileCopyrightText: Copyright 2026 RPA Architecture Team
.. SPDX-License-Identifier: CC-BY-SA-4.0

Architecture Overview
=====================

System Architecture
-------------------

The RPA architecture defines a layered approach to processor management:

.. graphviz::

   digraph architecture {
       rankdir=TB;
       node [shape=box, style=filled, fillcolor=lightblue];

       Application [label="Application Layer"];
       OS [label="Operating System"];
       RPA_API [label="RPA API Layer", fillcolor=lightyellow];
       Hardware [label="Hardware Abstraction", fillcolor=lightgreen];

       Application -> OS;
       OS -> RPA_API;
       RPA_API -> Hardware;
   }

Memory Model
------------

The RPA memory model supports virtual memory with configurable page sizes:

.. list-table:: Supported Page Sizes
   :widths: 25 25 50
   :header-rows: 1

   * - Page Size
     - Levels
     - Virtual Address Bits
   * - 4 KB
     - 3 (Sv39) / 4 (Sv48)
     - 39 / 48
   * - 2 MB
     - 2 (Sv39) / 3 (Sv48)
     - 39 / 48
   * - 1 GB
     - 1 (Sv39) / 2 (Sv48)
     - 39 / 48