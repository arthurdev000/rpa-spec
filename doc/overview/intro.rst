.. SPDX-FileCopyrightText: Copyright 2026 RPA Architecture Team
.. SPDX-License-Identifier: CC-BY-SA-4.0

Introduction
============

This document defines the RPA (RISC-V Processor Architecture) Specification.

Purpose
-------

The RPA Specification provides a standardized interface for:

* Processor configuration and control
* Memory management unit (MMU) programming
* Interrupt and exception handling
* Performance monitoring

Scope
-----

This specification covers:

.. list-table:: Coverage Areas
   :widths: 20 80
   :header-rows: 1

   * - Area
     - Description
   * - MMU
     - Page table structure, TLB management, address translation
   * - Interrupts
     - Interrupt controller interface, priority handling
   * - Timers
     - Timer configuration and event scheduling
   * - Debug
     - Debug interface and breakpoint management

References
----------

.. [RISCV] RISC-V Instruction Set Manual, Volume II: Privileged Architecture