def calculate_bmi(weight, height):
    # Calculer l'IMC
    bmi = weight / (height ** 2)
    return bmi

def interpret_bmi(bmi):
    # Interpréter les résultats de l'IMC
    if bmi < 18.5:
        return "Insuffisance pondérale"
    elif 18.5 <= bmi < 24.9:
        return "Poids normal"
    elif 25 <= bmi < 29.9:
        return "Surpoids"
    else:
        return "Obésité"

def main():
    print("Calculateur d'IMC")
    
    try:
        weight = float(input("Entrez votre poids en kg: "))
        height = float(input("Entrez votre taille en mètres: "))
        
        if weight <= 0 or height <= 0:
            raise ValueError("Le poids et la taille doivent être des valeurs positives.")
        
        # Calculer l'IMC
        bmi = calculate_bmi(weight, height)
        print(f"Votre IMC est : {bmi:.2f}")
        
        # Fournir une interprétation
        result = interpret_bmi(bmi)
        print(f"Catégorie : {result}")

    except ValueError as e:
        print(f"Erreur : {e}")

if __name__ == "__main__":
    main()
