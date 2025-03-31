import streamlit as st
import random
import string

def password_strength(password):
    score = 0
    feedback = []
    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Include at least one uppercase letter.")
    
    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Include at least one lowercase letter.")
    
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Include at least one number.")
    
    if any(char in "!@#$%^&*()_+[]{}|;:,.<>?" for char in password):
        score += 1
    else:
        feedback.append("Include at least one special character.")
    
    return score, feedback

def get_strength_label(score):
    labels = [
        ('Weak', 'red'),
        ('Weak', 'orange'),
        ('Medium', 'yellow'),
        ('Strong', 'green'),
        ('Very Strong', 'blue'),
        ('Very Strong', 'purple')
    ]
    return labels[score]

def generate_password(length, include_uppercase, include_special, include_numbers):
    characters = string.ascii_lowercase  
    if include_uppercase:
        characters += string.ascii_uppercase  
    if include_special:
        characters += string.punctuation
    if include_numbers:
        characters += string.digits  
    return ''.join(random.choice(characters) for _ in range(length))

st.set_page_config(page_title="Password Strength Checker", page_icon="🔐")

st.markdown("""
    <style>
    body {
        background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
        color: white;
    }
    h1 {
        color: #4CAF50;
        text-align: center;
        font-family: 'Arial', sans-serif;
    }
    .stButton > button {
        background-color: #0000FF; 
        border: 2px solid #d1a3ff; 
        border-radius: 8px; 
        color: white;
        padding: 10px 20px; 
        font-size: 16px;
        font-weight: bold;
        cursor: pointer; 
        transition: 0.3s ease; 
    }
  
    * {
        font-family: 'Verdana', sans-serif;
    }
    section[data-testid="stSidebar"] {
        background: linear-gradient(to top, #6a2c91, #a072b4);  
        color: white !important;
    }
    .feedback-box {
        background-color: #444; 
        border-radius: 5px; 
        padding: 10px; 
        margin-bottom: 10px; 
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Password Strength Checker")

password = st.text_input("Enter your password", type="password", key="password")
if st.button("Check Password Strength"):
    if password:
        score, feedback = password_strength(password)
        strength_label, color = get_strength_label(score)
        
        st.markdown(f"<h3 style='color:{color};'>{strength_label}</h3>", unsafe_allow_html=True)
        st.progress(score / 5)  
        st.write(f"Password Strength Score: {score} / 5")
        
        if feedback:
            st.markdown("### Suggestions for Improvement:")
            for suggestion in feedback:
                st.markdown(f"""
                    <div class='feedback-box'>
                        <p style="font-size:16px;">{suggestion}</p>
                    </div>
                """, unsafe_allow_html=True)
    else:
        st.warning("Please enter a password to check its strength.")

st.subheader("Password Generator")
length = st.slider("Select Password Length", min_value=8, max_value=20, value=12)
include_uppercase = st.checkbox("Include Uppercase Letters?", value=True)
include_special = st.checkbox("Include Special Characters?", value=True)
include_numbers = st.checkbox("Include Numbers?", value=True)  

if st.button("Generate Password"):
    generated_password = generate_password(length, include_uppercase, include_special, include_numbers)
    st.text(f"Generated Password: {generated_password}")
