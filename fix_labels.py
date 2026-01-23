import re

# Leer el archivo
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Reemplazar renderOrders label
old_pattern1 = r"const orderLabel = order\.tableNumber && order\.tableNumber\.includes\('Online'\)\s+\?\s+'🛍️\s+'\s+\+\s+order\.tableNumber\s+:\s+'📦\s+Pedido\s+Catálogo\s+Virtual';"
new_pattern1 = "const hasCustomer = order.customerData && order.customerData.name;\n\t\t\tconst orderLabel = hasCustomer \n\t\t\t\t? '🛍️ Pedido de ' + order.customerData.name \n\t\t\t\t: '📦 Pedido Catálogo Virtual';"
content = re.sub(old_pattern1, new_pattern1, content)

# Reemplazar completeOrder label
old_pattern2 = r"const orderLabel = order\.tableNumber && order\.tableNumber\.includes\('Online'\)\s+\?\s+order\.tableNumber\s+:\s+'Pedido\s+Catálogo\s+Virtual';"
new_pattern2 = "const hasCustomer = order.customerData && order.customerData.name;\n\t\tconst orderLabel = hasCustomer \n\t\t\t? 'Pedido de ' + order.customerData.name \n\t\t\t: 'Pedido Catálogo Virtual';"
content = re.sub(old_pattern2, new_pattern2, content)

# Guardar
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Labels actualizados correctamente")
