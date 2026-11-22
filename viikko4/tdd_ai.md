# TDD raportti

**Päätyikö agentti hyvään toteutukseen ja laadukkaisiin testeihin?**

Toteutus oli lopulta hyvä, kaikki 15 testiä menevät läpi ja hinta ja tavaroiden määrä lasketaan oikeasti ostoksista. Refaktoroinnissa toisteinen haku siirrettiin apumetodiin `_hae_ostos` ja turhat laskurit poistettiin. Testeissä oli ongelmia osassa B. Agentti yhdisti askeleiden 8 ja 9 testit yhdeksi, ja jouduin pyytämään sitä erottamaan ne.

**Pysyikö agentti osassa A minimitoteutuksessa, ja jättikö se testit rauhaan?**

Pääosin kyllä. Agentti toteutti vain sen, mitä testi vaati (ensin laskuri ja sitten hinnan summaus), eikä koskenut testeihin. Askeleet 1 ja 4-7 menivät läpi heti ilman uutta koodia, koska pohjassa oli jo `return 0` ja aiempi toteutus kattoi ne.

**Yrittikö agentti huijata?**

En huomannut. Koodissa ei ole kovakoodattuja arvoja, ja `ostos.py` ja `tuote.py` ovat ennallaan.

**Kumpi työnjako, A vai B, tuntui paremmalta?**

A tuntui paremmalta. Kun kirjoitin testit itse, tiesin tarkalleen, mitä koodin pitää tehdä, ja agentin tekemän muutoksen oli helppo tarkistaa. Osassa B agentti teki virheitä esim. kun se yhdisti kaksi askelta, jota pytest ei huomauttanut. Virheet huomasin vasta lukemalla `git diff`in ja laskemalla testien määrän.

**Muuta**

Testien määrä ja `git diff` kannattaa tarkistaa jokaisen askeleen jälkeen, koska pelkkä `passed` ei kerro, mitä agentti on muuttanut. Ohjetiedostoon piti lisätä myöhemmin sääntö `# step N` -kommenteista.
