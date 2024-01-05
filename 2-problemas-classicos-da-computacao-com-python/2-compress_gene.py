class gene_comprimido:
    def __init__(self, _gene):
        self._comprimir(_gene)
    
    def _comprimir(self, _gene):
        self.bit_string = 1
        for nucleotideo in _gene.upper():
            self.bit_string <<= 2       # desloca 2 bits para esquerda
            if nucleotideo == "A":      # muda os 2 ultimos bits para 00
                self.bit_string |= 0b00 
            elif nucleotideo == "C":    # muda os 2 ultimos bits para 01
                self.bit_string |= 0b01


if __name__ == "__main__":
    from sys import getsizeof
    gene = "TAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATATAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATA" * 100
    
    tamanho_gene_original = (getsizeof(gene))
    print(f"{tamanho_gene_original} bytes")

    tamanho_gene_comprimido = gene_comprimido(gene)
    print(f"{tamanho_gene_comprimido} bytes")

