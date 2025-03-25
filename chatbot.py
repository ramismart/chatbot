import pandas as pd
import streamlit as st

def load_faq(file_path):
    """Charge la FAQ à partir d'un fichier Excel et nettoie les données."""
    df = pd.read_excel(file_path, sheet_name="FAQ")
    df.fillna("", inplace=True)  # Remplace les valeurs NaN par des chaînes vides
    return df

def search_faq(question, df):
    """Recherche une réponse dans la FAQ en fonction des mots-clés de la question."""
    question = question.lower()
    
    # Recherche par mots-clés
    for index, row in df.iterrows():
        if any(keyword.lower() in question for keyword in str(row["Mots clés"]).split()):
            return row["Résolution gestionnaire"] or row["Résolution DSSIRH"] or "Aucune réponse trouvée."
    
    return "Je n'ai pas trouvé de réponse à votre question. Pouvez-vous reformuler ?"

# Interface web avec Streamlit
st.title("Chatbot RH - FAQ Résolution de demandes")
file_path = "FAQ Résolution demandes RENOIRH.xlsx"  # Remplacez par le bon chemin
faq_data = load_faq(file_path)

# Champ de saisie utilisateur
question = st.text_input("Posez votre question :")

if question:
    response = search_faq(question, faq_data)
    st.write("### Réponse :")
    st.write(response)
