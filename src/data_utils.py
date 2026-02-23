import pandas as pd

def load_data(path):
    return pd.read_csv(path)


def clean_data(df):
    # eliminar outliers de ADR
    df = df[(df["adr"] >= 0) & (df["adr"] <= 1000)].copy()

    # convertir fecha
    df["reservation_status_date"] = pd.to_datetime(df["reservation_status_date"])

    return df


def build_features(df):

    df["total_nights"] = (
        df["stays_in_weekend_nights"] +
        df["stays_in_week_nights"]
    )

    df["total_guests"] = (
        df["adults"] +
        df["children"].fillna(0) +
        df["babies"]
    )

    def categorize_lead_time(x):
        if x <= 30:
            return "short"
        elif x <= 90:
            return "medium"
        else:
            return "long"

    df["lead_time_category"] = df["lead_time"].apply(categorize_lead_time)

    return df