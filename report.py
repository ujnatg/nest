# coding=utf-8
import csv
import sys

csv_list = None
iphone = 'iPHONE(safari)'
android = 'ANDROID(Chrome)'
pc_edge = 'PC(msedge)'
pc_chrome = 'PC(chrome)'
mac ='MAC(Safari)'
company = sys.argv[2]
build_id = sys.argv[1]

elf_template_map = (
    ['Login', {iphone: ['US', 'CA', 'GB', 'EU', 'DE']}, {android: ['US', 'CA', 'GB', 'EU', 'DE']}, {pc_chrome: ['US', 'CA', 'GB', 'EU', 'DE']}, {pc_edge: ['US', 'CA', 'GB', 'EU', 'DE']}, {mac: ['US', 'CA', 'GB', 'EU', 'DE']}],
    ['Paypal Express (PPE)', {iphone: ['US', 'GB']}, {android: ['US', 'GB']}, {pc_chrome: ['US', 'GB']}, {pc_edge: ['US', 'GB']}, {mac: ['US', 'GB']}],
    ['ApplePay', {iphone: ['US', 'GB']}, None,  None, None, {mac: ['US', 'GB']}],
    ['Credit Card (CC)', {iphone: ['US', 'CA', 'GB', 'EU', 'DE']}, {android: ['US', 'CA', 'GB', 'EU', 'DE']}, {pc_chrome: ['US', 'CA', 'GB', 'EU', 'DE']}, {pc_edge: ['US', 'CA', 'GB', 'EU', 'DE']}, {mac: ['US', 'CA', 'GB', 'EU', 'DE']}],
    ['Paypal (PP)', {iphone: ['US', 'CA', 'GB', 'EU', 'DE']}, {android: ['US', 'CA', 'GB', 'EU', 'DE']}, {pc_chrome: ['US', 'CA', 'GB', 'EU', 'DE']}, {pc_edge: ['US', 'CA', 'GB', 'EU', 'DE']}, {mac: ['US', 'CA', 'GB', 'EU', 'DE']}],
    ['Afterpay (AP)', {iphone: ['US', 'GB']}, {android: ['US', 'GB']}, {pc_chrome: ['US', 'GB']}, {pc_edge: ['US', 'GB']}, {mac: ['US', 'GB']}],
    ['GC single', {iphone: ['US']}, {android: ['US']}, {pc_chrome: ['US']}, {pc_edge: ['US']}, {mac: ['US']}],
    ['GC multi', {iphone: ['US']}, {android: ['US']}, {pc_chrome: ['US']}, {pc_edge: ['US']}, {mac: ['US']}],
    ['GC + CC', {iphone: ['US']}, {android: ['US']}, {pc_chrome: ['US']}, {pc_edge: ['US']}, {mac: ['US']}],
    ['GC + PP', {iphone: ['US']}, {android: ['US']}, {pc_chrome: ['US']}, {pc_edge: ['US']}, {mac: ['US']}],
    ['GC + AP', {iphone: ['US']}, {android: ['US']}, {pc_chrome: ['US']}, {pc_edge: ['US']}, {mac: ['US']}],
                ['Klarna DDT', {iphone: ['EU', 'DE']}, {android:['EU', 'DE']}, {pc_chrome: ['EU', 'DE']}, {pc_edge: ['EU', 'DE']}, {mac: ['EU', 'DE']}],
               ['Klarna OBT', {iphone: ['EU', 'DE']}, {android:['EU', 'DE']}, {pc_chrome: ['EU', 'DE']}, {pc_edge: ['EU', 'DE']}, {mac: ['EU', 'DE']}])

