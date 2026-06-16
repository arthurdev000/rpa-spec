.. SPDX-FileCopyrightText: Copyright 2026 RPA Architecture Team
.. SPDX-License-Identifier: CC-BY-SA-4.0

Timer API
=========

Overview
--------

The Timer API provides functions for configuring and using processor timers.

Timer Types
-----------

.. list-table:: Timer Types
   :widths: 20 30 50
   :header-rows: 1

   * - Timer
     - Source
     - Description
   * - mtime
     - Machine Timer
     - Machine mode real-time timer
   * - stime
     - Supervisor Timer
     - Supervisor mode timer
   * - hpm
     - Hardware Performance Monitor
     - Performance counter timers

API Functions
-------------

.. c:function:: int rpa_timer_set_timeout(uint64_t ticks)

   Set the timer to trigger after the specified number of ticks.

   :param ticks: Number of timer ticks until interrupt
   :return: 0 on success, negative error code on failure

.. c:function:: uint64_t rpa_timer_get_value(void)

   Get the current timer value.

   :return: Current timer tick count