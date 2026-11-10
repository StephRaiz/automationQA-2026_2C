# Automatizacion QA

Proyecto de automatizacion de pruebas realizado con python para el curso de talento tech correspondiente al 2do cuatrimestre del 2026.

## Tecnologias usadas
- Python
- Selenium
- Pytest
- Git
- Github

## Instalacion

Instalar dependencias:

    ```python
    pip install selenium
    ```

    ```python
    pip install pytest
    ```

    ```python
    pip install pytest-html
    ```
    
# Reportes

El proyecto genera reportes HTML automáticos utilizando Pytest HTML.


# Ejecutar las pruebas

    
    ```python
    pytest
    ```

# Casos de prueba

Para la ejecucion de las pruebas, se utilizara la pagina www.saucedemo.com

1. **Automatización de Login**

****Validaciones:***

-Navegar a la página de login de saucedemo.com

-Ingresar credenciales válidas (usuario: "standard_user", contraseña: "secret_sauce")

-Validar login exitoso verificando que se haya redirigido a la página de inventario

****Criterios de aceptacion:***

-Login automatizado con espera explícita y validación de /inventory.html y “Products/Swag Labs”.

2. **Navegación y verificación del catálogo**

****Validaciones:***

-Verificar que el título de la página de inventario sea correcto

-Comprobar que existan productos visibles en la página (al menos verificar la presencia de uno)

-Validar que elementos importantes de la interfaz estén presentes (menú, filtros, etc.)

****Criterios de aceptacion:***

-Valida título

-Valida presencia de productos 

-Lista nombre/precio del primero.

3. **Interacción con productos**

****Validaciones:***

-Añadir un producto al carrito haciendo clic en el botón correspondiente

-Verificar que el contador del carrito se incremente correctamente

-Navegar al carrito de compras

-Comprobar que el producto añadido aparezca correctamente en el carrito

****Criterios de aceptacion:***

-Agrega primer producto

-Verifica ítem en carrito.