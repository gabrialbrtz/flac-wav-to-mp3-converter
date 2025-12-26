# FLAC/WAV to MP3 Converter

Una aplicación GUI en Python para convertir archivos de audio FLAC y WAV a formato MP3 con alta calidad (320kbps por defecto).

## Características

- **Interfaz gráfica intuitiva** con tkinter
- **Conversión por lotes** de múltiples archivos
- **Preservación de estructura de carpetas** opcional
- **Normalización de audio** configurable
- **Configuración personalizable** vía archivo YAML
- **Procesamiento paralelo** para mayor velocidad
- **Barra de progreso** en tiempo real

## Requisitos

### Dependencias del Sistema
- **Python 3.7+**
- **FFmpeg** (debe estar en PATH)

### Dependencias de Python
- `PyYAML` - Para configuración
- `tkinter` - Para la interfaz gráfica (incluido en Python)
- `pathlib` - Para manejo de rutas (incluido en Python 3.4+)

## Instalación

1. **Clona el repositorio**
   ```bash
   git clone https://github.com/tu-usuario/flac-wav-to-mp3-converter.git
   cd flac-wav-to-mp3-converter
   ```

2. **Instala FFmpeg**
   
   **macOS (con Homebrew):**
   ```bash
   brew install ffmpeg
   ```
   
   **Ubuntu/Debian:**
   ```bash
   sudo apt update
   sudo apt install ffmpeg
   ```
   
   **Windows:**
   - Descarga desde [ffmpeg.org](https://ffmpeg.org/download.html)
   - Añade el directorio bin al PATH

3. **Instala dependencias de Python**
   ```bash
   pip install PyYAML
   ```

## Uso

### Ejecución de la aplicación
```bash
python main.py
```

### Interfaz gráfica
1. **Selecciona carpeta de entrada** - Carpeta que contiene archivos FLAC/WAV
2. **Selecciona carpeta de salida** - Donde se guardarán los archivos MP3
3. **Haz clic en "▶ Convertir"** para iniciar el proceso

## ⚙️ Configuración

Edita el archivo `config.yaml` para personalizar la conversión:

```yaml
# Configuración de audio
bitrate: 320          # Bitrate en kbps (128, 192, 256, 320)
sample_rate: 44100    # Frecuencia de muestreo en Hz
channels: 2           # Número de canales (1=mono, 2=estéreo)

# Opciones de procesamiento
normalize: true               # Normalizar audio con loudnorm
preserve_structure: true     # Mantener estructura de carpetas
```

## Estructura del Proyecto

```
flac-wav-to-mp3-converter/
├── main.py              # Punto de entrada principal
├── config.yaml          # Archivo de configuración
├── README.md            # Documentación
└── src/
    ├── gui.py           # Interfaz gráfica
    ├── converter.py     # Lógica de conversión
    └── __pycache__/     # Cache de Python
```

## Características Técnicas

- **Formatos soportados:** FLAC, WAV → MP3
- **Codec:** libmp3lame (alta calidad)
- **Procesamiento:** Multiproceso para mejor rendimiento
- **Metadatos:** Preservación automática de metadatos
- **Normalización:** loudnorm de FFmpeg para audio consistente

## Solución de Problemas

### Error "yaml no funciona"
```bash
pip install PyYAML
```

### Error "ffmpeg command not found"
- Asegúrate de que FFmpeg esté instalado y en el PATH
- Verifica con: `ffmpeg -version`

### La aplicación no se abre
- Verifica que Python 3.7+ esté instalado
- Ejecuta desde el directorio del proyecto


## Autor

Desarrollado con ❤️ para DJs.
