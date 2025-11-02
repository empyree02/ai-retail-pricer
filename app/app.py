import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/..")
import streamlit as st
import pandas as pd
csv_file_path=os.path.join(os.path.dirname(__file__),'..','Classeur1.csv')
from src.model import generate_price_table
from src.price_calculator import calculate_retail_price

st.set_page_config(page_title="AI Retail Pricer", page_icon="💰")

st.title("💰 AI Retail Pricer")
st.write("Easily compute your optimal retail price based on your costs and margins.")

st.sidebar.header("Configuration")
logistics_rate = st.sidebar.slider("Logistics (%)", 0, 30, 10) / 100
it_rate = st.sidebar.slider("IT (%)", 0, 30, 5) / 100
personnel_rate = st.sidebar.slider("Personnel (%)", 0, 30, 10) / 100
profit_margin = st.sidebar.slider("Profit Margin (%)", 0, 50, 20) / 100

st.subheader("Single Product Calculator")
purchase_price = st.number_input("Enter purchase price ($):", min_value=0.0, step=1.0)
if purchase_price > 0:
    retail_price = calculate_retail_price(purchase_price, logistics_rate, it_rate, personnel_rate, profit_margin)
    st.success(f"Suggested retail price: **${retail_price}**")

st.subheader("Batch Calculation from CSV")
uploaded = st.file_uploader("Upload CSV with columns: product,purchase_price")
if uploaded:
    df = pd.read_csv(csv_file_path,sep=';',encoding='latin1')
    df.columns=df.columns.str.strip().str.lower()
    if'purchase_price' in df.columns:
        df['purchase_price']=(
            df['purchase_price'].astype(str)
                                .str.replace('$','',regex=False)
                                .astype(float)
        )
    else:
            print("\n--- ERREUR CRITIQUE DE CHARGEMENT ---")
            print("Noms des colonnes réels après le nettoyage:",df.columns.tolist())
            raise KeyError("La colonne 'purchase_price' est introuvable après la lecture du CSV.")
    df_out = generate_price_table(df, logistics_rate, it_rate, personnel_rate, profit_margin)
    st.dataframe(df_out)
    st.download_button("Download Results", df_out.to_csv(index=False), file_name="retail_prices.csv")
