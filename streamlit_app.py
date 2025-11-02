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

# CSS מותאם אישית
st.markdown("""
<style>
    .main {
        direction: rtl;
        text-align: right;
        padding-top: 0.5rem;
    }
    .stButton>button {
        width: 100%;
        border-radius: 6px;
        height: 35px;
        font-size: 13px;
        font-weight: bold;
        padding: 0 10px;
    }
    .success-box {
        padding: 10px;
        border-radius: 6px;
        background-color: #C8E6C9;
        border-right: 3px solid #4CAF50;
        margin: 5px 0;
    }
    .error-box {
        padding: 10px;
        border-radius: 6px;
        background-color: #FFCDD2;
        border-right: 3px solid #F44336;
        margin: 5px 0;
    }
    .info-box {
        padding: 10px;
        border-radius: 6px;
        background-color: #E3F2FD;
        border-right: 3px solid #2196F3;
        margin: 5px 0;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 12px;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 5px 0;
    }
    h1, h2, h3, h4 {
        text-align: right;
        margin-bottom: 0.3rem;
        margin-top: 0.3rem;
    }
    .stTabs [data-baseweb="tab-list"] {
        direction: rtl;
        gap: 2px;
    }
    .element-container {
        margin-bottom: 0.3rem;
    }
    [data-testid="stVerticalBlock"] > [style*="flex-direction: column;"] > [data-testid="stVerticalBlock"] {
        gap: 0.3rem;
    }
</style>
""", unsafe_allow_html=True)

# כותרת קומפקטית
st.markdown("""
    <div style='background: linear-gradient(90deg, #2196F3 0%, #9C27B0 100%); 
                padding: 10px 20px; 
                border-radius: 10px; 
                text-align: center;
                margin-bottom: 15px;'>
        <h2 style='color: white; margin: 0; font-size: 20px; text-align: center;'>🎓 אפליקציה ללימוד כלכלה</h2>
        <p style='color: white; font-size: 13px; margin: 5px 0 0 0; text-align: center;'>
            תופעת המחסור והוצאות אלטרנטיביות
        </p>
    </div>
""", unsafe_allow_html=True)

# יצירת טאבים
tab1, tab2, tab3 = st.tabs(["📊 עקומת התמורה", "🔢 מחשבון", "🎓 קוויז"])

# ==================== טאב 1: עקומת התמורה ====================
with tab1:
    st.markdown("<h4 style='margin: 5px 0; font-size: 16px;'>עקומת התמורה (PPC)</h4>", unsafe_allow_html=True)
    
    # נתוני ייצור
    production_data = [
        (0, 10), (1, 8), (2, 6), (3, 4), (4, 2), (5, 0)
    ]
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown("<strong style='font-size: 12px;'>בחר נקודה:</strong>", unsafe_allow_html=True)
        
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
        fig, ax = plt.subplots(figsize=(5.5, 3.8))
        
        xs = [p[0] for p in production_data]
        ys = [p[1] for p in production_data]
        
        # ציור העקומה
        ax.plot(xs, ys, 'b-', linewidth=2, label='עקומת התמורה', marker='o', markersize=6)
        
        # הדגשת הנקודה הנבחרת
        ax.plot(current_x, current_y, 'ro', markersize=14, label='נקודה נוכחית', zorder=5)
        
        ax.set_xlabel('מוצר X', fontsize=10, fontweight='bold')
        ax.set_ylabel('מוצר Y', fontsize=10, fontweight='bold')
        ax.set_title('עקומת התמורה (PPC)', fontsize=11, fontweight='bold')
        ax.grid(True, alpha=0.3, linestyle='--')
        ax.legend(loc='upper right', fontsize=9)
        ax.set_xlim(-0.5, 5.5)
        ax.set_ylim(-0.5, 10.5)
        
        st.pyplot(fig)
        plt.close()
    
    with col2:
        st.markdown("<strong style='font-size: 12px;'>מידע על הנקודה:</strong>", unsafe_allow_html=True)
        
        # הצגת הנקודה הנוכחית
        st.markdown(f"""
        <div class='info-box' style='padding: 6px; margin: 3px 0;'>
            <strong style='font-size: 12px; display: block; text-align: center;'>הנקודה הנוכחית</strong>
            <h4 style='text-align: center; color: #2196F3; margin: 3px 0 0 0; font-size: 16px;'>{current_x} מוצר X, {current_y} מוצר Y</h4>
        </div>
        """, unsafe_allow_html=True)
        
        # חישוב הוצאות
        max_y = production_data[0][1]
        total_cost = max_y - current_y
        average_cost = total_cost / current_x if current_x > 0 else 0
        
        st.markdown("<strong style='font-size: 13px;'>הוצאות אלטרנטיביות:</strong>", unsafe_allow_html=True)
        
        # הוצאה כוללת
        st.markdown(f"""
        <div style='background-color: #E3F2FD; padding: 5px 8px; border-radius: 6px; 
                    border-right: 3px solid #2196F3; margin: 3px 0;'>
            <strong style='font-size: 11px;'>הוצאה כוללת:</strong>
            <span style='font-size: 16px; color: #1976D2;'><b>{total_cost}</b></span> יח' Y
            <span style='font-size: 10px; color: #666; margin-right: 5px;'>({max_y}-{current_y}={total_cost})</span>
        </div>
        """, unsafe_allow_html=True)
        
        # הוצאה ממוצעת
        st.markdown(f"""
        <div style='background-color: #FFF9C4; padding: 5px 8px; border-radius: 6px; 
                    border-right: 3px solid #FBC02D; margin: 3px 0;'>
            <strong style='font-size: 11px;'>הוצאה ממוצעת:</strong>
            <span style='font-size: 16px; color: #F9A825;'><b>{average_cost:.2f}</b></span> Y/X
            <span style='font-size: 10px; color: #666; margin-right: 5px;'>({total_cost}÷{current_x}={average_cost:.2f})</span>
        </div>
        """, unsafe_allow_html=True)
        
        # הוצאה שולית
        if idx > 0:
            prev_y = production_data[idx - 1][1]
            marginal_cost = prev_y - current_y
            st.markdown(f"""
            <div style='background-color: #FFEBEE; padding: 5px 8px; border-radius: 6px; 
                        border-right: 3px solid #E53935; margin: 3px 0;'>
                <strong style='font-size: 11px;'>הוצאה שולית:</strong>
                <span style='font-size: 16px; color: #C62828;'><b>{marginal_cost}</b></span> יח' Y
                <span style='font-size: 10px; color: #666; margin-right: 5px;'>(יחידה #{current_x})</span>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div style='background-color: #FFEBEE; padding: 5px 8px; border-radius: 6px; 
                        border-right: 3px solid #E53935; margin: 3px 0;'>
                <strong style='font-size: 11px;'>הוצאה שולית:</strong>
                <span style='font-size: 12px;'>אין יחידה קודמת</span>
            </div>
            """, unsafe_allow_html=True)
        
        # מקרא
        st.markdown("""
        <div style='margin-top: 8px; padding: 6px; background-color: #f5f5f5; border-radius: 5px;'>
        <strong style='font-size: 12px;'>מקרא:</strong>
        <span style='font-size: 11px;'>
        🟢 על העקומה - יעיל | 🟡 בתוך - לא יעיל | 🔴 מחוץ - בלתי אפשרי
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
