## 🍔 Rappi Listas — Ordering System Using Linked Lists in Python  
**Python | Linked Lists | File Handling | Console/GUI | Data Structures**

---

## 🚀 Overview  
**Rappi Listas** es un prototipo inspirado en apps tipo *Rappi*, diseñado para demostrar el uso de **listas enlazadas** y modelado de datos en Python.  
Permite que compradores y restaurantes interactúen con menús, carritos y archivos reales de inventario.

---

## 🎯 Objetivo del Proyecto  
El proyecto busca fortalecer habilidades en:

- Diseño e implementación de **listas enlazadas personalizadas**  
- Abstracción mediante **TADs propios**  
- Simulación de un marketplace de restaurantes  
- Sincronización **archivos ↔ listas**  
- Manejo de **roles y flujos completos de usuario**

---

## 🧩 Functional Requirements  

### 📁 1. Carga y actualización de archivos  
- Cada restaurante tiene su propio archivo (`.txt`, `.csv`, etc.)  
- Al iniciar: los datos se cargan en listas enlazadas  
- Al cerrar: las listas actualizan sus archivos  
- Permite una manipulación ordenada y eficiente del inventario  

---

### 👤 2. Roles del Sistema  

#### 🔸 **Rol: Restaurante**  
El restaurante puede:  
- ➕ Agregar productos  
- ✏️ Modificar precios o cantidades  
- ❌ Eliminar productos  
- 📈 Ver productos vendidos, cantidades y ganancias  
- 🔄 Actualizar inventario al final del día  

#### 🛒 **Rol: Comprador**  
El comprador puede:  
- 👀 Ver menú de un restaurante  
- 🔍 Buscar un producto en todos los restaurantes  
- ➕ Agregar productos al carrito  
- ❌ Eliminar productos del carrito  
- 💳 Realizar compras  
- ⚠️ Recibir alertas por falta de stock  

---

### 🔁 3. Sistema siempre activo  
Después de cada sesión:  
> *“¿Desea ingresar como restaurante o como cliente?”*

- El sistema solo finaliza manualmente  
- Inventarios y carritos se actualizan dinámicamente  
- Productos agotados → no se pueden pedir  

---
