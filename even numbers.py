numbers = [3,7,52,45,67,8,34,3]
for num in numbers:
  if num>50:
    continue
  if num % 2 == 0:
   print(f"first even number found: {num}")
   break
   