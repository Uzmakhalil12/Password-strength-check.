import streamlit as st
import re

# Function to check password strength
def check_password_strength(password):
    """Evaluates the strength of a password and returns a score & message."""

    # Common weak passwords list (expandable)
    common_passwords = {"123456", "password", "123456789", "qwerty", "abc123", "password1", "12345678"}

    # Strength score
    score = 0
    criteria = []

    # Check password length
    if len(password) >= 8:
        score += 1
        criteria.append("✅ Length is 8 or more characters")
    else:
        criteria.append("❌ Less than 8 characters")

    # Check uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
        criteria.append("✅ Contains uppercase letters")
    else:
        criteria.append("❌ No uppercase letters")

    # Check lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
        criteria.append("✅ Contains lowercase letters")
    else:
        criteria.append("❌ No lowercase letters")

    # Check digits
    if re.search(r"\d", password):
        score += 1
        criteria.append("✅ Contains numbers")
    else:
        criteria.append("❌ No numbers")

    # Check special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
        criteria.append("✅ Contains special characters")
    else:
        criteria.append("❌ No special characters")

    # Check common weak passwords
    if password.lower() in common_passwords:
        return 0, "❌ Common password. Choose a stronger one.", criteria

    # Determine password strength category
    if score == 5:
        return score, "🟢 Very Strong", criteria
    elif score == 4:
        return score, "🟡 Strong", criteria
    elif score == 3:
        return score, "🟠 Moderate", criteria
    else:
        return score, "🔴 Weak", criteria

# Streamlit UI
st.title("🔒 Password Strength Meter")

# User input
password = st.text_input("Enter your password:", type="password")

if password:
    score, strength_message, criteria = check_password_strength(password)
    
    # Display criteria check results
    st.subheader("Password Strength Analysis")
    for check in criteria:
        st.write(check)
    
    # Display strength message with color
    if score == 5:
        st.success(f"✅ Strength: {strength_message}")
    elif score == 4:
        st.warning(f"⚠️ Strength: {strength_message}")
    elif score == 3:
        st.info(f"ℹ️ Strength: {strength_message}")
    else:
        st.error(f"❌ Strength: {strength_message}")

