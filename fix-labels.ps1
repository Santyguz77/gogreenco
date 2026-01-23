$content = Get-Content "index.html" -Raw -Encoding UTF8

# Reemplazar renderOrders label (línea 982-984)
$content = $content -replace "const orderLabel = order\.tableNumber && order\.tableNumber\.includes\('Online'\)\s+\?\s+'🛍️ '\s+\+\s+order\.tableNumber\s+:\s+'📦 Pedido Catálogo Virtual';", "const hasCustomer = order.customerData && order.customerData.name;`n`t`t`tconst orderLabel = hasCustomer ? '🛍️ Pedido de ' + order.customerData.name : '📦 Pedido Catálogo Virtual';"

# Reemplazar completeOrder label (línea 1037-1039)
$content = $content -replace "const orderLabel = order\.tableNumber && order\.tableNumber\.includes\('Online'\)\s+\?\s+order\.tableNumber\s+:\s+'Pedido Catálogo Virtual';", "const hasCustomer = order.customerData && order.customerData.name;`n`t`t`tconst orderLabel = hasCustomer ? 'Pedido de ' + order.customerData.name : 'Pedido Catálogo Virtual';"

Set-Content "index.html" -Value $content -Encoding UTF8
Write-Host "Labels actualizados correctamente"
