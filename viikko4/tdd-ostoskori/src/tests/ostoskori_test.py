import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    # step 1
    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    # step 2
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.hinta(), 3)

    # step 3
    def test_yhden_tuotteen_lisaamisen_jalkeen_korin_hinta_on_tuotteen_hinta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.hinta(), 3)

    # step 4
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        self.kori.lisaa_tuote(Tuote("Maito", 3))
        self.kori.lisaa_tuote(Tuote("Juusto", 5))

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    # step 5
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_hinta_on_summa(self):
        self.kori.lisaa_tuote(Tuote("Maito", 3))
        self.kori.lisaa_tuote(Tuote("Juusto", 5))

        self.assertEqual(self.kori.hinta(), 8)

    # step 6
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    # step 7
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_hinta_on_kaksi_kertaa_hinta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.hinta(), 6)

    # step 8
    def test_yhden_tuotteen_lisaamisen_jalkeen_ostoksia_yksi(self):
        self.kori.lisaa_tuote(Tuote("Maito", 3))

        self.assertEqual(len(self.kori.ostokset()), 1)

    # step 9
    def test_yhden_tuotteen_lisaamisen_jalkeen_ostos_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.ostokset()[0].tuotteen_nimi(), maito.nimi())
        self.assertEqual(self.kori.ostokset()[0].lukumaara(), 1)

    # step 10
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoksia_kaksi(self):
        self.kori.lisaa_tuote(Tuote("Maito", 3))
        self.kori.lisaa_tuote(Tuote("Juusto", 5))

        self.assertEqual(len(self.kori.ostokset()), 2)

    # step 11
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostos_yksi(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(len(self.kori.ostokset()), 1)