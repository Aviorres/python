buah = ("pepaya", "mangga", "pisang", "anggur", "bluebarry")
print ("data awal buah adalah", buah)

buah_list = list (buah)
print ("data setelah di convert menjadi", buah_list)

buah_list.append ("kiwi")
print ("setelah di append", buah_list)

index_mangga = buah_list.index("mangga")
buah_list[index_mangga] = "mangga muda"
print ("setelah di update menjadi", buah_list)