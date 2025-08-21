import streamlit as st
import numpy as np
import pandas as pd

# Title
st.title("🎓 Student Marks Analysis with NumPy & Streamlit")

# Sidebar input
st.sidebar.header("Settings")
num_students = st.sidebar.slider("Number of Students", 10, 200, 50)
num_subjects = st.sidebar.slider("Number of Subjects", 2, 10, 5)
seed = st.sidebar.number_input("Random Seed", min_value=0, value=42, step=1)

# Generate random marks
np.random.seed(seed)
marks = np.random.randint(40, 100, size=(num_students, num_subjects))

# Create DataFrame for display
students = [f"Student {i+1}" for i in range(num_students)]
subjects = [f"Subject {j+1}" for j in range(num_subjects)]
df = pd.DataFrame(marks, index=students, columns=subjects)

# Calculate statistics
average_per_student = df.mean(axis=1)
average_per_subject = df.mean(axis=0)
highest_score = df.values.max()
lowest_score = df.values.min()
top_students = average_per_student.sort_values(ascending=False).head(5)

# Display data
st.subheader("📊 Student Marks (first 10 rows)")
st.dataframe(df.head(10))

st.subheader("📚 Average Marks per Subject")
st.bar_chart(average_per_subject)

st.subheader("🔥 Top 5 Students (by average marks)")
st.write(top_students)

# Show overall stats
st.subheader("📌 Summary")
st.write(f"🏆 Highest Score: {highest_score}")
st.write(f"⚠️ Lowest Score: {lowest_score}")
st.write(f"📈 Overall Average: {df.values.mean():.2f}")
