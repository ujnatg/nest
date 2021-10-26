# coding=utf-8
import csv
import sys

csv_list = None
iphone = 'iPHONE(safari)'
android = 'ANDROID(Chrome)'
pc_edge = 'PC(edge)'
pc_chrome = 'PC(chrome)'
mac ='MAC(Safari)'
company = sys.argv[2]
build_id = sys.argv[1]

template_map = (
    ['Paypal Express checkout', {iphone: ['US', 'GB']}, {android: ['US', 'GB']}, {pc_chrome: ['US', 'GB']}, {pc_edge: ['US', 'GB']}, {mac: ['US', 'GB']}],
    ['ApplePay checkout', {iphone: ['US', 'UK']}, {android: ['US', 'UK']},  {pc_chrome: ['US', 'GB']}, {pc_edge: ['US', 'GB']}, {mac: ['US', 'UK']}],
    ['Guest checkout', {iphone: ['US', 'CA', 'UK', 'EU', 'DE']}, {android: ['US', 'CA', 'UK', 'EU', 'DE']}, {pc_chrome: ['US', 'CA', 'UK', 'EU', 'DE']}, {pc_edge: ['US', 'CA', 'UK', 'EU', 'DE']}, {mac: ['US', 'CA', 'UK', 'EU', 'DE']}],
    ['Paypal checkout', {iphone: ['US', 'CA', 'UK', 'EU', 'DE']}, {android: ['US', 'CA', 'UK', 'EU', 'DE']}, {pc_chrome: ['US', 'CA', 'UK', 'EU', 'DE']}, {pc_edge: ['US', 'CA', 'UK', 'EU', 'DE']}, {mac: ['US', 'CA', 'UK', 'EU', 'DE']}],
    ['Afterpay checkout', {iphone: ['US', 'UK']}, {android: ['US', 'UK']}, {pc_chrome: ['US', 'UK']}, {pc_edge: ['US', 'UK']}, {mac: ['US', 'UK']}],
    ['Giftcard checkout', {iphone: ['US']}, {android: ['US']}, {pc_chrome: ['US']}, {pc_edge: ['US']}, {mac: ['US']}],
    ['Giftcard(multi) checkout', {iphone: ['US']}, {android: ['US']}, {pc_chrome: ['US']}, {pc_edge: ['US']}, {mac: ['US']}],
    ['Giftcard + CreditCard checkout', {iphone: ['US']}, {android: ['US']}, {pc_chrome: ['US']}, {pc_edge: ['US']}, {mac: ['US']}],
    ['Giftcard and Paypal checkout', {iphone: ['US']}, {android: ['US']}, {pc_chrome: ['US']}, {pc_edge: ['US']}, {mac: ['US']}],
    ['Giftcard and Afterpay checkout', {iphone: ['US']}, {android: ['US']}, {pc_chrome: ['US']}, {pc_edge: ['US']}, {mac: ['US']}],
                ['Klarna checkout DDT', {iphone: ['EU', 'DE']}, {android:['EU', 'DE']}, {pc_chome: ['EU', 'DE']}, {pc_edge: ['EU', 'DE']}, {mac: ['EU', 'DE']}],
               ['Klarna checkout OBT', {iphone: ['EU', 'DE']}, {android:['EU', 'DE']}, {pc_chome: ['EU', 'DE']}, {pc_edge: ['EU', 'DE']}, {mac: ['EU', 'DE']}])

template_line = '{},{},{},{},{},{}'

def load_results():
    with open('/tmp/report.txt', mode='r') as csv_file:
        global csv_list
        csv_list = [{k: v for k, v in row.items()}
            for row in csv.DictReader(csv_file, skipinitialspace=True)]


def s(test, platform_country):
    result = ''
    for country in list(platform_country.values())[0]:
        for line in csv_list:
            if company in line["Company"]:
                if line["Test Name"] == test:
                    if line["Country"] == country:
                        if line["Platform"] == list(platform_country.keys())[0]:
                            if line["Build ID"] == 'BUILD_ID:'+build_id:
                                result = result + country +':'+ line["Order ID"]+' '
    if result == '':
        return 'NA'
    else:
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
