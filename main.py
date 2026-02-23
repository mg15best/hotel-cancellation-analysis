from src.data_utils import load_data, clean_data, build_features

RAW_PATH = "data/raw/hotel_bookings.csv"
OUT_PATH = "data/processed/clean_dataset.csv"

def main():
    # 1. Cargar datos
    df = load_data(RAW_PATH)

    # 2. Limpiar datos
    df = clean_data(df)

    # 3. Crear features
    df = build_features(df)

    # 4. Guardar dataset procesado
    df.to_csv(OUT_PATH, index=False)

    print("Pipeline ejecutado correctamente.")
    print(f"Dataset guardado en {OUT_PATH}")

if __name__ == "__main__":
    main()