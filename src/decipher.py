# Class to decipher Vigenere ciphers
# For English language and limited to alphabet characters
# all sopaces are removed

from typing import Optional
import string
import itertools


class VigenereDecipher:

    alphabet_position = dict(zip(string.ascii_uppercase, range(0, 26)))
    positions = dict(zip(range(0, 26), string.ascii_uppercase))

    def __init__(
        self, cipher: str, key: Optional[str] = None, key_length: Optional[int] = None
    ):
        if key:
            self.key = [self.alphabet_position[letter] for letter in key]
        else:
            self.key = None
        self.key_length = key_length
        self.cipher = cipher.replace(" ", "")
        self.cipher_representation = [
            self.alphabet_position[letter] for letter in self.cipher
        ]

    def decipher(self):
        """
        Decipher Vigenere cipher with or without the key/keylength

        Returns:
            str: Deciphered cipher.
        """
        if self.key:
            return self._decipher_with_key(self.key)
        elif self.key_length:
            key = self.guess_key(self.key_length)
            print(key)
            return self._decipher_with_key(key)
        # Estimate key legnth and then run previous methods

    def _decipher_with_key(self, key: str) -> str:
        clear_text = ""
        for index, letter in enumerate(self.cipher_represenation):
            deciphered_position = (letter - key[index % len(key)]) % 26
            clear_text += self.positions[deciphered_position]
        return clear_text

    def guess_key(self, keylength: int) -> str:
        """
        Make single guess for key based on frequency

        Args:
            keylength (int): Length of the key

        Returns:
            str: Possible key
        """
        key = ""
        for i in range(keylength):
            key += self._frequencies_letter(i, keylength)
        return key

    def _frequencies_letter(self, position: int, keylength: int) -> str:
        frequency = dict()
        for i in range(position, len(self.cipher), keylength):
            if frequency.get(self.cipher_representation[i]):
                frequency[self.cipher_representation[i]] += 1
                continue
            frequency[self.cipher_representation[i]] = 1
        ordered_frequency = list(frequency.items())
        del frequency
        ordered_frequency.sort(key=lambda freq: freq[1], reverse=True)
        return [self.positions[(i[0] - 4) % 26] for i in ordered_frequency][0]
