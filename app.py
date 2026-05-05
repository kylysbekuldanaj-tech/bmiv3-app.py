
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils import *

st.set_page_config(page_title="Денсаулық қосымшасы", layout="centered")

# Theme
theme = st.radio("Тақырып:", ["Жарық", "Қараңғы"])
bg = "#ffe6f0" if theme=="Жарық" else "#1e1e1e"
text = "black" if theme=="Жарық" else "white"

st.markdown(f"""
<style>
body {{background-color:{bg}; color:{text};}}
.stButton>button {{background:pink;border-radius:10px;}}
</style>
""", unsafe_allow_html=True)

# Login
if "login" not in st.session_state:
    st.session_state.login=False

if not st.session_state.login:
    u=st.text_input("Логин")
    p=st.text_input("Пароль", type="password")
    if st.button("Кіру"):
        if u=="admin" and p=="1234":
            st.session_state.login=True
        else:
            st.error("Қате")
    st.stop()

st.title("💖 Денсаулық қосымшасы")

# Inputs
name=st.text_input("Атың")
age=st.number_input("Жас",10,100)
weight=st.number_input("Салмақ",30,200)
height=st.number_input("Бой",100,220)

if st.button("Есептеу"):
    bmi=calculate_bmi(weight,height)
    cat,color=bmi_category(bmi)

    st.markdown(f"<h3 style='color:{color}'>BMI {bmi:.2f} - {cat}</h3>",unsafe_allow_html=True)

    st.write("💧",water_intake(weight),"мл")
    st.write("🔥",calories_needed(weight),"ккал")

    ideal=ideal_weight(height,age)
    st.success(f"Идеал: {ideal} кг")

    diff=abs(weight-ideal)
    st.info(f"{int(diff/2)+1} айда жетесің")

# ===== DAILY TRACKER =====
st.subheader("📅 Күнделікті трекер")

water=st.number_input("Ішкен су (мл)",0,5000)
cal=st.number_input("Калория",0,5000)
steps=st.number_input("Қадам",0,50000)

if st.button("Сақтау"):
    df=pd.DataFrame([[water,cal,steps]],columns=["water","cal","steps"])
    df.to_csv("tracker.csv",mode="a",header=False,index=False)
    st.success("Сақталды")

# Graphs
try:
    df=pd.read_csv("tracker.csv")
    st.subheader("📊 Трекер график")

    fig,ax=plt.subplots()
    ax.plot(df["water"], label="Су")
    ax.plot(df["cal"], label="Калория")
    ax.plot(df["steps"], label="Қадам")
    ax.legend()
    st.pyplot(fig)
except:
    st.info("Дерек жоқ")

# AI advice
st.subheader("🤖 Кеңес")
if steps<5000:
    st.warning("Көбірек жүр")
elif steps>10000:
    st.success("Жақсы белсенділік")
