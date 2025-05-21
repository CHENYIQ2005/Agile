# 📺 Projet BlueJ : **Serie Netflix**

## 🎯 Contexte

À l’ère de la surcharge informationnelle, chaque plateforme cherche à lancer la prochaine série à succès.  
Mais avez-vous déjà pensé que derrière ces productions brillantes, il faut aussi une **gestion rigoureuse et bien structurée** ?

C’est précisément pour cela que notre projet a vu le jour.  
Il s'agit d'un **outil simple et fonctionnel** de gestion des informations sur les séries et les acteurs, destiné aux plateformes de contenu audiovisuel comme **Netflix**, etc.

---

## 🧩 Objectifs

Ce programme vise à modéliser deux entités principales :

- **`Serie`** : une série télévisée, avec un nom propre, qui peut voir son nombre de saisons augmenter au fil du temps et de son développement narratif.
- **`Acteur`** : un acteur ou une actrice, pouvant être associé(e) à une série précise, et susceptible d’en jouer plusieurs à l’avenir.

Grâce à ce programme, les éditeurs de contenu, les équipes de production, voire les développeurs de systèmes de gestion de médias peuvent :

- Créer un objet série, en saisissant son nom et le nombre initial de saisons ;
- Ajouter dynamiquement de nouvelles saisons；
- Associer un acteur à une série donnée；
- Générer un message promotionnel lié à un acteur et sa série；

---

## 🛠️ Étapes du développement

### 1. Création d’un objet `Serie`

> J’ai créé et instancié un nouvel objet `Serie`.  
> Au début, il était encore vide, avec seulement un titre et quelques informations de base — un peu comme une série fraîchement imaginée, sans contenu pour l’instant.
> 
> <img width="415" alt="image" src="https://github.com/user-attachments/assets/321dd9bd-ae11-477b-b20e-c0a37140a0b1" />


### 2. Ajout de saisons via la méthode `ajouterSaisons()`

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

### 4. Création de la classe `SerieTest`

> Pour m’assurer que tout fonctionne comme prévu, j’ai commencé par créer une nouvelle classe de test appelée `SerieTest`.  
> C’est un peu comme installer une table d’examen : tout ce que je vais coder dans ma classe `Serie` devra maintenant passer par cette étape de validation.

### 5. Initialisation avec `@BeforeEach`

> Dans la méthode annotée `@BeforeEach`, j’ai initialisé un objet `serie1`.  
> Cela me permet d’avoir un point de départ commun pour tous les tests, comme un environnement propre avant chaque expérience.

### 6. Méthode de test `testAjouterSaisons()`

> Puis, j’ai créé une méthode de test `testAjouterSaisons()`, dans laquelle j’ai simulé l’ajout de saisons à ma série.  
> À chaque appel, je vérifie que le comportement correspond bien à ce que j’attends : que le nombre de saisons a bien été mis à jour, par exemple.

> Et enfin, moment de vérité : **j’ai lancé l’exécution du test... et la barre est apparue verte. ✅**  
> Pas d’erreur, pas d’exception : mon code passe le test avec succès.
>
> ![image](https://github.com/user-attachments/assets/108f607e-443c-4c85-b88c-1f9c11e1c989)


---

## 🎭 Extension du projet : la classe `Acteur`

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



## 🚀 À venir

- Gestion de plusieurs séries pour un acteur
- Historique des saisons
- Interface graphique de visualisation

---

Merci pour votre lecture ! 🎉  
*Projet éducatif réalisé dans le cadre de l’apprentissage de la programmation objet avec BlueJ.*


