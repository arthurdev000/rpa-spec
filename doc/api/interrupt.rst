.. SPDX-FileCopyrightText: Copyright 2026 RPA Architecture Team
.. SPDX-License-Identifier: CC-BY-SA-4.0

Interrupt API
=============

Overview
--------

The Interrupt API provides functions for configuring and managing
processor interrupts.

Interrupt Controller
--------------------

.. plantuml::

   @startuml
   !define RECTANGLE class

   package "Interrupt Controller" {
       rectangle "Priority Encoder" as PE
       rectangle "Interrupt Vector Table" as IVT
       rectangle "Pending Register" as PR
       rectangle "Enable Register" as ER
   }

   package "Sources" {
       rectangle "Timer" as T
       rectangle "External" as E
       rectangle "Software" as S
   }

   T --> PR
   E --> PR
   S --> PR

   PR --> PE
   ER --> PE
   PE --> IVT

   @enduml

Interrupt Priority Levels
-------------------------

.. list-table:: Interrupt Priority Levels
   :widths: 15 25 60
   :header-rows: 1

   * - Level
     - Name
     - Description
   * - 0
     - Machine
     - Highest priority, machine mode
   * - 1
     - Supervisor
     - Supervisor mode interrupts
   * - 2
     - User
     - User mode interrupts
   * - 3
     - Debug
     - Debug interrupts

API Functions
-------------

.. c:function:: int rpa_interrupt_enable(uint32_t irq)

   Enable a specific interrupt.

   :param irq: Interrupt number
   :return: 0 on success, negative error code on failure

.. c:function:: int rpa_interrupt_disable(uint32_t irq)

   Disable a specific interrupt.

   :param irq: Interrupt number
   :return: 0 on success, negative error code on failure