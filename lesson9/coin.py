import requests
res_perse_list = []
response = requests.get("https://coinmarketcap.com/")
response_text = response.text
response_parse = response_text.split("<span>")
for parse_element_1 in response_parse:
    if parse_element_1.startswith("$"):
        # print(parse_element_1)
        for parse_element_2 in parse_element_1.split("</span>"):
            if parse_element_2.startswith("$") and parse_element_2[1].isdigit():
                # print(parse_element_2)
                res_perse_list.append(parse_element_2)
bitcoin_exange_rate = res_perse_list[0]
print(bitcoin_exange_rate)


