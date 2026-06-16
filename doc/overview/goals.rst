.. SPDX-FileCopyrightText: Copyright 2026 RPA Architecture Team
.. SPDX-License-Identifier: CC-BY-SA-4.0

Design Goals
============

Primary Goals
-------------

The RPA Specification is designed with the following goals:

Portability
   The API abstracts hardware-specific details, allowing software to run
   on different RISC-V implementations without modification.

Simplicity
   The interface is kept minimal and intuitive, reducing the learning curve
   and potential for implementation errors.

Performance
   The API design enables efficient implementations with minimal overhead
   in both code size and execution time.

Security
   Memory isolation, privilege levels, and secure boot mechanisms are
   fundamental to the design.

Non-Goals
---------

This specification explicitly does **not** address:

* Application-level APIs
* High-level operating system interfaces
* Hardware-specific optimizations