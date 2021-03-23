import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_uuden_varaston_tilavuus_ei_voi_olla_negatiivinen(self):
        tyhja_varasto = Varasto(-10)

        self.assertAlmostEqual(tyhja_varasto.tilavuus, 0)

    def test_alkusaldo_ei_voi_olla_negatiivinen(self):
        varasto2 = Varasto(10, -10)

        self.assertAlmostEqual(varasto2.saldo, 0)
    
    def test_uusi_varasto_tayttyy_oikein(self):
        varasto2 = Varasto(10, 10)

        self.assertAlmostEqual(varasto2.saldo, 10)

    def test_uusi_varasto_ei_voi_ylitayttya(self):
        varasto2 = Varasto(10, 100)

        self.assertAlmostEqual(varasto2.saldo, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_ei_ylita_saldoa(self):
        self.varasto.lisaa_varastoon(50)

        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_varastoon_ei_voi_lisata_negatiivista_maaraa(self):
        self.varasto.lisaa_varastoon(-10)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_varastosta_voi_ottaa_korkeintaan_saldon_verran(self):
        self.varasto.lisaa_varastoon(5)

        saatu_maara = self.varasto.ota_varastosta(10)

        self.assertAlmostEqual(saatu_maara, 5)

    def test_varastosta_ei_voi_ottaa_negatiivista_maaraa(self):
        self.varasto.lisaa_varastoon(10)
        self.varasto.ota_varastosta(-10)

        self.assertAlmostEqual(self.varasto.saldo, 10)
    
    def test_varasto_tulostuu_oikein(self):
        self.assertEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")

