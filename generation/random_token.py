import random

numbers = list(range(1, 6))
random.shuffle(numbers)
random_number = random.choice(numbers)
print(numbers)
for i in range(5):
  context = torch.zeros((1, 1), dtype=torch.long, device=device)
  print(f"{i+1}. {decode(m.generate(context, max_new_tokens= (10 + random_number*5))[0].tolist())}")
