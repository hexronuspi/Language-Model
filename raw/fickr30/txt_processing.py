import os
import zipfile

with zipfile.ZipFile('results.csv.zip', 'r') as zip_ref:
    zip_ref.extractall('/content/')

extracted_path = '/content/'
extracted_files = os.listdir(extracted_path)
print(extracted_files)

import pandas as pd
import numpy as np
from io import StringIO  

df = pd.read_csv('results.csv', delimiter='|')

df.head()

columns_to_delete = ['image_name', ' comment_number']

if all(col in df.columns for col in columns_to_delete):

    df.drop(columns_to_delete, axis=1, inplace=True)

    output_file_path = 'words.csv'
    df.to_csv(output_file_path, index=False)

    print(f"Columns {columns_to_delete} removed. DataFrame saved to {output_file_path}.")
else:
    missing_columns = [col for col in columns_to_delete if col not in df.columns]
    print(f"Columns {missing_columns} not found in the DataFrame.")

words = pd.read_csv('words.csv')

words.columns

old_column_name = ' comment'
new_column_name = 'comment'

if old_column_name in df.columns:

    words.rename(columns={old_column_name: new_column_name}, inplace=True)

    output_file_path = 'wording.csv'
    words.to_csv(output_file_path, index=False)

    print(f"Column '{old_column_name}' renamed to '{new_column_name}'. DataFrame saved to {output_file_path}.")
else:
    print(f"Column '{old_column_name}' not found in the DataFrame.")


trainer = pd.read_csv('wording.csv')

trainer.head()

import csv

csv_file_path = 'wording.csv'
txt_file_path = 'sentences.txt'
with open(csv_file_path, 'r') as csv_file, open(txt_file_path, 'w') as txt_file:
    csv_reader = csv.reader(csv_file)
    header_skipped = False

    for row in csv_reader:
        if not header_skipped:

            header_skipped = True
            continue

        cleaned_row = [cell.lstrip() for cell in row]

        txt_file.write('\n'.join(cleaned_row) + '\n')

  with open('sentences.txt', 'r') as file:
    f_word = file.read()

for line in f_word.splitlines()[:10]:
    print(line)

import string

def process_text(text):
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = text.lower()
    return text

input_file_path = 'sentences.txt'
with open(input_file_path, 'r') as file:
    text_content = file.read()

processed_text = process_text(text_content)

output_file_path = 'g_word.txt'
with open(output_file_path, 'w') as file:
    file.write(processed_text)

print(f'The processed text has been saved to {output_file_path}.')

with open('g_word.txt', 'r') as file:
  g_word=file.read()
for line in g_word.splitlines()[:10]:
  print(line)

len(g_word.split()) # words

num_unique_words = len(set(g_word.split()))

num_unique_words

len(g_word.splitlines()) # sentences

len(g_word) # characters

words = g_word.split()
word_occurrences = {}

for word in words:
    word_occurrences[word] = word_occurrences.get(word, 0) + 1

csv_filename = "unique_word_occurrences.csv"
with open(csv_filename, 'w', newline='') as csvfile:
    fieldnames = ['word', 'occurrences']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for word, count in word_occurrences.items():
        writer.writerow({'word': word, 'occurrences': count})

print(f"\nWord occurrences saved to {csv_filename}")

unique_words = pd.read_csv('unique_word_occurrences.csv')
