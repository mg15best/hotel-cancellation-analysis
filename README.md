```markdown
## Estructura del proyecto

Se crean los siguientes directorios y archivos:

```bash
mkdir data
mkdir data/raw
mkdir data/processed
mkdir notebooks
mkdir src
ni main.py
ni README.md
ni requirements.txt
```

- `data/raw`: Datos originales sin procesar.
- `data/processed`: Datos procesados y listos para análisis.
- `notebooks`: Notebooks para exploración y visualización.
- `src`: Código fuente del proyecto.
- `main.py`: Script principal.
- `README.md`: Documentación del proyecto.
- `requirements.txt`: Dependencias del proyecto.
```

# Proyecto: Análisis de Cancelaciones Hotel

## Objetivo
Analizar factores asociados a la cancelación de reservas hoteleras utilizando un enfoque de exploración de datos, limpieza estructurada y generación de nuevas variables.

## Dataset
Hotel Booking Dataset (Kaggle)

El dataset contiene información sobre reservas hoteleras, incluyendo tipo de hotel, antelación de la reserva (lead_time), segmento de mercado, ADR y estado de cancelación.

## Pipeline del Proyecto
El proyecto sigue un flujo reproducible definido en `main.py`:

1. Carga de datos desde `data/raw/`
2. Limpieza de datos:
   - Eliminación de outliers evidentes en ADR (ADR < 0 y ADR > 1000)
   - Conversión de `reservation_status_date` a formato datetime
3. Creación de nuevas features:
   - `total_nights` = `stays_in_weekend_nights` + `stays_in_week_nights`
   - `total_guests` = `adults` + `children` + `babies` (con `children` imputado a 0 si falta)
   - `lead_time_category` (short/medium/long)
4. Exportación del dataset limpio a `data/processed/clean_dataset.csv`

Para ejecutar el pipeline completo:

```bash
python main.py