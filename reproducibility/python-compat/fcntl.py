"""Small Windows compatibility shim for advisory file locks.

The formalization workflow uses only ``flock`` and the constants below. The
Windows CRT exposes exclusive byte-range locks, which are conservative for
shared-lock callers and preserve mutual exclusion.
"""

from __future__ import annotations

import msvcrt
import os


LOCK_SH = 1
LOCK_EX = 2
LOCK_NB = 4
LOCK_UN = 8


def flock(fd: int, operation: int) -> None:
    current = os.lseek(fd, 0, os.SEEK_CUR)
    try:
        os.lseek(fd, 0, os.SEEK_SET)
        if operation & LOCK_UN:
            mode = msvcrt.LK_UNLCK
        elif operation & LOCK_NB:
            mode = msvcrt.LK_NBLCK
        else:
            mode = msvcrt.LK_LOCK
        msvcrt.locking(fd, mode, 1)
    finally:
        os.lseek(fd, current, os.SEEK_SET)
