
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="פריסת חרוט קטום", layout="centered")

st.title("פריסת חרוט קטום עם מידות")
st.markdown("הכניסו את הקוטר העליון, הקוטר התחתון והגובה ולחצו על **Generate** להצגת הפריסה:")

d_top = st.number_input("קוטר עליון בסנטימטרים", min_value=0.0, step=0.1, value=6.0)
d_bottom = st.number_input("קוטר תחתון בסנטימטרים", min_value=0.0, step=0.1, value=10.0)
height = st.number_input("גובה החרוט בסנטימטרים", min_value=0.0, step=0.1, value=12.0)

if st.button("Generate"):
    r1 = d_bottom / 2
    r2 = d_top / 2
    L = np.sqrt(height**2 + (r1 - r2)**2)
    theta = 2 * np.pi * r1 / L
    R_inner = L - (r1 - r2)
    R_outer = L

    angles = np.linspace(0, theta, 500)
    x_outer = R_outer * np.cos(angles)
    y_outer = R_outer * np.sin(angles)
    x_inner = R_inner * np.cos(angles[::-1])
    y_inner = R_inner * np.sin(angles[::-1])

    fig, ax = plt.subplots(figsize=(6,6))
    ax.plot(x_outer, y_outer, 'b')
    ax.plot(x_inner, y_inner, 'r')
    ax.fill(np.concatenate([x_outer, x_inner]), np.concatenate([y_outer, y_inner]), 'lightblue', alpha=0.5)
    ax.plot([0, x_outer[0]], [0, y_outer[0]], 'k--')
    ax.plot([0, x_outer[-1]], [0, y_outer[-1]], 'k--')
    ax.text(0, R_outer + 1, f"הנותחת תשק: {2 * np.pi * r1:.2f} מס", ha='center')
    ax.text(0, R_inner - 1, f"הנוילע תשק: {2 * np.pi * r2:.2f} מס", ha='center')
    ax.text(0, R_inner / 2, f"ימינפ רטוק: {R_inner:.2f} סמ", ha='center', va='center', fontsize=10, color='purple')
    ax.text(x_outer[0] * 0.5, y_outer[0] * 0.5, f"םיסוידר שרפה: {L:.2f} מס")
    ax.set_aspect('equal')
    ax.axis('off')
    st.pyplot(fig)
    st.markdown(f"כדי לשרטט, סמנו שני מעגלים מאותה נקודת אמצע, לפי הקטרים הפנימי והחיצוני.")
    st.markdown(f"סמנו נקודה על המעגל הפנימי, ומדדו על הקשת את אורך הקשת בעזרת סגולי. סמנו שם נקודה.")
    st.markdown(f"מתחו בעזרת סרגל ארוך קו שעובר דרך אמצע המעגל, והנקודה על הקשת, וחותך את שתי הקשתות. חזרו על הפעולה גם עם הנקודה השניה שעל הקשת הפנימית.")
    st.markdown(f"זהו יש לכם את הגזרה ואפשר לגזור אותה")
