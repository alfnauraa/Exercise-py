m = input(f"whats m? ")
a = input(f"whats a? ")

if m < a or m > a:
    print("m is not equal to a")
else:
    print("m is equal to a")


def main():
    nama_file = input("file name: ").lower().strip()
    titik = nama_file.rfind(".")

    if titik == -1:
        hasil = "application/octet-stream"
    else:
        ekstensi = nama_file[titik + 1 :]
        if ekstensi == "gif":
            hasil = "image/gif"
        elif ekstensi == "jpg" or ekstensi == "jpeg":
            hasil = "image/jpeg"
        elif ekstensi == "png":
            hasil = "image/png"
        elif ekstensi == "pdf":
            hasil = "application/pdf"
        elif ekstensi == "txt":
            hasil = "text/plain"
        elif ekstensi == "zip":
           hasil = "application/zip"
        else:
            hasil = "application/octet-stream"
    print(hasil)
main()

