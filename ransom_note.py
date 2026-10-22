
def can_construct(ransomNote: str, magazine: str) -> bool:
    """
    Determine whether ransomNote can be constructed
    using characters from magazine.
    """

    char_count = {}

    # Count characters in the magazine
    for char in magazine:
        char_count[char] = char_count.get(char, 0) + 1

    # Check each character needed for the ransom note
    for char in ransomNote:
        if char_count.get(char, 0) == 0:
            return False

        char_count[char] -= 1

    return True