keys_template_map = (
    ['Login', {iphone: ['US', 'CA']}, {android: ['US', 'CA']}, {pc_chrome: ['US', 'CA']}, {pc_edge: ['US', 'CA']}, {mac: ['US', 'CA']}],
    ['Paypal Express (PPE)', {iphone: ['US']}, {android: ['US']}, {pc_chrome: ['US']}, {pc_edge: ['US']}, {mac: ['US']}],
    ['ApplePay', {iphone: ['US']}, None,  None, None, {mac: ['US']}],
    ['Credit Card (CC)', {iphone: ['US', 'CA']}, {android: ['US', 'CA']}, {pc_chrome: ['US', 'CA']}, {pc_edge: ['US', 'CA']}, {mac: ['US', 'CA']}],
    ['Paypal (PP)', {iphone: ['US', 'CA']}, {android: ['US', 'CA']}, {pc_chrome: ['US', 'CA']}, {pc_edge: ['US', 'CA']}, {mac: ['US', 'CA']}],
    ['Afterpay (AP)', {iphone: ['US']}, {android: ['US']}, {pc_chrome: ['US']}, {pc_edge: ['US']}, {mac: ['US']}],
    ['GC single', {iphone: ['US']}, {android: ['US']}, {pc_chrome: ['US']}, {pc_edge: ['US']}, {mac: ['US']}],
    ['GC multi', {iphone: ['US']}, {android: ['US']}, {pc_chrome: ['US']}, {pc_edge: ['US']}, {mac: ['US']}],
    ['GC + CC', {iphone: ['US']}, {android: ['US']}, {pc_chrome: ['US']}, {pc_edge: ['US']}, {mac: ['US']}],
    ['GC + PP', {iphone: ['US']}, {android: ['US']}, {pc_chrome: ['US']}, {pc_edge: ['US']}, {mac: ['US']}],
    ['GC + AP', {iphone: ['US']}, {android: ['US']}, {pc_chrome: ['US']}, {pc_edge: ['US']}, {mac: ['US']}])

well_template_map = (
    ['Login', {iphone: ['US']}, {android: ['US']}, {pc_chrome: ['US']}, {pc_edge: ['US']}, {mac: ['US']}],
    ['Paypal Express (PPE)', {iphone: ['US']}, {android: ['US']}, {pc_chrome: ['US']}, {pc_edge: ['US']}, {mac: ['US']}],
    ['ApplePay', {iphone: ['US']}, None,  None, None, {mac: ['US']}],
    ['Credit Card (CC)', {iphone: ['US']}, {android: ['US']}, {pc_chrome: ['US']}, {pc_edge: ['US']}, {mac: ['US']}],
    ['Paypal (PP)', {iphone: ['US']}, {android: ['US']}, {pc_chrome: ['US']}, {pc_edge: ['US']}, {mac: ['US']}],
    ['Afterpay (AP)', {iphone: ['US']}, {android: ['US']}, {pc_chrome: ['US']}, {pc_edge: ['US']}, {mac: ['US']}],
    ['GC single', {iphone: ['US']}, {android: ['US']}, {pc_chrome: ['US']}, {pc_edge: ['US']}, {mac: ['US']}],
    ['GC multi', {iphone: ['US']}, {android: ['US']}, {pc_chrome: ['US']}, {pc_edge: ['US']}, {mac: ['US']}],
    ['GC + CC', {iphone: ['US']}, {android: ['US']}, {pc_chrome: ['US']}, {pc_edge: ['US']}, {mac: ['US']}],
    ['GC + PP', {iphone: ['US']}, {android: ['US']}, {pc_chrome: ['US']}, {pc_edge: ['US']}, {mac: ['US']}],
    ['GC + AP', {iphone: ['US']}, {android: ['US']}, {pc_chrome: ['US']}, {pc_edge: ['US']}, {mac: ['US']}])

template_line = '{},{},{},{},{},{}'

def load_results():
    with open('/tmp/report.txt', mode='r') as csv_file:
        global csv_list
        csv_list = [{k: v for k, v in row.items()}
            for row in csv.DictReader(csv_file, skipinitialspace=True)]


def s(test, platform_country):
    if platform_country == None:
        return ''
    result = ''
    for country in list(platform_country.values())[0]:
        country_result = ''
        for line in csv_list:
            if company in line["Company"]:
                if line["Test Name"] == test:
                    if line["Country"] == country:
                        if line["Platform"] == list(platform_country.keys())[0]:
                            if line["Build ID"] == 'BUILD_ID:'+build_id:
                                country_result = line["Order ID"]
                                result = result + country +':'+ country_result+' '
        if country_result == '':
            result = result + country +':'+ 'NA'+' '
   
    return result.strip()

def report():
    load_results()
    template_map = []
    if company == "ELF":
        template_map = elf_template_map
    elif company == "KEYS":
        template_map = keys_template_map
    elif company == "W3LL":
        template_map = well_template_map
        
        
    # Print headers
    row_h = template_map[0];
    print(template_line.format('Testcase', list(row_h[1].keys())[0], list(row_h[2].keys())[0], list(row_h[3].keys())[0], list(row_h[4].keys())[0], list(row_h[5].keys())[0]))
    for row in template_map:
        print (template_line.format(row[0], s(row[0], row[1]), s(row[0], row[2]), s(row[0], row[3]), s(row[0], row[4]), s(row[0], row[5])))



if __name__ == '__main__':
    report()
