#Superclass
class Pendidikan():
    
    def __init__(self, nama_sekolah, alamat_sekolah ) :
        self.nama_sekolah = nama_sekolah
        self.alamat_sekolah = alamat_sekolah

#Subclass Pendidikan Sekolah Dasar dan Sekolah Menengah Atas
class Pendidikan_SekolahDasar(Pendidikan):
    pass

class Pendidikan_SekolahMenengahAtas(Pendidikan):
    pass

SDNBUNDAMARIA = Pendidikan_SekolahDasar("SDBUNDAMARIA", "DEPOK")
SMAMARDIYUANA = Pendidikan_SekolahMenengahAtas("SMAMARDIYUANA", "DEPOK")

#Output
print(SDNBUNDAMARIA.nama_sekolah, SDNBUNDAMARIA.alamat_sekolah)
print(SMAMARDIYUANA.nama_sekolah, SMAMARDIYUANA.alamat_sekolah)
