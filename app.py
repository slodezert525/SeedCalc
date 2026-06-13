import streamlit as st

st.set_page_config(page_title="Seeds Per Acre Calculator")

st.title("Seeds Per Acre Calculator")

bed_size = st.number_input(
    "Bed Size (inches)",
    min_value=0.1,
    value=40.0
)

seed_lines = st.number_input(
    "Seed Lines",
    min_value=1,
    value=2
)

spacing = st.number_input(
    "In-Row Spacing (inches)",
    min_value=0.1,
    value=12.0
)

ms_per_acre = (
    43560 /
    ((spacing / 12) * (bed_size / 12)) *
    seed_lines
) / 1000

st.metric(
    "M's Per Acre",
    f"{ms_per_acre:,.2f}"
)
