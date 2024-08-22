#!/usr/bin/python3
"""
This module provides a method to validate UTF-8 encoding
"""


def validUTF8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding

    Args:
        data: List of integers where each integer represents a byte

    Returns:
        True if data is a valid UTF-8 encoding, else False
    """
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks to check the first few bits of a byte
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    # Iterate over each byte in the data
    for num in data:
        # Convert to the least 8 significant bits
        byte = num & 0xFF

        if num_bytes == 0:
            # Count the number of leading 1's in the first byte
            mask = 1 << 7
            while mask & byte:
                num_bytes += 1
                mask >>= 1

            # 1-byte character (ASCII)
            if num_bytes == 0:
                continue

            # If the number of bytes is more than 4 or 1 (invalid cases)
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Check if the byte starts with 10xxxxxx
            if not (byte & mask1 and not (byte & mask2)):
                return False

        # Decrement the number of bytes we are expecting
        num_bytes -= 1

    # If we finish expecting more bytes, it's invalid
    return num_bytes == 0
