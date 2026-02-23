# Proyecto: Análisis de cancelaciones hoteleras

## Objetivo
Analizar qué variables se asocian con la cancelación de reservas hoteleras y construir un EDA reproducible que permita extraer conclusiones accionables.

## Dataset
- **Nombre**: Hotel Booking Demand Dataset.
- **Origen**: Kaggle.
- **Enlace**: https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand
- **Archivo usado**: `data/raw/hotel_bookings.csv`.

## Preguntas de análisis
1. ¿Qué tipo de hotel presenta mayor tasa de cancelación?
2. ¿Influye la antelación de reserva (`lead_time`) en la probabilidad de cancelar?
3. ¿Existe estacionalidad en las cancelaciones?
4. ¿Qué segmentos de mercado concentran más cancelaciones?

## Estructura del proyecto
- `main.py`: pipeline reproducible (load → clean → features → export → viz).
- `notebooks/eda.ipynb`: EDA narrado y visualizaciones.
- `src/data_utils.py`: carga, limpieza y creación de features.
- `src/utils.py`: validaciones simples (por ejemplo `assert_columns`).
- `src/viz.py`: funciones de visualización reutilizables.
- `src/config.py`: rutas de entrada/salida.
- `data/raw/`: datos originales.
- `data/processed/`: dataset limpio y salidas de pipeline.

## Pipeline reproducible
1. Cargar CSV con validación de esquema mínima.
2. Limpiar datos:
   - Filtrado de outliers de `adr` (0 a 1000).
   - Conversión robusta de `reservation_status_date` a datetime.
   - Imputación de `children` con 0 cuando hay nulos.
3. Crear features:
   - `total_nights`.
   - `total_guests`.
   - `lead_time_category` (short/medium/long).
4. Exportar `data/processed/clean_dataset.csv`.
5. Exportar gráfico `data/processed/cancellation_rate_by_hotel.png`.

## Ejecución
```bash
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

## Hallazgos (EDA)
1. **City Hotel** presenta mayor tasa de cancelación que **Resort Hotel**.
2. Las reservas con mayor `lead_time` muestran mayor probabilidad de cancelación.
3. Existen diferencias de cancelación por mes y por `market_segment`, con segmentos de muestra pequeña que requieren cautela al interpretar porcentajes.

## Estado de entrega
- Notebook ejecutable con rutas relativas.
- Código modular en `src/` con funciones reutilizables.
- Validaciones básicas incluidas en `src/utils.py`.
