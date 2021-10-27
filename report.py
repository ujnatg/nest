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

template_map = (
    ['Paypal Express checkout', {iphone: ['US', 'GB']}, {android: ['US', 'GB']}, {pc_chrome: ['US', 'GB']}, {pc_edge: ['US', 'GB']}, {mac: ['US', 'GB']}],
    ['ApplePay checkout', {iphone: ['US', 'GB']}, None,  None, None, {mac: ['US', 'GB']}],
    ['Guest checkout', {iphone: ['US', 'CA', 'GB', 'EU', 'DE']}, {android: ['US', 'CA', 'GB', 'EU', 'DE']}, {pc_chrome: ['US', 'CA', 'GB', 'EU', 'DE']}, {pc_edge: ['US', 'CA', 'GB', 'EU', 'DE']}, {mac: ['US', 'CA', 'GB', 'EU', 'DE']}],
    ['Paypal checkout', {iphone: ['US', 'CA', 'GB', 'EU', 'DE']}, {android: ['US', 'CA', 'GB', 'EU', 'DE']}, {pc_chrome: ['US', 'CA', 'GB', 'EU', 'DE']}, {pc_edge: ['US', 'CA', 'GB', 'EU', 'DE']}, {mac: ['US', 'CA', 'GB', 'EU', 'DE']}],
    ['Afterpay checkout', {iphone: ['US', 'GB']}, {android: ['US', 'GB']}, {pc_chrome: ['US', 'GB']}, {pc_edge: ['US', 'GB']}, {mac: ['US', 'GB']}],
    ['Giftcard checkout', {iphone: ['US']}, {android: ['US']}, {pc_chrome: ['US']}, {pc_edge: ['US']}, {mac: ['US']}],
    ['Giftcard(multi) checkout', {iphone: ['US']}, {android: ['US']}, {pc_chrome: ['US']}, {pc_edge: ['US']}, {mac: ['US']}],
    ['Giftcard + CreditCard checkout', {iphone: ['US']}, {android: ['US']}, {pc_chrome: ['US']}, {pc_edge: ['US']}, {mac: ['US']}],
    ['Giftcard and Paypal checkout', {iphone: ['US']}, {android: ['US']}, {pc_chrome: ['US']}, {pc_edge: ['US']}, {mac: ['US']}],
    ['Giftcard and Afterpay checkout', {iphone: ['US']}, {android: ['US']}, {pc_chrome: ['US']}, {pc_edge: ['US']}, {mac: ['US']}],
                ['Klarna checkout DDT', {iphone: ['EU', 'DE']}, {android:['EU', 'DE']}, {pc_chrome: ['EU', 'DE']}, {pc_edge: ['EU', 'DE']}, {mac: ['EU', 'DE']}],
               ['Klarna checkout OBT', {iphone: ['EU', 'DE']}, {android:['EU', 'DE']}, {pc_chrome: ['EU', 'DE']}, {pc_edge: ['EU', 'DE']}, {mac: ['EU', 'DE']}])

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

    # Print headers
    row_h = template_map[0];
    print(template_line.format('Testcase', list(row_h[1].keys())[0], list(row_h[2].keys())[0], list(row_h[3].keys())[0], list(row_h[4].keys())[0], list(row_h[5].keys())[0]))
    for row in template_map:
        print (template_line.format(row[0], s(row[0], row[1]), s(row[0], row[2]), s(row[0], row[3]), s(row[0], row[4]), s(row[0], row[5])))



if __name__ == '__main__':
    report()
