# SPDX-FileCopyrightText: Copyright 2026 RPA Architecture Team
# SPDX-License-Identifier: Apache-2.0

/**
 * @file rpa_mmu.h
 * @brief RPA Memory Management Unit API
 */

#ifndef RPA_MMU_H
#define RPA_MMU_H

#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif

/**
 * @defgroup MMU_FLAGS MMU Protection Flags
 * @{
 */
#define RPA_MMU_R    (1U << 0)  /**< Readable */
#define RPA_MMU_W    (1U << 1)  /**< Writable */
#define RPA_MMU_X    (1U << 2)  /**< Executable */
#define RPA_MMU_U    (1U << 3)  /**< User accessible */
/** @} */

/**
 * @brief Set the root page table physical address.
 *
 * @param root_pa Physical address of the root page table (must be 4KB aligned).
 * @return 0 on success, negative error code on failure.
 */
int rpa_mmu_set_page_table(uint64_t root_pa);

/**
 * @brief Create a memory mapping.
 *
 * @param va Virtual address (must be page-aligned).
 * @param pa Physical address (must be page-aligned).
 * @param size Size of the mapping in bytes.
 * @param flags Protection flags (RPA_MMU_R, RPA_MMU_W, RPA_MMU_X, RPA_MMU_U).
 * @return 0 on success, negative error code on failure.
 */
int rpa_mmu_map(uint64_t va, uint64_t pa, uint64_t size, uint64_t flags);

/**
 * @brief Remove memory mappings.
 *
 * @param va Starting virtual address.
 * @param size Size of the region to unmap.
 * @return 0 on success, negative error code on failure.
 */
int rpa_mmu_unmap(uint64_t va, uint64_t size);

#ifdef __cplusplus
}
#endif

#endif /* RPA_MMU_H */