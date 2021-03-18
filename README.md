# SP-business-rules
We gaan aan het werk met het opzetten van een rule-based systeem ten behoeve van de recommendation engine.


Als mensen naar een bepaald product kijken ze ook geinterresseerd kunnen zijn in een ander product uit de zelfde categorie met de zelfde doelgroep en target.
Al deze kolommen worden dan samen gevoeg tot 1 kolom (combined genoemd) en samen met de product ID in een nieuwe tabel gezet genaamd contentFilter.


Voor de Collaborative Filtering missen we helaas alle data die nodig is om een goede recommendation te maken.
We hebben namelijk alleen een klantenid maar niks wat het koppelt aan een product dat is gekocht.
