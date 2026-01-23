with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Eliminar opción del menú
content = content.replace(
    """\t\t\t<li onclick="showSection('profitability'); closeMobileMenu();">
\t\t\t\t<span class="menu-icon">📊</span> Rentabilidad
\t\t\t</li>\n""", 
    ""
)

# 2. Encontrar y eliminar toda la sección de rentabilidad (desde <!-- Rentabilidad --> hasta <!-- Configuración del Sistema -->)
start_marker = "<!-- Rentabilidad -->"
end_marker = "<!-- Configuración del Sistema -->"

start_index = content.find(start_marker)
end_index = content.find(end_marker)

if start_index != -1 and end_index != -1:
    content = content[:start_index] + content[end_index:]
    print("Sección de Rentabilidad HTML eliminada")
else:
    print("No se encontraron los marcadores")

# 3. Eliminar todas las funciones relacionadas con rentabilidad
# Encontrar desde "// RENTABILIDAD" hasta "// CONFIGURACIÓN DEL SISTEMA"
func_start = content.find("// RENTABILIDAD")
func_end = content.find("// CONFIGURACIÓN DEL SISTEMA")

if func_start != -1 and func_end != -1:
    content = content[:func_start] + content[func_end:]
    print("Funciones de Rentabilidad eliminadas")
else:
    print("No se encontraron las funciones")

# 4. Eliminar variables globales de charts
chart_vars = """\t// Variables globales para charts
\tlet salesByDayChart = null;
\tlet topProductsChart = null;
\tlet profitByMonthChart = null;
\tlet categoryChart = null;

"""
content = content.replace(chart_vars, "")

# 5. Eliminar llamadas a generateProfitabilityReport en otros lugares
content = content.replace("generateProfitabilityReport();", "")
content = content.replace("\t\t\t\tgenerateProfitabilityReport();", "")

# 6. Eliminar referencia en showSection
content = content.replace("if (sectionId === 'profitability') renderProfitability();", "")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Sección de Rentabilidad completamente eliminada")
