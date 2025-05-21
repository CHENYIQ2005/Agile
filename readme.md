# 🎬 **Opération Netflix** : l’outil ultime pour gérer vos séries


As-tu déjà pensé à ce qui se passe **dans les coulisses** pendant que tu binges ta série préférée sur Netflix ?  
Qui tient à jour les infos sur les séries ?  
Quels acteurs jouent dedans ? Combien de saisons existent ? 

C’est pour répondre à toutes ces questions qu’est né ce petit projet de gestion de séries ! 🎬

---

## 👩‍💻 Pour qui ?

🎬 **Les plateformes** (comme Netflix) — pour enregistrer toutes les infos utiles sur les séries.

🎥 **Les équipes de production** — pour connaître facilement les liens entre acteurs et séries.


---

## 🛠️ Étapes du développement

### 🎬 1 : C’est parti ! Création d’une `Serie`

On commence par créer un nouvel objet série — un peu comme si on venait tout juste de trouver un titre,  
mais sans acteur ni scénario pour l’instant.

> J’ai créé et instancié un nouvel objet `Serie`.  
> Au début, il était encore vide, avec seulement un titre et quelques informations de base — un peu comme une série fraîchement imaginée, sans contenu pour l’instant.
> 
> <img width="415" alt="image" src="https://github.com/user-attachments/assets/321dd9bd-ae11-477b-b20e-c0a37140a0b1" />


### 🔧 2. **Petit bonus** : grâce à la méthode `ajouterSaisons()`, on peut ajouter de nouvelles saisons à volonté.  
C’est comme si l’équipe de production disait : *« Le public adore ? Allez, on tourne trois saisons de plus ! »*

> Ensuite, j’ai appelé la méthode `ajouterSaisons()` pour ajouter plusieurs saisons.  
> J’ai saisi le nombre de saisons, validé — quelques lignes d’interaction.  
> Chaque saison ajoutée représentait une étape vers une série plus complète, plus aboutie.
>
> <img width="415" alt="image" src="https://github.com/user-attachments/assets/5fdff841-50ec-43ca-9620-30ac0e43585f" />


### 3. Visualisation avec l’outil **Inspecter** de BlueJ

> Enfin, j’ai utilisé l’outil **Inspecter** pour visualiser l’état actuel de l’objet.  
> En l’ouvrant, j’ai pu voir la structure, le nombre et les détails des saisons contenues dans l’objet `Serie`.
>
><img width="377" alt="image" src="https://github.com/user-attachments/assets/0e971510-39c5-411c-8090-dccb8f9dd2fb" />
<img width="388" alt="image" src="https://github.com/user-attachments/assets/2e6746af-40b0-4270-ad0f-8cc3d7ed872e" />
<img width="415" alt="image" src="https://github.com/user-attachments/assets/8f6132a0-185e-4090-b4fa-d290af615fd5" />



---

## ✅ Mise en place des tests unitaires
###  Et les tests alors ? On veut du solide ! 🔍

### 4. Création de la classe `SerieTest`
Tester, c’est comme goûter une recette avant de la servir à ses invités.  
Alors j’ai sorti ma loupe de développeur et j’ai créé une classe spéciale : `SerieTest`.  
Passer ma classe `Serie` au crible, histoire de m'assurer qu'elle se comporte bien avant de monter sur scène. 🎭
 
> Pour m’assurer que tout fonctionne comme prévu, j’ai commencé par créer une nouvelle classe de test appelée `SerieTest`.  
> C’est un peu comme installer une table d’examen : tout ce que je vais coder dans ma classe `Serie` devra maintenant passer par cette étape de validation.

### 5. Initialisation avec `@BeforeEach`
Avant chaque test, on nettoie le plateau et on repart à zéro.  
Grâce à la méthode `@BeforeEach`, j’ai créé une série de base (`serie1`) pour avoir un terrain neutre à chaque fois.  
Un peu comme si on remettait tous les accessoires en place avant de rejouer une scène.
 
> Cela me permet d’avoir un point de départ commun pour tous les tests, comme un environnement propre avant chaque expérience.

### 6. Méthode de test `testAjouterSaisons()`

> Puis, j’ai créé une méthode de test `testAjouterSaisons()`, dans laquelle j’ai simulé l’ajout de saisons à ma série.  
> À chaque appel, je vérifie que le comportement correspond bien à ce que j’attends : que le nombre de saisons a bien été mis à jour, par exemple.

> Et enfin, moment de vérité : **j’ai lancé l’exécution du test... et la barre est apparue verte. ✅**  
> Pas d’erreur, pas d’exception : mon code passe le test avec succès.
>
> ![image](https://github.com/user-attachments/assets/108f607e-443c-4c85-b88c-1f9c11e1c989)


---

### 🎭 Étape 2 : Casting en cours ! Ajout de l’acteur `Acteur`

### 7. Création de la classe `Acteur`

> Une série sans acteur ? Impossible.  
> Pour aller plus loin dans la modélisation, j’ai créé une nouvelle classe `Acteur`, avec un attribut de type `Serie` à l’intérieur.  
> Cela permet d’établir une **relation unidirectionnelle** : l’acteur connaît la série dans laquelle il joue, mais la série ne garde pas directement de référence vers lui.

> Une relation simple, claire — de type **(0..1 à 0..1)**.

### 8. Méthode `setSerie()` dans `Acteur`

> Dans la classe `Acteur`, j’ai ensuite ajouté une méthode `setSerie(Serie serie)`.  
> Grâce à elle, on peut associer un acteur à une série spécifique，comme si l’on distribuait un rôle à un comédien dans un projet bien défini.
>
> <img width="415" alt="image" src="https://github.com/user-attachments/assets/d291c29c-3cd9-4c25-ab81-e0f432bb690a" />
<img width="415" alt="image" src="https://github.com/user-attachments/assets/032e32de-b5c8-46ea-80b5-8ccbb5b87dc7" />



---

## 🔁 Intégration dans les tests

### 9. Utilisation de l’acteur dans la fixture

> Dans la méthode `setUp()` de `SerieTest`, j’ai instancié un objet `Acteur` et je lui ai assigné une série via la méthode `setSerie()`.  
> Une étape essentielle pour tester que cette liaison fonctionne correctement dès la phase d’initialisation.
>
> <img width="416" alt="image" src="https://github.com/user-attachments/assets/f5fb5fef-cbc8-457a-8808-de9bb66fc04d" />
![image](https://github.com/user-attachments/assets/bbc4bfbe-076a-4af8-8666-d73fcb1c8659)



### 10. Méthode de test `testPromotionMessage()`

> Ensuite, j’ai créé interactivement une méthode de test, qui utilise ces objets pour vérifier que le **message promotionnel de l’acteur correspond bien à la série associée**.
>
> ![image](https://github.com/user-attachments/assets/e399b603-560d-4037-9757-8fda7fed8ae2)


---

## 🟩 Résultat final

💡 **J’exécute le test… et la barre devient verte.**  
Un petit moment de satisfaction : cela signifie que **ma logique fonctionne**, que les objets sont bien reliés, et que mes méthodes répondent aux attentes.

![image](https://github.com/user-attachments/assets/99cf61f4-e35b-4de1-b34e-923ba24b4a81)





