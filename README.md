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

## Requisitos

- **Windows recomendado** (solo ahí funciona el modo clic-a-través).
- **Python 3.9+** instalado con la opción **"Add python.exe to PATH"** marcada durante la instalación.
- No necesita librerías extras: usa solo la biblioteca estándar (`tkinter`, `json`, `ctypes`).

## Cómo usarlo

1. Descarga o clona este repositorio.
2. Abre una terminal en la carpeta y ejecuta:

   ```bash
   python penumbra.py
   ```

3. Ajusta los deslizadores, activa el filtro y cierra la ventana de controles para quitarlo.

## Limitaciones

- En **Mac y Linux** los clics pueden quedar bloqueados por el filtro (el modo clic-a-través solo está implementado para Windows).
- Cubre únicamente la **pantalla principal**.
- No cambia el brillo real del hardware; simula oscuridad con una capa encima de la pantalla.

## Próximos pasos

- [ ] Ícono en la bandeja del sistema
- [ ] Atajos de teclado
- [ ] Horario automático de activación
- [ ] Soporte para varios monitores
- [ ] Generar archivo `.exe`
- [ ] Versión para Android

## Licencia

MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.
