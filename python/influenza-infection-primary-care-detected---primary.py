# Chukwuma Iwundu, Clare MacRae, Eleftheria Vasileiou, 2023.

import sys, csv, re

codes = [{"code":"1126371000000114","system":"snomedct"},{"code":"1126431000000117","system":"snomedct"},{"code":"676781000000110","system":"snomedct"},{"code":"676841000000114","system":"snomedct"},{"code":"676901000000115","system":"snomedct"},{"code":"676961000000116","system":"snomedct"},{"code":"677081000000114","system":"snomedct"},{"code":"1126371000000114","system":"snomedct"},{"code":"676781000000110","system":"snomedct"},{"code":"676841000000114","system":"snomedct"},{"code":"676901000000115","system":"snomedct"},{"code":"676961000000116","system":"snomedct"},{"code":"677081000000114","system":"snomedct"},{"code":"XaPIN","system":"ctv3"},{"code":"XaPIO","system":"ctv3"},{"code":"XaPIP","system":"ctv3"},{"code":"XaPIQ","system":"ctv3"},{"code":"XaPIS","system":"ctv3"},{"code":"XaPIN","system":"ctv3"},{"code":"XaPIO","system":"ctv3"},{"code":"XaPIP","system":"ctv3"},{"code":"XaPIQ","system":"ctv3"},{"code":"XaPIS","system":"ctv3"},{"code":"4JU0.00","system":"readv2"},{"code":"4JU2.00","system":"readv2"},{"code":"4JU3.00","system":"readv2"},{"code":"4JU5.00","system":"readv2"},{"code":"4JU0.00","system":"readv2"},{"code":"4JU2.00","system":"readv2"},{"code":"4JU3.00","system":"readv2"},{"code":"4JU5.00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('influenza-infection-primary-care-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["influenza-infection-primary-care-detected---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["influenza-infection-primary-care-detected---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["influenza-infection-primary-care-detected---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
