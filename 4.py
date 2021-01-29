"""

System operacyjny Windows korzysta z systemu dwójkowego dlatego 1GB = 1024 MB, 1MB = 1024KB, 1KB = 1024B,
natomiast producenci dysków twardych którzy używają systemu dziesiętnego, zaokrąglają te wartości dla wygody,
dlatego np; 1GB = 1000MB, 1MB = 1000KB, 1KB = 1000B.

"""

def hardDiskCopacity(value):
    gigabytesToBytes = value * 1000*1000*1000 #zamiana na bajty (wartość) * 1000(kilobajtów) * 1000(megabajtów) * 1000(gigabajtów)

    actualValue = gigabytesToBytes/1024/1024/1024
    return round(actualValue,2) #zaokrąglenie do 2 miejsca po przecinku

value=int(input("Podaj wartość dysku twardego w GB (gigabajtach): "))

print("Rzeczywista pojemność twojego dyku wynosi:",hardDiskCopacity(value), "GB")
