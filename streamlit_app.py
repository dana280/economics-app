"""
אפליקציה ללימוד תופעת המחסור והוצאות אלטרנטיביות
Economics Education App - Scarcity & Opportunity Cost

Streamlit Web App Version
"""

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# הגדרת העמוד
st.set_page_config(
    page_title="אפליקציה ללימוד כלכלה",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS מותאם אישית - מינימלי ללפטופ
st.markdown("""
<style>
    .main {
        direction: rtl;
        text-align: right;
        padding-top: 0.2rem;
        padding-bottom: 0rem;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 28px;
        font-size: 11px;
        font-weight: bold;
        padding: 0 8px;
        margin: 0;
    }
    .block-container {
        padding-top: 1rem;
        padding-bottom: 0rem;
        max-width: 100%;
    }
    .element-container {
        margin-bottom: 0.2rem;
    }
    h1, h2, h3, h4 {
        text-align: right;
        margin: 0.2rem 0;
    }
    .stTabs [data-baseweb="tab-list"] {
        direction: rtl;
        gap: 1px;
    }
    .stTabs [data-baseweb="tab-list"] button {
        font-size: 13px;
        padding: 8px 12px;
    }
    .stTabs [data-baseweb="tab-panel"] {
        padding-top: 0.5rem;
    }
    div[data-testid="stVerticalBlock"] > div {
        gap: 0.2rem;
    }
</style>
""", unsafe_allow_html=True)

# יצירת טאבים (ללא כותרת - חוסכים מקום)
tab1, tab2, tab3 = st.tabs(["📊 עקומת התמורה - תופעת המחסור", "🔢 מחשבון", "🎓 קוויז"])

# ==================== טאב 1: עקומת התמורה ====================
with tab1:
    
    # נתוני ייצור
    production_data = [
        (0, 10), (1, 8), (2, 6), (3, 4), (4, 2), (5, 0)
    ]
    
    col1, col2 = st.columns([2.5, 1.5])
    
    with col1:
        
        # כפתורים לבחירת נקודה
        cols = st.columns(6)
        selected_point = None
        
        for i, (x, y) in enumerate(production_data):
            with cols[i]:
                if st.button(f"({x}, {y})", key=f"point_{i}"):
                    st.session_state['selected_point'] = i
        
        # ברירת מחדל
        if 'selected_point' not in st.session_state:
            st.session_state['selected_point'] = 2
        
        # קבלת הנקודה הנבחרת
        idx = st.session_state['selected_point']
        current_x, current_y = production_data[idx]
        
        # יצירת הגרף
        fig, ax = plt.subplots(figsize=(4.2, 2.8))
        
        xs = [p[0] for p in production_data]
        ys = [p[1] for p in production_data]
        
        # ציור העקומה
        ax.plot(xs, ys, 'b-', linewidth=1.5, label='עקומה', marker='o', markersize=4)
        
        # הדגשת הנקודה הנבחרת
        ax.plot(current_x, current_y, 'ro', markersize=10, label='נוכחית', zorder=5)
        
        ax.set_xlabel('מוצר X', fontsize=9)
        ax.set_ylabel('מוצר Y', fontsize=9)
        ax.set_title('עקומת התמורה (PPC)', fontsize=10, fontweight='bold', pad=5)
        ax.grid(True, alpha=0.3, linestyle='--')
        ax.legend(loc='upper right', fontsize=8)
        ax.set_xlim(-0.5, 5.5)
        ax.set_ylim(-0.5, 10.5)
        ax.tick_params(labelsize=8)
        
        st.pyplot(fig)
        plt.close()
    
    with col2:
        
        # הצגת הנקודה הנוכחית
        st.markdown(f"""
        <div style='background-color: #E3F2FD; padding: 6px 10px; border-radius: 6px; 
                    border-right: 3px solid #2196F3; margin: 3px 0; text-align: center;'>
            <strong style='font-size: 12px;'>נקודה נוכחית:</strong>
            <div style='color: #2196F3; font-size: 17px; font-weight: bold; margin-top: 3px;'>
                {current_x} מוצר X, {current_y} מוצר Y
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # חישוב הוצאות
        max_y = production_data[0][1]
        total_cost = max_y - current_y
        average_cost = total_cost / current_x if current_x > 0 else 0
        marginal_cost = (production_data[idx - 1][1] - current_y) if idx > 0 else 0
        
        st.markdown("<div style='font-size: 12px; font-weight: bold; margin: 5px 0 3px 0;'>הוצאות אלטרנטיביות:</div>", unsafe_allow_html=True)
        
        # הוצאה כוללת
        st.markdown(f"""
        <div style='background-color: #E3F2FD; padding: 5px 8px; border-radius: 5px; 
                    border-right: 3px solid #2196F3; margin: 2px 0;'>
            <div style='font-size: 11px;'><strong>כוללת (Total):</strong></div>
            <div style='font-size: 18px; color: #1976D2; font-weight: bold;'>{total_cost} <span style='font-size: 12px;'>יח' Y</span></div>
            <div style='font-size: 9px; color: #666;'>{max_y} - {current_y} = {total_cost}</div>
        </div>
        """, unsafe_allow_html=True)
        
        # הוצאה ממוצעת
        st.markdown(f"""
        <div style='background-color: #FFF9C4; padding: 5px 8px; border-radius: 5px; 
                    border-right: 3px solid #FBC02D; margin: 2px 0;'>
            <div style='font-size: 11px;'><strong>ממוצעת (Average):</strong></div>
            <div style='font-size: 18px; color: #F9A825; font-weight: bold;'>{average_cost:.1f} <span style='font-size: 12px;'>Y/X</span></div>
            <div style='font-size: 9px; color: #666;'>{total_cost} ÷ {current_x} = {average_cost:.1f}</div>
        </div>
        """, unsafe_allow_html=True)
        
        # הוצאה שולית
        if idx > 0:
            st.markdown(f"""
            <div style='background-color: #FFEBEE; padding: 5px 8px; border-radius: 5px; 
                        border-right: 3px solid #E53935; margin: 2px 0;'>
                <div style='font-size: 11px;'><strong>שולית (Marginal):</strong></div>
                <div style='font-size: 18px; color: #C62828; font-weight: bold;'>{marginal_cost} <span style='font-size: 12px;'>יח' Y</span></div>
                <div style='font-size: 9px; color: #666;'>עלות יחידה #{current_x}</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div style='background-color: #FFEBEE; padding: 5px 8px; border-radius: 5px; 
                        border-right: 3px solid #E53935; margin: 2px 0;'>
                <div style='font-size: 11px;'><strong>שולית (Marginal):</strong></div>
                <div style='font-size: 13px; color: #666;'>אין יחידה קודמת</div>
            </div>
            """, unsafe_allow_html=True)
        
        # מקרא
        st.markdown("""
        <div style='margin-top: 5px; padding: 4px 8px; background-color: #f8f8f8; border-radius: 5px; 
                    border: 1px solid #ddd; text-align: center;'>
            <span style='font-size: 10px;'>
            🟢 יעיל | 🟡 לא יעיל | 🔴 בלתי אפשרי
            </span>
        </div>
        """, unsafe_allow_html=True)

# ==================== טאב 2: מחשבון ====================
with tab2:
    st.header("מחשבון הוצאות אלטרנטיביות")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("הגדר את התרחיש שלך:")
        
        # קלט שמות מוצרים
        product_x = st.text_input("שם מוצר X:", value="מכוניות", key="prod_x")
        product_y = st.text_input("שם מוצר Y:", value="אופניים", key="prod_y")
        
        st.markdown("---")
        
        # סליידרים
        max_y = st.slider(f"מקסימום {product_y} (Ymax):", 
                         min_value=10, max_value=200, value=100, step=5)
        
        quantity_x = st.slider(f"כמות {product_x} שאתה מייצר:", 
                              min_value=0, max_value=50, value=10, step=1)
        
        actual_y = st.slider(f"כמות {product_y} בפועל:", 
                            min_value=0, max_value=max_y, value=80, step=5)
    
    with col2:
        st.subheader("תוצאות:")
        
        # חישובים
        opp_cost = max_y - actual_y
        avg_cost = opp_cost / quantity_x if quantity_x > 0 else 0
        
        # הצגת תוצאות
        st.markdown(f"""
        <div class='metric-card'>
            <h3 style='margin: 0; text-align: center;'>הוצאה אלטרנטיבית כוללת</h3>
            <h1 style='margin: 10px 0; text-align: center;'>{opp_cost}</h1>
            <p style='margin: 0; text-align: center;'>{product_y}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class='metric-card'>
            <h3 style='margin: 0; text-align: center;'>הוצאה ממוצעת</h3>
            <h1 style='margin: 10px 0; text-align: center;'>{avg_cost:.2f}</h1>
            <p style='margin: 0; text-align: center;'>{product_y} / {product_x}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### הסבר:")
        st.info(f"""
        **כדי לייצר {quantity_x} {product_x}, ויתרת על {opp_cost} {product_y}.**
        
        המשמעות: בממוצע, כל {product_x} "עולה" לך {avg_cost:.2f} {product_y}.
        
        זו ההוצאה האלטרנטיבית - מה שוויתרת עליו כדי לייצר את מה שבחרת.
        """)
        
        # דוגמה
        with st.expander("💡 רוצה דוגמה?"):
            st.markdown(f"""
            **דוגמה:**
            - אם יכולתי לייצר מקסימום 100 {product_y}
            - אבל ייצרתי רק 80 {product_y}
            - כי ייצרתי 10 {product_x}
            - אז העלות היא: **20 {product_y}**
            
            **כלומר:** כל {product_x} "עלה" לי בממוצע 2 {product_y}
            """)

# ==================== טאב 3: קוויז ====================
with tab3:
    st.header("קוויז - בדוק את הידע שלך!")
    
    # שאלות
    questions = [
        {
            "question": "מהי תופעת המחסור?",
            "options": [
                "יש לנו מספיק משאבים לכל הצרכים",
                "יש לנו משאבים מוגבלים אבל צרכים בלתי מוגבלים",
                "אנחנו לא צריכים לבחור בין אפשרויות",
                "כל האנשים עניים"
            ],
            "correct": 1,
            "explanation": "תופעת המחסור היא המצב שבו משאבים מוגבלים, אבל הצרכים והרצונות שלנו בלתי מוגבלים. לכן אנחנו חייבים לבחור איך להשתמש במשאבים."
        },
        {
            "question": "מהי הוצאה אלטרנטיבית?",
            "options": [
                "הכסף ששילמתי על משהו",
                "הערך של האפשרות הטובה ביותר שוויתרתי עליה",
                "סכום כל ההוצאות שלי",
                "מה שחסכתי"
            ],
            "correct": 1,
            "explanation": "הוצאה אלטרנטיבית היא הערך של האפשרות הטובה ביותר שוויתרת עליה כשבחרת באפשרות אחרת. לדוגמה: אם בחרת ללמוד במקום לעבוד, ההוצאה האלטרנטיבית היא השכר שהיית יכול להרוויח."
        },
        {
            "question": "מה מציגה עקומת התמורה (PPC)?",
            "options": [
                "את המחירים של מוצרים שונים",
                "את כל השילובים האפשריים של שני מוצרים שאפשר לייצר",
                "את הרווח של החברה",
                "את הביקוש למוצרים"
            ],
            "correct": 1,
            "explanation": "עקומת התמורה (Production Possibilities Curve) מציגה את כל השילובים האפשריים של שני מוצרים שניתן לייצר עם המשאבים הקיימים. כל נקודה על העקומה מייצגת ייצור יעיל."
        },
        {
            "question": "אם אתה על עקומת התמורה, מה זה אומר?",
            "options": [
                "אתה מבזבז משאבים",
                "אתה מייצר ביעילות מקסימלית",
                "אתה צריך יותר עובדים",
                "אתה מפסיד כסף"
            ],
            "correct": 1,
            "explanation": "כשאתה על עקומת התמורה, אתה מנצל את כל המשאבים שלך בצורה יעילה. אי אפשר לייצר יותר ממוצר אחד בלי לוותר על המוצר השני."
        }
    ]
    
    # אתחול session state
    if 'quiz_started' not in st.session_state:
        st.session_state['quiz_started'] = False
        st.session_state['current_q'] = 0
        st.session_state['score'] = 0
        st.session_state['answered'] = False
        st.session_state['user_answer'] = None
    
    # התחלת קוויז
    if not st.session_state['quiz_started']:
        st.info("🎓 הקוויז מכיל 4 שאלות. בחר תשובה ולחץ 'בדוק' כדי לראות אם צדקת!")
        if st.button("🚀 התחל קוויז", key="start_quiz"):
            st.session_state['quiz_started'] = True
            st.session_state['current_q'] = 0
            st.session_state['score'] = 0
            st.rerun()
    else:
        # הצגת התקדמות
        progress = st.session_state['current_q'] / len(questions)
        st.progress(progress)
        st.markdown(f"**שאלה {st.session_state['current_q'] + 1} מתוך {len(questions)}** | "
                   f"**ציון: {st.session_state['score']}/{len(questions)}**")
        
        if st.session_state['current_q'] < len(questions):
            q = questions[st.session_state['current_q']]
            
            st.markdown(f"### {q['question']}")
            
            # אפשרויות תשובה
            user_answer = st.radio(
                "בחר תשובה:",
                options=range(len(q['options'])),
                format_func=lambda x: q['options'][x],
                key=f"q_{st.session_state['current_q']}"
            )
            
            col1, col2, col3 = st.columns([1, 1, 2])
            
            with col1:
                if st.button("✓ בדוק תשובה", key="check"):
                    st.session_state['answered'] = True
                    st.session_state['user_answer'] = user_answer
                    if user_answer == q['correct']:
                        st.session_state['score'] += 1
                    st.rerun()
            
            # הצגת תוצאה
            if st.session_state['answered']:
                if st.session_state['user_answer'] == q['correct']:
                    st.markdown(f"""
                    <div class='success-box'>
                        <h3>✓ כל הכבוד! תשובה נכונה!</h3>
                        <p>{q['explanation']}</p>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div class='error-box'>
                        <h3>✗ לא נכון, אבל בוא נלמד:</h3>
                        <p><strong>התשובה הנכונה:</strong> {q['options'][q['correct']]}</p>
                        <p>{q['explanation']}</p>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col2:
                    if st.button("→ שאלה הבאה", key="next"):
                        st.session_state['current_q'] += 1
                        st.session_state['answered'] = False
                        st.session_state['user_answer'] = None
                        st.rerun()
        
        else:
            # סיום קוויז
            percentage = (st.session_state['score'] / len(questions)) * 100
            
            if percentage == 100:
                message = "🏆 מושלם! אתה מבין את החומר מצוין!"
                color = "#4CAF50"
            elif percentage >= 75:
                message = "👍 עבודה טובה! יש לך הבנה טובה של החומר"
                color = "#2196F3"
            else:
                message = "📚 כדאי לחזור על החומר ולנסות שוב"
                color = "#FF9800"
            
            st.markdown(f"""
            <div style='background-color: {color}; padding: 30px; border-radius: 15px; 
                        text-align: center; color: white;'>
                <h1 style='margin: 0; text-align: center;'>סיימת את הקוויז!</h1>
                <h2 style='margin: 20px 0; text-align: center;'>
                    הציון שלך: {st.session_state['score']}/{len(questions)} ({percentage:.0f}%)
                </h2>
                <h3 style='margin: 0; text-align: center;'>{message}</h3>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("🔄 התחל מחדש", key="restart"):
                st.session_state['quiz_started'] = False
                st.session_state['current_q'] = 0
                st.session_state['score'] = 0
                st.session_state['answered'] = False
                st.rerun()

# Sidebar
with st.sidebar:
    st.markdown("### 📚 על האפליקציה")
    st.info("""
    אפליקציה ללימוד:
    - תופעת המחסור
    - הוצאות אלטרנטיביות
    - עקומת התמורה (PPC)
    """)
    
    st.markdown("### 💡 טיפים")
    st.success("""
    - התחל עם הקוויז לבדיקת ידע
    - השתמש במחשבון לתרגול
    - ראה את העקומה בפעולה
    """)
    
    st.markdown("---")
    st.markdown("### 🔗 קישורים")
    st.markdown("[GitHub Repository](https://github.com/dana280/economics-app)")
    
    st.markdown("---")
    st.caption("נוצר עם ❤️ בעזרת Streamlit")
