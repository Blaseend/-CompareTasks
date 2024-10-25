import re

def extract_customfields(file_path):
    customfields = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

        
        matches = re.findall(
            r'<customfield id="(.*?)">.*?<customfieldname>(.*?)<\/customfieldname>.*?<customfieldvalue.*?>(.*?)<\/customfieldvalue>', 
            content, 
            re.DOTALL
        )

        for match in matches:
            customfield_id = match[0].strip()  # ID customfield
            customfield_name = match[1].strip()  # Имя customfield
            customfield_value = match[2].strip()  # Значение customfield
            customfields[customfield_id] = (customfield_name, customfield_value)

    return customfields

def compare_customfields(file1, file2):

    customfields_file1 = extract_customfields(file1)
    customfields_file2 = extract_customfields(file2)

    
    common_keys = set(customfields_file1.keys()) & set(customfields_file2.keys())

    
    for key in common_keys:
        name1, value1 = customfields_file1[key]
        name2, value2 = customfields_file2[key]

       
        if name1 == name2 and value1 != value2:
            print("\n-------------------------------------")
            print()  
            print(f"Различие в '{name1}':")
            print(f"{file1}: {value1}")
            print(f"{file2}: {value2}")
            print()  
            print("-------------------------------------\n")


file1 = 'vac.txt'
file2 = 'zak.txt'

compare_customfields(file1, file2)
