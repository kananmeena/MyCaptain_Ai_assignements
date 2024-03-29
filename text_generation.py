# -*- coding: utf-8 -*-
"""text generation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/178Vd8ETrjvM7CrtcNijGn7Qc0tuFh5O3
"""

!pip install transformers

from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

model = GPT2LMHeadModel.from_pretrained('gpt2')
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

prompt_text = "Once upon a time"
input_ids = tokenizer.encode(prompt_text, return_tensors='pt')

max_length = 100
output = model.generate(input_ids, max_length=max_length, num_return_sequences=1, pad_token_id=tokenizer.eos_token_id)

generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

print(generated_text)