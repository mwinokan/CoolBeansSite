ABOUT = (
    "About Cool Beans",
    """Cool Beans BV is an independent film production company, established in 2008 and headquartered in Amsterdam, the Netherlands. Cool Beans and its producers Richard Claus, Chantal Nissen and Rienkje Attoh have a proven track record of successful international co-productions with a certain preference for films with socially relevant topics and the family entertainment genre.<br><br>Together with its German sister company Comet Film and its predecessors, Cool Beans has produced more than theatrical 20 feature films in collaboration with leading companies such as Disney, New Line Cinema, Warner Bros., Fox, Sony Classics, Icon, Propaganda Films, and Sidney Kimmel Entertainment. These films have benefited from sources of public funding, such as the FFA and regional funds in Germany, the Netherlands Film Fund and the Abraham Tuschinski Fund, the Danish Film Institute, France’s CNC, Eurimages, Creative Europe, and various rebate programs in South Africa, Ireland, Germany, the Netherlands, Estonia, and Luxembourg.<br><br>Cool Beans is a member of NAPA (the Netherlands Audiovisual Producers Alliance), and its producers are members to the Dutch Academy for Film.""",
)

PRODUCTIONS = {
    "PANDA BEAR IN AFRICA": {
        "video": "https://vimeo.com/912613069",
        "text": """A fun and adventurous young Panda travels from China to Africa to rescue his best friend, Jielong the Dragon, who has been kidnapped. A fish-out of water comedy, a coming of age story.
			BEST FAMILY FILM FESTIVAL AT THE GERMAN FILMFESTIVAL IN LUDWIGSHAVEN AM RHEIN
			OFFICIAL SELECTION STUTTGART INTERNATIONAL FESTIVAL OF ANIMATED FILM
			OFFICIAL SELECTION ANNECY FESTIVAL 2024
			GOLDEN FILM AWARD (>100K ADMISSIONS NETHERLANDS)""",
        "table": {
            "YEAR / FORMAT": "2024 / 3D ANIMATION / FEATURE FILM",
            "DIRECTED BY": "RICHARD CLAUS, KARSTEN KIILERICH",
            "STORY BY": "KARSTEN KIILERICH, RICHARD CLAUS",
            "SCREENPLAY BY": "ROBERT SPRACKLING",
            "PRODUCED BY": "RICHARD CLAUS, CHANTAL NISSSEN",
            "CAST": "YOOTHA WONG-LOI-SING, GEORGINA VERBAAN, MAURITS DELCHOT, THOM HOFFMAN",
            "CO-PRODUCERS": "A. FILM (DENMARK), LE PACTE (FRANCE), COMET FILM (GERMANY)",
            "ANIMATION STUDIOS": "KATUNI, A. FILM",
            "INTERNATIONAL SALES": "CINEMA MANAGEMENT GROUP",
        },
    }
}

from site_class import Site

site = Site("Cool Beans")

site.slideshow = site.get_text_chapter(*ABOUT)
site.about = site.get_text_chapter(*ABOUT)
site.films = site.get_films_chapter(PRODUCTIONS)

site.setup_page()
site.write_html()
