with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Encontrar la línea "// VER DETALLE DE MESA" (línea 1396)
for i, line in enumerate(lines):
    if '// VER DETALLE DE MESA' in line:
        # Insertar la función viewInvoice antes
        new_function = [
            '\n',
            '\tfunction viewInvoice(transactionId) {\n',
            '\t\tconst transaction = AppState.transactions.find(t => t.id === transactionId);\n',
            '\t\tif (!transaction || !transaction.invoicePDF) {\n',
            '\t\t\talert(\'Factura no disponible\');\n',
            '\t\t\treturn;\n',
            '\t\t}\n',
            '\t\t\n',
            '\t\t// Abrir PDF en nueva pestaña\n',
            '\t\twindow.open(transaction.invoicePDF, \'_blank\');\n',
            '\t}\n',
            '\n'
        ]
        # Insertar en la posición correcta
        for j, new_line in enumerate(new_function):
            lines.insert(i + j, new_line)
        break

with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Función viewInvoice agregada correctamente")
