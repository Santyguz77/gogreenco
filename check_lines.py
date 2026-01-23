with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Buscar la línea problemática
for i, line in enumerate(lines):
    if i >= 2029 and i <= 2037:
        print(f"{i+1}: {repr(line)}")
