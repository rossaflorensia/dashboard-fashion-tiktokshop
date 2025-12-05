import streamlit as st
import pandas as pd
import plotly.express as px

st.title("DASHBOARD PENJUALAN FASHION DI TIKTOKSHOP")

# Load dataset
df = pd.read_excel("dataset_final.xlsx")

# Bersihkan tanggal
df["date"] = pd.to_datetime(df["date"], errors="coerce")
df = df.dropna(subset=["date"])

# Filter kategori
kategori_list = ["Semua"] + sorted(df["category"].unique())
kategori = st.selectbox("Pilih Kategori Produk", kategori_list)

# Apply filter
if kategori == "Semua":
    df_filtered = df.copy()
else:
    df_filtered = df[df["category"] == kategori]

st.write("Data Saat Ini:")
st.dataframe(df_filtered)

# =======================
# 1. LINE CHART — REVENUE
# =======================
line_chart = px.line(
    df_filtered,
    x="date",
    y="revenue",
    title="Tren Pendapatan dari Waktu ke Waktu"
)
st.plotly_chart(line_chart)

# =======================
# 2. BAR CHART — TOTAL REVENUE PER CATEGORY
# =======================
bar_data = df.groupby("category")["revenue"].sum().reset_index()

bar_chart = px.bar(
    bar_data,
    x="category",
    y="revenue",
    title="Total Pendapatan per Kategori"
)
st.plotly_chart(bar_chart)

# =======================
# 3. PIE CHART — PROPOSI REVENUE
# =======================
pie_chart = px.pie(
    bar_data,
    names="category",
    values="revenue",
    title="Proporsi Pendapatan per Kategori"
)
st.plotly_chart(pie_chart)

# =======================
# 4. SCATTER — PRICE vs UNITS SOLD
# =======================
scatter_chart = px.scatter(
    df_filtered,
    x="price",
    y="units_sold",
    color="category",
    title="Hubungan Harga dan Jumlah Terjual"
)
st.plotly_chart(scatter_chart)

# =======================
# 5. AREA CHART — UNITS SOLD
# =======================
area_chart = px.area(
    df_filtered.sort_values("date"),
    x="date",
    y="units_sold",
    title="Trend Units Sold dari Waktu ke Waktu"
)
st.plotly_chart(area_chart)
