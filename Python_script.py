
from transformers import AutoModelForCausalLM, AutoTokenizer 
import torch
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import time

filters = [
    ('Total', ''),
    ('Used', '?filter=new_used_eq_used'),
    ('New', '?filter=new_used_eq_new'),
    ('Open-Box', '?filter=new_used_eq_open-box'),
    ('For Parts', '?filter=new_used_eq_for-parts-or-not-working'),
    ('Refurbished', '?filter=new_used_eq_refurbished')
]

url = 'https://www.olx.com.pk/lahore_g4060673/mobile-phones_c1453/q-mobile-in-lahore'

all_data = {}

def scrape_olx(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        element = soup.select_one('#body-wrapper > div._948d9e0a._95d4067f._1e086faf._4122130d > header:nth-child(4) > div > div > div > div._948d9e0a._53c2e845._95d4067f.e1c7c3d4._4122130d > div._948d9e0a.cbff116c.e1c7c3d4 > div._948d9e0a.b2cb83b0._95d4067f > div:nth-child(5) > div:nth-child(2) > div._891e7c21')
        
        if element:
            extracted_text = element.get_text(strip=True)
            
            pattern = re.findall(r'([A-Za-z\s]+)\((\d+)\)', extracted_text)
            
            return {brand.strip(): int(count) for brand, count in pattern}
    
    return {}

for filter_name, filter_query in filters:
    full_url = url + filter_query
    brand_data = scrape_olx(full_url)
    
    all_data[filter_name] = brand_data

all_brands = set()
for data in all_data.values():
    all_brands.update(data.keys())

df = pd.DataFrame(index=sorted(all_brands))

for filter_name, brand_counts in all_data.items():
    df[filter_name] = df.index.map(lambda brand: brand_counts.get(brand, 0))

print(df)


for i in range(1,10):
    print("."*i ,end= " ")
    time.sleep(1)

print("Cleaning Complete\n")

df = df.drop_duplicates()

print(df)

def query_deepseek(prompt):
                                                        
    model_name = "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B"  #recommend to use more paramter model
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=100)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return response

prompt = "Perform analysis on the following DataFrame: {df}"
output = query_deepseek(prompt)
print(output)

