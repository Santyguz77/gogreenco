with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Reemplazar las líneas 2032-2035 con el código correcto
lines[2031] = '\t\t\t// Abrir en nueva pestaña\n'
lines[2032] = '\t\t\tconst pdfBlob = doc.output(\'blob\');\n'
lines.insert(2033, '\t\t\tconst pdfUrl = URL.createObjectURL(pdfBlob);\n')
lines.insert(2034, '\t\t\twindow.open(pdfUrl, \'_blank\');\n')
lines.insert(2035, '\t\t} catch (error) {\n')
lines.insert(2036, '\t\t\tconsole.error(\'Error generando PDF:\', error);\n')
lines.insert(2037, '\t\t\t// No detener el flujo si falla el PDF\n')
lines[2038] = '\t\t}\n'
lines[2039] = '\t}\n'

with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Archivo corregido exitosamente")
