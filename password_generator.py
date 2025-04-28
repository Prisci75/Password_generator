import random
import string

def generate_password(length=12, use_special_chars=True):
    """ Génère un mot de passe sécurisé en excluant certains caractères spéciaux. """
    
    characters = string.ascii_letters + string.digits
    
    if use_special_chars:
        forbidden_chars = "~^[]}{`<>|()''"  # Liste des caractères à exclure
        special_chars = ''.join(c for c in string.punctuation if c not in forbidden_chars) 
        characters += special_chars  # Ajoute uniquement les caractères autorisés

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

password = generate_password(length=16, use_special_chars=True)
print(f"Votre mot de passe sécurisé : {password}")
