# listing 1.10
class CompressedGenere:
    def __init__(self, gene: str) -> None:
        self._compress(gene)

        
# listing 1.11



class CompressedGenere:
    def __init__(self, gene: str) -> None:
        self._compress(gene)

    def _compress(self, gene: str) -> None:
        # Implementation of gene compression goes here
        pass

if __name__ == "__main__":
    gene = "ATBGGBTA"
    compressed_genere = CompressedGenere(gene)


    
    
    
    
# listing 1.12


class CompressedGenere:
    def __init__(self, gene: str) -> None:
        self._compress(gene)

    def _compress(self, gene: str) -> None:
        self.bit_string: int = 1  # start with sentinel
        for nucleotide in gene.upper():
            self.bit_string <<= 2  # shift left two bits
            if nucleotide == "A":  # change last two bits to 00
                self.bit_string |= 0b00
            elif nucleotide == "B":  # change last two bits to 01
                self.bit_string |= 0b01
            elif nucleotide == "G":  # change last two bits to 10
                self.bit_string |= 0b10
            elif nucleotide == "T":  # change last two bits to 11
                self.bit_string |= 0b11
            else:
                raise ValueError("Invalid Nucleotide: {}".format(nucleotide))

if __name__ == "__main__":
    gene = "ATBGGBTA"
    compressed_genere = CompressedGenere(gene)

# listing 1.13

class CompressedGenere:
    def __init__(self, gene: str) -> None:
        self._compress(gene)

    def _compress(self, gene: str) -> None:
        self.bit_string: int = 1  # start with sentinel
        for nucleotide in gene.upper():
            self.bit_string <<= 2  # shift left two bits
            if nucleotide == "A":  # change last two bits to 00
                self.bit_string |= 0b00
            elif nucleotide == "B":  # change last two bits to 01
                self.bit_string |= 0b01
            elif nucleotide == "G":  # change last two bits to 10
                self.bit_string |= 0b10
            elif nucleotide == "T":  # change last two bits to 11
                self.bit_string |= 0b11
            else:
                raise ValueError("Invalid Nucleotide: {}".format(nucleotide))

    def decompress(self) -> str:
        gene: str = ""
        for i in range(0, self.bit_string.bit_length() - 1, 2):  # - 1 to exclude sentinel
            bits: int = self.bit_string >> i & 0b11  # get just 2 relevant bits
            if bits == 0b00:  # A
                gene += "A"
            elif bits == 0b01:  # B
                gene += "B"
            elif bits == 0b10:  # G
                gene += "G"
            elif bits == 0b11:  # T
                gene += "T"
            else:
                raise ValueError("Invalid bits: {}".format(bits))
        return gene[::-1]  # [::-1] reverses string by slicing backward

    def __str__(self) -> str:  # string representation for pretty printing
        return self.decompress()
if __name__ == "__main__":
  gene = "ATBGGBTA"
  compressed_genere = CompressedGenere(gene)
  print(compressed_genere)






# listing 1.14
if __name__ == "__main__":
    from sys import getsizeof
original = "TAGGGATTAABBGTTATATATATATAGBBATGGATBGATTATATAGGGATTAABBGTTATATATATATAGB"
compressed = CompressedGenere(original)  # compress
print("original is {} bytes".format(getsizeof(original)))
print("compressed is {} bytes".format(getsizeof(compressed.bit_string)))
print(compressed.decompress())
print("original and decompressed are the same:", original == compressed.decompress())

print(compressed)  # decompress
print("original and decompressed are the same: {}".format(original ==
     compressed.decompress()))
