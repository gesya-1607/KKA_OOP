class AkunBank:
    def __init__(self, saldo):
        self._saldo = saldo #Private attribute

    def cek_saldo(self):
        return self._saldo
    
    def setor(self, jumlah):
        if jumlah > 0:
            self._saldo += jumlah
        else:
            print("Jumlah setor harus positif.")
    
    def tarik(self, jumlah):
        if 0 < jumlah <= self._saldo:
            self._saldo -= jumlah
        else:
            print("Jumlah tarik atau saldo tidak mencukupi.")

rekening = AkunBank(1000)
rekening.setor(500)
rekening.tarik(500)
#print(rekening.cek_saldo()) # Output: 1500
# print(rekening._saldo)  # Tpi akan EROR Tidak bisa akses langsung