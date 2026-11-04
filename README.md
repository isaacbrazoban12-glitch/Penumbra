<p align="center"><img src="penumbra_logo.png" width="120" alt="Logo de Penumbra"></p>

# Penumbra

Protector de vista para laptop hecho en Python con tkinter. Oscurece la pantalla por debajo del brillo mínimo y agrega un filtro cálido que reduce la luz azul, ideal para trabajar de noche o en ambientes oscuros sin forzar la vista.

## Qué hace

- Muestra una ventana de controles con dos deslizadores: **Oscuridad** y **Calidez**.
- Pone una capa semitransparente sobre la pantalla que oscurece más de lo que permite el brillo físico del monitor.
- Agrega un tinte cálido (ámbar) para reducir la luz azul.
- Incluye perfiles rápidos: Normal, Lectura, Noche, Muy oscuro y Extremo.
- Guarda tu configuración en un archivo oculto en tu carpeta de usuario (`.penumbra.json`).
- En Windows, los clics atraviesan el filtro para que puedas usar la computadora normalmente con el protector activado.
- Soporta **varios monitores**: pone el filtro en cada pantalla detectada.
- Atajos de teclado: **F11** activa/desactiva el filtro, **Esc** lo apaga por completo.
- Recuerda la posición de la ventana de controles entre sesiones.

## Requisitos

- **Windows recomendado** (solo ahí funciona el modo clic-a-través y el ajuste DPI para pantallas de alta resolución).
- **Python 3.9+** instalado con la opción **"Add python.exe to PATH"** marcada durante la instalación.
- No necesita librerías extras: usa solo la biblioteca estándar (`tkinter`, `json`, `ctypes`).

## Cómo usarlo

1. Descarga o clona este repositorio.
2. Abre una terminal en la carpeta y ejecuta:

   ```bash
   python penumbra.py
   ```

3. Ajusta los deslizadores, activa el filtro y usa los atajos si lo deseas:
   - **F11**: activar / desactivar filtro.
   - **Esc**: apagar filtro por completo.
4. Cierra la ventana de controles para quitar el filtro y guardar la configuración.

## Limitaciones

- En **Mac y Linux** los clics pueden quedar bloqueados por el filtro (el modo clic-a-través solo está implementado para Windows).
- No cambia el brillo real del hardware; simula oscuridad con una capa encima de la pantalla.

## Próximos pasos

- [x] Atajos de teclado (F11, Esc)
- [x] Soporte para varios monitores
- [x] Guardar posición de la ventana
- [x] Ajuste DPI para pantallas de alta resolución (Windows)
- [ ] Ícono en la bandeja del sistema
- [ ] Horario automático de activación
- [ ] Generar archivo `.exe`
- [ ] Versión para Android

## Licencia

MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.
