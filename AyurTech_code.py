import tkinter as tk

# Dictionary for disease and drug suggestions
disease_drugs = {
    "Common Cold": ["Neem", "Turmeric"],
    "Arthritis": ["Turmeric"],
    "Digestive Disorders": ["Ginger", "Fennel", "Cumin"],
    "Skin Allergies": ["Neem", "Aloe Vera"],
    "Hypertension": ["Arjuna", "Garlic"],
    "Diabetes": ["Fenugreek", "Cinnamon"],
    "Asthma": ["Licorice", "Tulsi"],
    "Anxiety": ["Ashwagandha", "Brahmi"],
    "Hair Loss": ["Amla", "Bhringraj"],
    "Indigestion": ["Triphala", "Aloe Vera"],
    "Migraine": ["Peppermint", "Lavender"],
    "Rheumatoid Arthritis":["Ashwagandha", "Guggul"],
    "Hepatitis": ["Bhumyamalaki", "Kutki"],
    "Menstrual Irregularities": ["Shatavari", "Lodhra"],
    "Obesity": ["Guggul", "Triphala"],
    "Acne": ["Neem", "Manjistha"],
    "Chronic Fatigue": ["Ashwagandha", "Shilajit"],
    "Cough": ["Honey", "Tulsi"],
    "Insomnia": ["Brahmi", "Jatamansi"],
    "Constipation": ["Triphala", "Haritaki"],
    "Hemorrhoids": ["Aloe Vera", "Turmeric"],
    "Allergies": ["Neem", "Turmeric"],
    "High Cholesterol": ["Arjuna", "Garlic"],
    "Eczema": ["Neem", "Aloe Vera"],
    "Gastric Ulcers": ["Licorice", "Amla"],
    "PCOS": ["Shatavari", "Ashoka"],
    "Anemia": ["Ashwagandha", "Triphala"],
    "Psoriasis": ["Neem", "Manjistha"],
    "Osteoporosis": ["Ashwagandha", "Guggul"],
    "Dandruff": ["Aloe Vera", "Bhringraj"],
    "Gout": ["Ginger", "Punarnava"],
    "Thyroid Disorders": ["Kanchanar", "Guggul"],
    "Hemorrhoids": ["Triphala", "Aloe Vera"],
    "Urinary Tract Infections": ["Neem", "Gokshura"],
    "Depression": ["Ashwagandha", "Jatamansi"],
    "Migraine": ["Peppermint", "Lavender"],
    "Rheumatoid Arthritis": ["Ashwagandha", "Guggul"],
    "Heartburn": ["Aloe Vera", "Licorice"],
    "Osteoarthritis": ["Turmeric", "Guggul"],
    "Stress": ["Ashwagandha", "Brahmi"],
    "Hypothyroidism": ["Kanchanar", "Guggul"],
    "Piles": ["Triphala", "Aloe Vera"],
    "Kidney Stones": ["Punarnava", "Gokshura"],
    "Depression": ["Ashwagandha", "Jatamansi"],
    "Migraine": ["Peppermint", "Lavender"],
    "Rheumatoid Arthritis": ["Ashwagandha", "Guggul"],
    "Heartburn": ["Aloe Vera", "Licorice"],
    "Osteoarthritis": ["Turmeric", "Guggul"],
    "Stress": ["Ashwagandha", "Brahmi"],
    "Hypothyroidism": ["Kanchanar", "Guggul"],
    "Piles": ["Triphala", "Aloe Vera"],
    "Kidney Stones": ["Punarnava", "Gokshura"],
    "fever": ["Neem", "Turmeric"],
    "Hypertension": ["Arjuna", "Garlic", "Hawthorn"],
    "Diabetes": ["Fenugreek", "Cinnamon", "Bitter Melon"],
    "Asthma": ["Licorice", "Tulsi", "Ginger Tea"],
    "Anxiety": ["Ashwagandha", "Brahmi", "Valerian Root"],
    "Hair Loss": ["Amla", "Bhringraj", "Saw Palmetto"],
    "Indigestion": ["Triphala", "Aloe Vera", "Chamomile"],
    "Migraine": ["Peppermint", "Lavender", "Butterbur"],
    "Hepatitis": ["Bhumyamalaki", "Kutki", "Milk Thistle"],
    "Menstrual Irregularities": ["Shatavari", "Lodhra", "Dong Quai"],
    "Obesity": ["Guggul", "Triphala", "Green Tea"],
    "Acne": ["Neem", "Manjistha", "Tea Tree Oil"],
    "Chronic Fatigue": ["Ashwagandha", "Shilajit", "Rhodiola"],
    "Cough": ["Honey", "Tulsi", "Echinacea"],
    "Insomnia": ["Brahmi", "Jatamansi", "Lemon Balm"],
    "Constipation": ["Triphala", "Haritaki", "Psyllium Husk"],
    "Hemorrhoids": ["Aloe Vera", "Turmeric", "Witch Hazel"],
    "Allergies": ["Neem", "Turmeric", "Quercetin"],
    "High Cholesterol": ["Arjuna", "Garlic", "Red Yeast Rice"],
    "Eczema": ["Neem", "Aloe Vera", "Oatmeal Baths"],
    "Gastric Ulcers": ["Licorice", "Amla", "Marshmallow Root"],
    "PCOS (Polycystic Ovary Syndrome)": ["Shatavari", "Ashoka", "Inositol"],
    "Anemia": ["Ashwagandha", "Triphala", "Iron Supplements"],
    "Psoriasis": ["Neem", "Manjistha", "Dead Sea Salt Baths"],
    "Osteoporosis": ["Ashwagandha", "Guggul", "Calcium Supplements"],
    "Dandruff": ["Aloe Vera", "Bhringraj", "Tea Tree Shampoo"],
    "Gout": ["Ginger", "Punarnava", "Cherry Juice"],
    "Thyroid Disorders": ["Kanchanar", "Guggul", "Selenium"],
    "Urinary Tract Infections": ["Neem", "Gokshura", "Cranberry"],
    "Depression": ["Ashwagandha", "Jatamansi", "St. John's Wort"],
    "Heartburn": ["Aloe Vera", "Licorice", "Ginger"],
    "Osteoarthritis": ["Turmeric", "Guggul", "Glucosamine"],
    "Stress": ["Ashwagandha", "Brahmi", "L-Theanine"],
    "Hypothyroidism": ["Kanchanar", "Guggul", "Ashwagandha"],
    "Piles": ["Triphala", "Aloe Vera", "Witch Hazel"],
    "Kidney Stones": ["Punarnava", "Gokshura", "Dandelion Root"],
    # Add more diseases and drug suggestions as needed
}

# Function to suggest drugs based on the disease
def suggest_drugs():
    disease = entry.get()
    if disease in disease_drugs:
        suggested_drugs = "\n".join([f"{i + 1}. {drug}" for i, drug in enumerate(disease_drugs[disease])])
        result_label.config(text=f"Suggested drugs for {disease}:\n{suggested_drugs}")
    else:
        result_label.config(text=f"No drug suggestions found for {disease}.")

# the main window
root = tk.Tk()
root.title("Drug Suggestion App")

#  configure input elements
label = tk.Label(root, text="Enter a disease name:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack()

suggest_button = tk.Button(root, text="Suggest Drugs", command=suggest_drugs)
suggest_button.pack(pady=10)

# configure output label
result_label = tk.Label(root, text="", wraplength=300)
result_label.pack(pady=10)

# the main GUI loop
root.mainloop()
