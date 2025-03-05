import pandas as pd

year = "2024"
num_registries = "24"
country_code_broker = "NL"
isin = "ES0178430E18"
company_name = "TELEFONICA"
country_code_company = "ES"
company_value = "5000"
shares = "100"
total_value = "5000"
ownership = "100"

archivo_csv = "personal_data.csv"
datos = pd.read_csv(archivo_csv, sep=';')

dni = datos['dni'].astype(str)[0]
name = datos['name'].astype(str)[0]
last_name = datos['last_name'].astype(str)[0]
phone = datos['phone'].astype(str)[0]

lineas = [
    "1720" + year + dni + last_name + ", " + name + "                      T" + phone + last_name + ", " + name + "                      7200000000000  00000000000000000000" + num_registries + " 00000000000059345 00000000000000000                                                                                                                                                                                                                                                                                                                                ",
    "2720" + year + dni + dni + "         " + last_name + ", " + name + "                      1                         V1                         " + country_code_broker + "1" + isin + "                                              " + company_name + "                                                                                                                                                                                                                     " + country_code_company + "00000000M00000000 " + str(
        company_value).zfill(14) + " 00000000000000A" + str(shares).zfill(
        10) + "00 " + ownership + "00                    "
]

filename = dni+"_"+year+".720"

with open(filename, mode='w', encoding='windows-1252') as archivo:
    for linea in lineas:
        archivo.write(linea + '\n')

if __name__ == "__main__":
    print(f"File {filename} successfully created.")
