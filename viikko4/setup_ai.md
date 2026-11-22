# Testien siistiminen setUp-metodiin

**Poistiko agentti toisteisuuden järkevästi?**
Kyllä. Mockit ja `Kauppa`-olio luodaan nyt kerran `setUp`-metodissa, joten testit ovat lyhyempiä ja luettavampia.

**Muuttiko agentti testien toiminnallisuutta?**
Ei. Kaikki testit ja `assert_called_with`-tarkistukset ovat ennallaan. Testit, jotka tarvitsevat eri tuotteita, määrittelevät varaston toteutuksen itse.

**Jouduinko korjaamaan agentin muutoksia?**
En. Muutokset toimivat sellaisenaan ja testit menivät läpi.
