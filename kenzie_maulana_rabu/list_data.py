mobil = ["BMW", "Audi", "Mercedes Benz", "pagani", "bugatti", "ferrari", "chevrolet"]
stand = ["KILLER QUEEN", "D4C", "THE HAND", "STAR PLATINUM", "THE WORLD", "MADE IN HEAVEN", "GOLDEN EXPERIENCE", "TUSK ACT 4", "WONDER OF U", "SOFT AND WET"]

print ("list mobil adalah", mobil)
print ("nama nama stand di jba", stand)

mobil.append ("toyota")
print ("list setelah ditambah append adalah", mobil)

stand.extend (["ONE REPUBLIC", "BRAIN HEAD"])
print ("list setelah ditambah extend adalah", stand)

stand.insert (4, "KING CRIMSON")
print ("list setelah ditambah insert adalah", stand)

mobil.remove ("toyota")
print ("list setelah di remove menjadi", mobil)

last_item = mobil.pop()
print ("list setelah ditambah pop menjadi", mobil)

last_item = mobil.pop(2)
print ("data setelah pop dan memilih tempat menjadi", mobil)

stand.sort()
print ("data setelah di urutkan menjadi", stand)

print ("banyaknya data stand adalah", len(stand))