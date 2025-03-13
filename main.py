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


def process_personal_data(filename):
    return pd.read_csv(filename, sep=';')


def create_registries(personal_data):
    dni = personal_data['dni'].astype(str)[0]
    name = personal_data['name'].astype(str)[0]
    last_name = personal_data['last_name'].astype(str)[0]
    phone = personal_data['phone'].astype(str)[0]

    registries = [
        "1720" + year + dni + last_name + ", " + name + ""
                                                        "                      T" + phone + last_name + ", " + name + "                      7200000000000  00000000000000000000" + num_registries + " 00000000000059345 00000000000000000                                                                                                                                                                                                                                                                                                                                ",
        "2720" + year + dni + dni + "         " + last_name + ", " + name + "                      1                         V1                         " + country_code_broker + "1" + isin + "                                              " + company_name + "                                                                                                                                                                                                                     " + country_code_company + "00000000M00000000 " + str(
            company_value).zfill(14) + " 00000000000000A" + str(shares).zfill(
            10) + "00 " + ownership + "00                    "
    ]

    return registries


def generate_720():
    personal_data_file = "personal_data.csv"
    personal_data = process_personal_data(personal_data_file)

    registries_720 = create_registries(personal_data)

    filename = personal_data['dni'].astype(str)[0] + "_" + year + ".720"

    with open(filename, mode='w', encoding='windows-1252') as archivo:
        for registry in registries_720:
            archivo.write(registry + '\n')

    print(f"File {filename} successfully created.")


if __name__ == "__main__":
    generate_720()
