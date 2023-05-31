import csv

# Masukkan data csv ke variabel data_file
data_file = 'materials.csv'

# membuat fungsi perform_audit untuk data_file
def perform_audit(data_file):
    # Load data dari CSV file
    with open(data_file, 'r') as file:
        reader = csv.DictReader(file)
        data = list(reader)

    # Audit High quality Material
    print("\nHasil Audit Supplier Material Dengan Kualitas Tinggi:")
    count_quality = 0

    for row in data:
        if row['Quality'] == 'High':
            print(f"Supplier: {row['Supplier']}, Material: {row['Material']}")
            count_quality += 1

    print(f"Jumlah Material: {count_quality}")

    # Audit Medium Material quality
    print("\nHasil Audit Supplier Material Dengan Kualitas Sedang:")
    count_quality = 0

    for row in data:
        if row['Quality'] == 'Medium':
            print(f"Supplier: {row['Supplier']}, Material: {row['Material']}")
            count_quality += 1

    print(f"Jumlah Material: {count_quality}")
            
    # Audit Low Material quality
    print("\nHasil Audit Supplier Material Dengan Kualitas Rendah:")
    count_quality = 0

    for row in data:
        if row['Quality'] == 'Low':
            print(f"Supplier: {row['Supplier']}, Material: {row['Material']}")
            count_quality += 1

    print(f"Jumlah Material: {count_quality}")
            
    # Audit pricing
    print("\nMaterial dengan Harga >= 100:")
    count_quality = 0
    for row in data:
        price = float(row['Price'])
        if price >= 100.0:
            print(f"Material: {row['Material']}, Harga: {price}")
            count_quality += 1

    print(f"Jumlah Material: {count_quality}")

    print("\nMaterial dengan harga < 100:")
    count_quality = 0
    for row in data:
        price = float(row['Price'])
        if price < 100.0:
            print(f"Material: {row['Material']}, Harga: {price}")
            count_quality += 1

    print(f"Jumlah Material: {count_quality}")
    count_quality = 0
    # Audit quantity accuracy
    print("\nJumlah Stok Barang Banyak:")
    for row in data:
        quantity = int(row['Quantity'])
        if quantity >= 5000:
            print(f"Material: {row['Material']}, Jumlah: {quantity}")
            count_quality += 1

    print(f"Jumlah Material: {count_quality}")
    
    print("\nJumlah Stok Barang Sedikit:")
    count_quality = 0
    for row in data:
        quantity = int(row['Quantity'])
        if quantity < 5000:
            print(f"Material: {row['Material']}, Jumlah : {quantity}")
            count_quality += 1

    print(f"Jumlah Material: {count_quality}")
    
    print("\nAudit Berdasarkan Material yang Memiliki Warna:")
    count_quality = 0
    for row in data:
        color = row['Color']
        if color != "Colorless":
            print(f"Material: {row['Material']}, Warna : {color}")
            count_quality += 1

    print(f"Jumlah Material: {count_quality}")

    print("\nAudit Berdasarkan Material yang tidak Memiliki Warna:")
    count_quality = 0
    for row in data:
        color = row['Color']
        if color == "Colorless":
            print(f"Material: {row['Material']}, Warna : {color}")
            count_quality += 1

    print(f"Jumlah Material: {count_quality}")
    
    print("\nAudit Berdasarkan Tipe Material Solid:")
    count_quality = 0
    for row in data:
        type = int(row['Type'])
        if type == 0:
            print(f"Material: {row['Material']}")
            
    print("\nAudit Berdasarkan Tipe Material Liquid:")
    count_quality = 0
    for row in data:
        type = int(row['Type'])
        if type == 2:
            print(f"Material: {row['Material']}")
            count_quality += 1

    print(f"Jumlah Material: {count_quality}")
    
    print("\nAudit Berdasarkan Tipe Material Gas:")
    count_quality = 0
    for row in data:
        type = int(row['Type'])
        if type == 1:
            print(f"Material: {row['Material']}")
            count_quality += 1

    print(f"Jumlah Material: {count_quality}")
    
    print("\nAudit Material dengan Konduktivitas Tinggi:")
    count_quality = 0
    for row in data:
        conductivity = row['Conductivity']
        if conductivity == 'High':
            print(f"Material: {row['Material']}")
            count_quality += 1

    print(f"Jumlah Material: {count_quality}")
            
    print("\nAudit Material dengan Konduktivitas Sedang:")
    count_quality = 0
    for row in data:
        conductivity = row['Conductivity']
        if conductivity == 'Medium':
            print(f"Material: {row['Material']}")
            count_quality += 1
    if not conductivity == 'Medium':
        print(f"Tidak ada material dengan konduktivitas Sedang")

    print(f"Jumlah Material: {count_quality}")
            
    print("\nAudit Material dengan Konduktivitas Rendah:")
    count_quality = 0
    for row in data:
        conductivity = row['Conductivity']
        if conductivity == 'Low':
            print(f"Material: {row['Material']}")
            count_quality += 1

    print(f"Jumlah Material: {count_quality}")
            
            
# Perform the audit
perform_audit(data_file)