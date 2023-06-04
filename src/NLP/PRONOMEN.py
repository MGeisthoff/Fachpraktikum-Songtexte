#from NLP.special_words import relativ_pronomen_derdiedas, relativ_pronomen_welche, \
 #   special_wo  	rd_form, demonstrativ_pronomen_dies, demonstrativ_pronomen_jen, \
  #  indefinit_pronomen_jed, unbestimmte_artikel, bestimmte_artikel, \
    #personal_pronomen_dritte_person, demonstrativ_pronomen_derdiedas, \
   # demonstrativ_pronomen_solch, demonstrativ_pronomen_derselb, demonstrativ_pronomen_derjenige, \
   # indefinit_pronomen_kein_artikelwort, indefinit_pronomen_irgendein_artikelwort, indefinit_pronomen_welche, \
    #indefinit_pronomen_all, indefinit_pronomen_einige, indefinit_pronomen_manch, indefinit_pronomen_irgenwelch, \
    #indefinit_pronomen_ein, indefinit_pronomen_kein_substituirend, indefinit_pronomen_irgendein_substituirt, \
    #possesiv_pronomen_ich_artikelwort, possesiv_pronomen_du_artikelwort, possesiv_pronomen_er_es_artikelwort, \
    #possesiv_pronomen_sie_artikelwort, possesiv_pronomen_wir_artikelwort, possesiv_pronomen_ihr_artikelwort, \
    #possesiv_pronomen_sie_plural_artikelwort, possesiv_pronomen_ich_attributierend, possesiv_pronomen_du_attributierend, \
    #possesiv_pronomen_er_es_attributierend, posssesiv_pronomen_sie_attributierend, \
    #posssesiv_pronomen_wir_attributierend, posssesiv_pronomen_ihr_attributierend, \
    #posssesiv_pronomen_sie_plural_attributierend, frage_pronomen_welche

def get_possible_pronomen_lists_for_tag(tag):
    pronomen_map = {
        # Artikel
        "ART": [
            unbestimmte_artikel,
            bestimmte_artikel
        ],

        # attribuierendes Demonstrativpronomen
        "PDAT": [
            demonstrativ_pronomen_derdiedas,
            demonstrativ_pronomen_solch,
            demonstrativ_pronomen_derselb,
            demonstrativ_pronomen_derjenige,
            demonstrativ_pronomen_dies,
            demonstrativ_pronomen_jen
        ],

        # substituierendes Demonstrativpronomen
        "PDS": [
            demonstrativ_pronomen_derdiedas,
            demonstrativ_pronomen_solch,
            demonstrativ_pronomen_derselb,
            demonstrativ_pronomen_derjenige,
            demonstrativ_pronomen_dies,
            demonstrativ_pronomen_jen
        ],

        # attribuierendes Indefinitpronomen
        "PIAT": [
            indefinit_pronomen_kein_artikelwort,
            indefinit_pronomen_irgendein_artikelwort,

            indefinit_pronomen_welche,
            indefinit_pronomen_all,
            indefinit_pronomen_einige,
            indefinit_pronomen_manch,
            indefinit_pronomen_irgenwelch,
            indefinit_pronomen_jed

        ],

        # substituierendes Indefinitpronomen
        "PIS": [
            # nur substituirend
            indefinit_pronomen_ein,
            indefinit_pronomen_kein_substituirend,
            indefinit_pronomen_irgendein_substituirt,

            indefinit_pronomen_welche,
            indefinit_pronomen_all,
            indefinit_pronomen_einige,
            indefinit_pronomen_manch,
            indefinit_pronomen_irgenwelch,
            indefinit_pronomen_jed
        ],

        # (nicht-reflexives) Personalpronomen
        "PPER": [
            personal_pronomen_dritte_person,

        ],

        # attribuierendes Possessivpronomen
        "PPOSAT": [
            possesiv_pronomen_ich_artikelwort,
            possesiv_pronomen_du_artikelwort,
            possesiv_pronomen_er_es_artikelwort,
            possesiv_pronomen_sie_artikelwort,
            possesiv_pronomen_wir_artikelwort,
            possesiv_pronomen_ihr_artikelwort,
            possesiv_pronomen_sie_plural_artikelwort
        ],

        # substituierendes Possessivpronomen
        "PPOSS": [
            possesiv_pronomen_ich_attributierend,
            possesiv_pronomen_du_attributierend,
            possesiv_pronomen_er_es_attributierend,
            posssesiv_pronomen_sie_attributierend,
            posssesiv_pronomen_wir_attributierend,
            posssesiv_pronomen_ihr_attributierend,
            posssesiv_pronomen_sie_plural_attributierend
        ],

        # substituierendes Relativpronomen
        "PRELS": [
            relativ_pronomen_derdiedas,
            relativ_pronomen_welche,



        ],

        # attribuierendes Relativpronomen
        "PRELAT": [
            relativ_pronomen_derdiedas,
            relativ_pronomen_welche,

        ],

        # Reflexivpronomen
        "PRF": [
            #??
        ],

        # substituierendes Interrogativpronomen
        "PWS": [
            frage_pronomen_welche
        ],

        # attribuierendes Interrogativpronomen
        "PWAT": [
            frage_pronomen_welche
        ],

        # adverbiales Interrogativpronomen
        "PWAV": [
            frage_pronomen_welche
        ]

    }

    return pronomen_map[tag]