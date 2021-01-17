# Class to decipher Vigenere ciphers
# For English language and limited to alphabet characters
# all sopaces are removed

from typing import Optional
import string
import math
import itertools
import functools


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
        Decipher Vigenere cipher with key

        Returns:
            str: Deciphered cipher.
        """
        if self.key:
            return self._decipher_with_key(self.key)

    def _decipher_with_key(self, key: str) -> str:
        clear_text = ""
        for index, letter in enumerate(self.cipher_representation):
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

    def estimate_key_length(self) -> str:
        # Use Kasiski's test to estimate the length of key
        trigrams = dict()
        for i in range(0, len(self.cipher) - 3):
            if trigrams.get(self.cipher[i : i + 3]):
                trigrams[self.cipher[i : i + 3]].append(i)
                continue
            trigrams[self.cipher[i : i + 3]] = [i]
        ordered_trigrams = list(trigrams.items())
        ordered_trigrams.sort(key=lambda trigram: len(trigram[1]), reverse=True)
        top_trigram = ordered_trigrams[0]
        distances = []
        for i in range(len(top_trigram[1]) - 1):
            distances.append(abs(top_trigram[1][i] - top_trigram[1][i + 1]))
        gcd = functools.reduce(lambda x, y: math.gcd(x, y), distances)
        return f"The keylength divides {gcd}"
