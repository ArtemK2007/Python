import pandas as pd
from fpdf import FPDF
from faker import Faker
import random
import os

fake = Faker()

FONT_FILE = "arial-unicode-ms.ttf"
if not os.path.exists(FONT_FILE):
    print(f"⚠️ Будь ласка, додайте файл шрифту {FONT_FILE} у папку з програмою")
    exit()

def generate_students(n=5):
    students = []
    subjects_list = ["Математика", "Фізика", "Хімія", "Інформатика", "Англійська", "Біологія"]
    
    for _ in range(n):
        name = fake.first_name()
        surname = fake.last_name()
        subjects = random.sample(subjects_list, k=random.randint(3, 5))  # 3-5 предметів
        grades = [round(random.uniform(60, 100), 1) for _ in subjects]  # оцінки від 60 до 100
        average = sum(grades) / len(grades)
        students.append({
            "Name": name,
            "Surname": surname,
            "Subjects": ", ".join(subjects),
            "Grades": ", ".join(map(str, grades)),
            "Average": round(average, 2)
        })

    return students

def save_csv(students, filename="students.csv"):
    df = pd.DataFrame(students)
    df.to_csv(filename, index=False, encoding='utf-8-sig')
    print(f"Дані збережено у {filename}")

def generate_pdf(students, filename="students_report.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.add_font('ArialUnicode', '', FONT_FILE, uni=True)
    pdf.set_font('ArialUnicode', '', 14)
    pdf.cell(0, 10, "Звіт по студентам", ln=True, align='C')
    pdf.ln(10)
    pdf.set_font('ArialUnicode', '', 12)
    
    for s in students:
        pdf.multi_cell(0, 8, f"{s['Name']} {s['Surname']} | Предмети: {s['Subjects']} | "
                              f"Оцінки: {s['Grades']} | Середній бал: {s['Average']}")
        pdf.ln(1)
    
    pdf.output(filename)
    print(f"PDF-звіт збережено у {filename}")

def main():
    try:
        n = int(input("Скільки студентів згенерувати? "))
        students = generate_students(n)
        students_sorted = sorted(students, key=lambda x: x['Average'], reverse=True)
        print("\n=== Таблиця студентів ===")
        for s in students_sorted:
            print(f"{s['Name']} {s['Surname']}: {s['Average']:.2f}")
        print(f"\nКращий студент: {students_sorted[0]['Name']} {students_sorted[0]['Surname']}")
        save_csv(students_sorted)
        generate_pdf(students_sorted)
    except Exception as e:
        print(f"Сталася помилка: {e}")

if __name__ == "__main__":
    main()
