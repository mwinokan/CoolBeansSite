#!/usr/bin/env python3

import mrich
from movie import Movie


def main():

    # movies = make_movie_data()

    cool_beans()
    # katuni(movies)

    add_changes()


def cool_beans():

    title = "Cool Beans"

    print(f"site({title})")

    contact = """Richard: <a href="mailto:rc@coolbeanspix.com">rc@coolbeanspix.com</a><br>
Chantal: <a href="mailto:cn@coolbeanspix.com">cn@coolbeanspix.com</a><br>
Rienkje: <a href="mailto:ra@coolbeanspix.com">ra@coolbeanspix.com</a>
"""
    address = "Haarlemmerweg 319-C<br>1051 LG, Amsterdam<br>Nederland"

    accent_color1 = "blue"
    accent_color2 = "lime"
    accent_color3 = "red"

    accent_contrast1 = "white"
    accent_contrast2 = "black"
    accent_contrast3 = "white"

    logo_url = "assets/cool_beans_logo.png"

    from cool_beans import ABOUT, MOVIES, TEXT_SECTIONS, IMDB_LINKS

    TEXT_SECTIONS["Producers"] = TEXT_SECTIONS["Producers"].replace(
        "Richard Claus",
        '<a href="https://www.imdb.com/name/nm0165290" style="text-decoration: none;">Richard Claus</a>',
    )
    TEXT_SECTIONS["Producers"] = TEXT_SECTIONS["Producers"].replace(
        "Chantal Nissen",
        '<a href="https://www.imdb.com/name/nm3900212" style="text-decoration: none;">Chantal Nissen</a>',
    )
    TEXT_SECTIONS["Producers"] = TEXT_SECTIONS["Producers"].replace(
        "Rienkje Attoh",
        '<a href="https://www.imdb.com/name/nm6973555" style="text-decoration: none;">Rienkje Attoh</a>',
    )
    TEXT_SECTIONS["Producers"] = TEXT_SECTIONS["Producers"].replace(
        "RICHARD CLAUS",
        '<a href="https://www.imdb.com/name/nm0165290" style="text-decoration: none;">RICHARD CLAUS</a>',
    )
    TEXT_SECTIONS["Producers"] = TEXT_SECTIONS["Producers"].replace(
        "CHANTAL NISSEN",
        '<a href="https://www.imdb.com/name/nm3900212" style="text-decoration: none;">CHANTAL NISSEN</a>',
    )
    TEXT_SECTIONS["Producers"] = TEXT_SECTIONS["Producers"].replace(
        "RIENKJE ATTOH",
        '<a href="https://www.imdb.com/name/nm6973555" style="text-decoration: none;">RIENKJE ATTOH</a>',
    )

    movies = MOVIES

    # text_buffer = 'Cool Beans BV is run by producers Richard Claus and Chantal Nissen, the Amsterdam animation outfit Katuni and the German Comet Film are its sister companies.</p><p>All of Cool Beans productions are international co-productions, including <i>Black Butterflies</i>, <i>The Price of Sugar</i>, <i>An Act of Defiance</i> and the recent 3D animated films <i>The Little Vampire 3D</i> (2017) in co-production with A. Film (Denmark) and <i>Ainbo</i> (2020) in co-production with Tunche Films (Peru).</p><p>The next 3D animated film coming from Cool Beans and Katuni is <i>Panda Bear in Africa</i>, which is set to start animation end of 2021. Le Pacte (France) joined the successful Dutch/German/Danish team that produced <i>The Little Vampire 3D</i> as the French co-producer in 2019, and sales agent CMG – Cinema Management Group has already sold an astonishing number of territories. There is still room for co-producers, animation studios and other partners to come on board.</p><p>Cool Beans’ development slate also includes new live action films, among others the Dutch “multiculti” comedy <i>Matties</i> and the historic drama <i>Tutuba</i>; the series <i>Panama Panic</i> and the animated series <i>The Little Vampire</i>.'
    text_buffer = ABOUT

    html_buffer = create_site(
        address,
        accent_color1,
        accent_color2,
        accent_color3,
        accent_contrast1,
        accent_contrast2,
        accent_contrast3,
        contact,
        logo_url,
        title,
        text_buffer,
        movies,
        link_lookup=IMDB_LINKS,
        text_sections=TEXT_SECTIONS,
    )

    write_buffer(html_buffer)


def create_site(
    address,
    accent_color1,
    accent_color2,
    accent_color3,
    accent_contrast1,
    accent_contrast2,
    accent_contrast3,
    contact,
    logo_url,
    title,
    text_buffer,
    movies,
    max_width=4000,
    slideshow_auto=False,
    slideshow_rate=5,
    text_sections=None,
    link_lookup=None,
):

    navigation_targets = {
        "about": f"ABOUT {title.upper()}",
        "productions": "Productions",
    }

    if text_sections:
        new_sections = {}
        for section_title, content in text_sections.items():
            safe_title = section_title.replace(" ", "_").replace("&", "and").lower()
            navigation_targets[safe_title] = section_title
            new_sections[safe_title] = (section_title, content)

    mrich.print(navigation_targets)

    # preamble
    html_buffer = "<!DOCTYPE html>"
    html_buffer += "<html>\n"
    html_buffer += "<head>\n"
    html_buffer += f"<title>{title}</title>\n"
    html_buffer += '<meta charset="UTF-8">\n'
    html_buffer += (
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
    )
    html_buffer += (
        '<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">\n'
    )
    html_buffer += '<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Oswald">\n'
    html_buffer += '<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Open Sans">\n'
    html_buffer += '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">\n'
    html_buffer += '<link rel="stylesheet" href="style.css">\n'

    # styling
    html_buffer += "<style>\n"
    html_buffer += (
        'h1,h2,h3,h4,h5,h6 {font-family: "Oswald"}body {font-family: "Open Sans"}\n'
    )
    html_buffer += ".mySlides {display:none}\n"
    html_buffer += ".w3-left, .w3-right, .w3-badge {cursor:pointer}\n"
    html_buffer += ".w3-badge {height:13px;width:13px;padding:0}\n"

    html_buffer += "@media screen and (max-width: 800px) { .hide-if-narrow { display: none !important; } }"
    html_buffer += "@media screen and (min-width: 801px) { .hide-if-wide { display: none !important; } }"
    html_buffer += "@media screen and (max-width: 800px) { .show-if-narrow { display: block !important; } }"
    html_buffer += "@media screen and (min-width: 801px) { .show-if-wide { display: block !important; } }"
    html_buffer += "@media screen and (min-width: 801px) { .margin-if-wide { margin-left:220px !important; } }"

    html_buffer += "</style>\n"
    html_buffer += "</head>\n"

    # begin body
    html_buffer += "<body>\n"
    html_buffer += f'<div class="w3-content" style="max-width:{max_width}px">\n'

    # top bar (one dynamic and one static)
    html_buffer += "<header>\n"
    html_buffer += '<div class="w3-top">\n'
    html_buffer += '<div class="w3-bar w3-center w3-padding-large" style="background-color:white">\n'
    # html_buffer += '<div class="w3-bar-item">\n'
    html_buffer += (
        f'<img src="{logo_url}" alt="{title} Logo" style="width:40%;max-width:200px">\n'
    )
    # html_buffer += '</div>\n'
    html_buffer += '<div class="w3-display-left w3-container">'

    # Navigation dropdown
    html_buffer += '<div class="w3-dropdown-hover">\n'
    html_buffer += '<button class="w3-xlarge w3-btn w3-white">&#9776;\n'
    html_buffer += "</button>\n"
    html_buffer += f'<div id="demo" class="w3-dropdown-content w3-bar-block w3-card-4" style="background-color:{accent_color3};color:{accent_contrast3};border-radius:5px;">\n'

    for target, text in navigation_targets.items():
        html_buffer += f'<a href="#{target}" class="w3-bar-item w3-button" style="border-radius:5px;">{text.upper()}</a>\n'

    html_buffer += "</div>\n"
    html_buffer += "</div>\n"
    html_buffer += "</div>\n"

    html_buffer += "</div>\n"
    html_buffer += "</div>\n"
    html_buffer += "</header>\n"

    # DYNAMIC
    html_buffer += '<div class="w3-bar w3-center w3-padding w3-white">\n'
    html_buffer += (
        f'<img src="{logo_url}" alt="{title} Logo" style="width:40%;max-width:200px">\n'
    )

    html_buffer += "</div>\n"

    # # sidebar
    # html_buffer += '<div class="w3-sidebar w3-bar-block hide-if-narrow" style="width:200px;background:none;margin-top:80px;">\n'
    # for target, text in navigation_targets.items():
    #     html_buffer += f'<a href="#{target}" class="w3-bar-item w3-button" style="background-color: rgba(255, 255, 255, 0.5)">{text.upper()}</a>\n'
    # html_buffer += '</div>\n'

    ### screencap slideshow

    subset = [d for d in movies if d.has_screencap]
    print(f"#movies w/ screencap_url = {len(subset)}")
    assert len(subset) > 1

    # screencap slideshow
    # html_buffer += f'<div class="w3-content w3-display-container w3-dark-grey" style="width:100%;max-width:{max_width}px">\n'
    html_buffer += f'<div class="w3-content w3-display-container w3-dark-grey" style="width:100%;max-width:{max_width}px">\n'

    for d in subset:
        # html_buffer += '<div class="w3-display-container mySlides w3-center" style="width:100%;max-height:800px"> \n'
        html_buffer += '<div class="w3-display-container mySlides w3-center" style="width:100%;max-height:1200px"> \n'
        # html_buffer += f'<img src="{d.screencap_url}" onclick="document.getElementById(\'{d.name}_modal\').style.display=\'block\'" style="object-fit:contain;background-color:white;width:100%;max-height:800px">\n'
        html_buffer += f'<img src="{d.screencap_url}" onclick="document.getElementById(\'{d.name}_modal\').style.display=\'block\'" style="object-fit:contain;background-color:white;width:100%;max-height:1200px">\n'
        # html_buffer += f'<div class="w3-padding w3-display-bottomleft w3-text-white"><h3>{d.title}</h3></div>\n'
        html_buffer += f"<div class=\"overlay overlay-round-box w3-button\" onclick=\"document.getElementById('{d.name}_modal').style.display='block'\"><h4>{d.title}</h4></div>\n"
        html_buffer += "</div>\n"

        # html_buffer += '<div class="image-container mySlides">\n'
        # html_buffer += f'<img src="{d.screencap_url}" alt="Image" class="responsive-image">\n'
        # html_buffer += f'<div class="overlay"><h3>{d.title}</h3></div>\n'
        # html_buffer += '</div>\n'

        # html_buffer += '<div class="w3-display-container mySlides w3-center" style="width:100%;max-height:800px;width:100%;object-fit:contain"> \n'
        # html_buffer += f'<img src="{d.screencap_url}" style="object-fit:contain;background-color:white">\n'
        # html_buffer += f'<div class="w3-padding w3-display-bottomleft w3-text-white"><h3>{d.title}</h3></div>\n'
        # html_buffer += "</div>\n"

        # html_buffer += f'<img src="{d.screencap_url}" style="width:100%;max-height:800px;object-fit: contain;background-color:white;">\n'
        # html_buffer += f'<div class="w3-padding w3-display-bottomleft w3-text-white"><h3>{d.title}</h3></div>\n'
        # html_buffer += f'<img src="{d.screencap_url}" style="width:100%">\n'
        # html_buffer += f'<div class="w3-padding w3-display-bottommiddle w3-text-white"><h3>{d.title}</h3></div>\n'
        # html_buffer += "</div>\n"

    if not slideshow_auto:
        # arrow buttons
        html_buffer += '<div class="w3-center w3-container w3-section w3-large w3-text-white w3-display-middle" style="width:100%">\n'
        html_buffer += '<div class="w3-left overlay-round-box" style="left:20px" onclick="plusDivs(-1)">&#10094;</div>\n'
        html_buffer += '<div class="w3-right overlay-round-box" style="right:20px" onclick="plusDivs(1)">&#10095;</div>\n'
        html_buffer += "</div>\n"

    html_buffer += "</div>\n"

    if not slideshow_auto:
        # slideshow scripting (manual)
        html_buffer += "<script>\n"

        html_buffer += "function getRandomInt(max) {\n"
        html_buffer += "  return Math.floor(Math.random() * max);\n"
        html_buffer += "}\n"
        # html_buffer += 'var slideIndex = 1;\n'
        html_buffer += f"var slideIndex = getRandomInt({len(subset)});\n"
        html_buffer += "showDivs(slideIndex);\n"
        html_buffer += "function plusDivs(n) {\n"
        html_buffer += "  showDivs(slideIndex += n);\n"
        html_buffer += "}\n"
        html_buffer += "function currentDiv(n) {\n"
        html_buffer += "  showDivs(slideIndex = n);\n"
        html_buffer += "}\n"
        html_buffer += "function showDivs(n) {\n"
        html_buffer += "  var i;\n"
        html_buffer += '  var x = document.getElementsByClassName("mySlides");\n'
        html_buffer += '  var dots = document.getElementsByClassName("demo");\n'
        html_buffer += "  if (n > x.length) {slideIndex = 1}\n"
        html_buffer += "  if (n < 1) {slideIndex = x.length}\n"
        html_buffer += "  for (i = 0; i < x.length; i++) {\n"
        html_buffer += '    x[i].style.display = "none";  \n'
        html_buffer += "  }\n"
        html_buffer += "  for (i = 0; i < dots.length; i++) {\n"
        html_buffer += (
            '    dots[i].className = dots[i].className.replace(" w3-white", "");\n'
        )
        html_buffer += "  }\n"
        html_buffer += '  x[slideIndex-1].style.display = "block";  \n'
        html_buffer += '  dots[slideIndex-1].className += " w3-white";\n'
        html_buffer += "}\n"
        html_buffer += "</script>\n"
    else:
        # slideshow scripting (auto)
        html_buffer += "<script>\n"
        html_buffer += "var myIndex = 0;\n"
        html_buffer += "carousel();\n"
        html_buffer += "function carousel() {\n"
        html_buffer += "  var i;\n"
        html_buffer += '  var x = document.getElementsByClassName("mySlides");\n'
        html_buffer += "  for (i = 0; i < x.length; i++) {\n"
        html_buffer += '    x[i].style.display = "none";  \n'
        html_buffer += "  }\n"
        html_buffer += "  myIndex++;\n"
        html_buffer += "  if (myIndex > x.length) {myIndex = 1}    \n"
        html_buffer += '  x[myIndex-1].style.display = "block";  \n'
        html_buffer += f"  setTimeout(carousel, {slideshow_rate}000);\n"
        html_buffer += "}\n"
        html_buffer += "</script>\n"

    # html_buffer += '<h1 class="hide-if-narrow">TEST WIDE</h1>'
    # html_buffer += '<h1 class="hide-if-wide">TEST NARROW</h1>'

    # sidebar
    # html_buffer += '<div class="w3-sidebar w3-bar-block hide-if-narrow sidebar" style="width:200px;margin-top:80px;">\n'
    html_buffer += '<div class="w3-bar-block hide-if-narrow sidebar locked-bottom-left" style="width:200px;margin-top:80px;">\n'
    for target, text in navigation_targets.items():
        html_buffer += f'<a href="#{target}" class="w3-bar-item w3-button" style="background:none;border-radius: 5px;">{text.upper()}</a>\n'
    html_buffer += "</div>\n"

    # whole page content
    html_buffer += '<div class="margin-if-wide">\n'

    # text content
    html_buffer += '<div class="w3-content" style="max-width:800px">\n'
    html_buffer += '<div class="w3-container w3-padding-large">\n'
    html_buffer += '<div id="about" style="height: 100px; margin-top: -100px;"></div>'  ## offset hyperlink target
    # html_buffer += f'<h2 style="margin-left:200px">About {title}</h2>\n'
    html_buffer += f"<h2>ABOUT {title.upper()}</h2>\n"
    html_buffer += "<p>\n"

    html_buffer += text_buffer

    html_buffer += "</p>    \n"
    html_buffer += "</div>\n"
    html_buffer += "</div>\n"

    # headshots
    html_buffer += '<div class="w3-content" style="max-width:600px">\n'
    html_buffer += '<div class="w3-cell-row">\n'
    html_buffer += '<div class="w3-container w3-cell w3-center">\n'
    html_buffer += '<img src="assets/Richard_Claus_1.jpg" alt="Richard_Claus_1" style="width:100%;max-width:200px" class="w3-padding">\n'
    html_buffer += '<h4 style="color:black">Richard Claus</h4>\n'
    # html_buffer += '<p>+31 (0) 650281410\n'
    html_buffer += "<p>rc@coolbeanspix.com</p>\n"
    html_buffer += "</div>\n"
    html_buffer += '<div class="w3-container w3-cell w3-center">\n'
    # html_buffer += '<img src="assets/Chantal_Nissen.jpg" alt="Chantal_Nissen" style="width:100%;max-width:200px" class="w3-padding">\n'
    html_buffer += '<img src="assets/chantal.jpg" alt="Chantal_Nissen" style="width:100%;max-width:200px" class="w3-padding">\n'
    html_buffer += '<h4 style="color:black">Chantal Nissen</h4>\n'
    html_buffer += "<p>cn@coolbeanspix.com</p>\n"
    html_buffer += "</div>\n"
    html_buffer += '<div class="w3-container w3-cell w3-center">\n'
    html_buffer += '<img src="assets/rienkje.jpg" alt="Rienkje Attoh" style="width:100%;max-width:200px" class="w3-padding">\n'
    html_buffer += '<h4 style="color:black">Rienkje Attoh</h4>\n'
    html_buffer += "<p>ra@coolbeanspix.com</p>\n"
    html_buffer += "</div>\n"
    html_buffer += "</div>\n"
    html_buffer += "</div>\n"

    # next section heading
    # html_buffer += f'<div class="w3-content w3-topbar w3-center" style="max-width:{max_width}px">\n'
    html_buffer += "<br>\n"
    html_buffer += "<br>\n"
    html_buffer += f'<div class="w3-content w3-center w3-text-white w3-padding-large" style="max-width:{max_width}px;background-color:{accent_color1};margin-left:-220px">\n'
    html_buffer += '<div id="productions" style="height: 100px; margin-top: -100px"></div>'  ## offset hyperlink target
    # html_buffer += '<h2 style="margin-left:200px">Productions</h2>\n'
    html_buffer += "<h2>PRODUCTIONS</h2>\n"
    html_buffer += "</div>\n"
    html_buffer += "<br>\n"

    # poster grid
    html_buffer += (
        # f'<div class="w3-content w3-padding-large" style="max-width:1200px">\n'
        f'<div class="w3-content w3-padding-large">\n'
    )
    html_buffer += '<div class="w3-container">\n'

    subset = [d for d in movies if d.has_poster]
    print(f"#movies w/ poster_url = {len(subset)}")
    assert len(subset) > 0

    names = set()

    start = 0
    end = len(subset)
    step = 3
    for i in range(start, end, step):
        x = i
        chunk = subset[x : x + step]

        html_buffer += '<br><div class="w3-row">\n'

        for d in chunk:
            html_buffer += f'<div class="w3-col l4 m12 s12 w3-padding-large" style="padding-left:0px;padding-right:0px">\n'

            # movie poster
            if d.trailer_url:
                html_buffer += f'<img class="w3-card-4 w3-hover-opacity" onclick="document.getElementById(\'{d.name}_modal\').style.display=\'block\'" src="{d.poster_url}" alt="{d.title} Poster" style="width:100%"></a>\n'
            else:
                html_buffer += f'<a href="{d.target_url}"><img class="w3-card-4 w3-hover-opacity" src="{d.poster_url}" alt="{d.title} Poster" style="width:100%"></a>\n'

            # info panel
            html_buffer += f'<div class="w3-container">\n'
            html_buffer += f"<h2>{d.title}</h2>\n"

            html_buffer += f"<p>{d.description}\n"
            # if d.more_data:
            # html_buffer += f'<i id="show_{d.name}" class="fa fa-plus" style="color:{accent_color1}" onclick="showDetail(\'{d.name}\')"></i>\n'
            html_buffer += "</p>\n"

            awards_table = ""
            if d.awards:
                # awards_table += "<table>\n"
                awards_table += '<table style="border-spacing: 10px 0">\n'

                for text in d.awards:
                    awards_table += "<tr>\n"
                    awards_table += "<td>\n"
                    awards_table += "<strong>\n"
                    awards_table += text
                    awards_table += "</stong>\n"
                    awards_table += "</td>\n"
                    awards_table += "</tr>\n"
                awards_table += "</table>\n"

            # html_buffer += awards_table

            # more info panel
            if d.more_data:
                # html_buffer += f'<div id="{d.name}_detail" style="display:none">\n'

                more_buffer = ""

                if isinstance(d.more_data, dict):
                    more_buffer += (
                        # '<table class="w3-table" style="border-spacing: 10px 0">\n'
                        '<table style="border-spacing: 10px 0">\n'
                    )
                    for cells in d.more_data.items():
                        more_buffer += "<tr>\n"

                        # if cells[0] in [
                        #     "DIRECTED BY",
                        #     "STORY BY",
                        #     "SCREENPLAY BY",
                        #     "PRODUCED BY",
                        #     "CAST",
                        # ]:
                        #     for name in cells[1].split(", "):
                        #         names.add(name)

                        for i, cell in enumerate(cells):
                            more_buffer += "<td>\n"
                            if i == 0:
                                more_buffer += "<strong>\n"

                            if i == 1:
                                cell = add_links(cell, link_lookup)

                            more_buffer += cell
                            if i == 0:
                                more_buffer += "</strong>\n"
                            more_buffer += "</td>\n"
                        more_buffer += "</tr>\n"
                    more_buffer += "</table>\n"
                    # html_buffer += more_buffer

                # else:
                # more_buffer = f"<p>{d.more_data}\n"
                # html_buffer += f"<p>{d.more_data}\n"
                # html_buffer += "</p>\n"

                # html_buffer += f'<i class="fa fa-close" style="color:{accent_color1}" onclick="hideDetail(\'{d.name}\')"></i>\n'
                # html_buffer += "</div>\n"

            # html_buffer += f'<div class="w3-center">\n'
            # if d.imdb_url:
            # html_buffer += f'<a href="{d.imdb_url}" class="w3-btn w3-hover-opacity w3-text-white" style="background-color:{accent_color1};"><strong>IMDb</strong></a>\n'
            # if d.trailer_url:
            # html_buffer += f'<button class="w3-btn w3-hover-opacity w3-text-white" onclick="document.getElementById(\'{d.name}_modal\').style.display=\'block\'" style="background-color:{accent_color1};"><strong>Trailer</strong></button>'
            # html_buffer += f'<a href="{d.trailer_url}" class="w3-btn w3-hover-opacity w3-text-white" style="background-color:{accent_color1};"><strong>Trailer</strong></a>\n'
            # html_buffer += "</div>\n"
            html_buffer += "</div>\n"
            html_buffer += "</div>\n"

            # modal
            if d.trailer_url:
                # html_buffer += f'<div id="{d.name}_modal" class="w3-modal" onclick="document.getElementById({d.name}_modal).style.display=\'none\'">\n'
                html_buffer += f'<div id="{d.name}_modal" class="w3-modal" onclick="document.getElementById(\'{d.name}_modal\').style.display=\'none\'">\n'
                html_buffer += '<div class="w3-modal-content">\n'
                html_buffer += '<div class="w3-container">\n'
                html_buffer += f"<span onclick=\"document.getElementById('{d.name}_modal').style.display='none'\" class=\"w3-button w3-display-topright\">&times;</span>\n"

                html_buffer += f"<h2>{d.title}</h2>\n"

                html_buffer += f'<iframe width="100%" height="500" src="{d.embed_url}" '
                # html_buffer += f'<iframe width="560" height="315" src="{d.embed_url}" '

                html_buffer += 'title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; '
                html_buffer += 'encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>\n'

                html_buffer += f"<p>{d.description}</p>\n"

                html_buffer += awards_table
                html_buffer += "<br>\n"

                if d.more_data:
                    html_buffer += more_buffer
                if d.imdb_url:
                    html_buffer += f'<a href="{d.imdb_url}" class="w3-btn w3-hover-opacity w3-text-white" style="background-color:{accent_color1};margin-left:-220px;"><strong>IMDb</strong></a>\n'
                html_buffer += "<br><br>\n"
                html_buffer += "</div>\n"
                html_buffer += "</div>\n"
                html_buffer += "</div>\n"

        html_buffer += "</div>\n"

    # print(names)

    html_buffer += "</div>\n"
    html_buffer += "</div>\n"

    html_buffer += "<script>\n"
    html_buffer += """
                    function showDetail(ID) {
                        document.getElementById(ID+"_detail").style.display = "block";
                        document.getElementById("show_"+ID).style.display = "none";
                    }
                    function hideDetail(ID) {
                        document.getElementById(ID+"_detail").style.display = "none";
                        document.getElementById("show_"+ID).style.display = "inline";
                    }
                    """
    html_buffer += "</script>\n"

    if text_sections:

        for safe_title, (section_title, content) in new_sections.items():

            html_buffer += "<br>\n"
            html_buffer += "<br>\n"
            html_buffer += f'<div class="w3-content w3-center w3-text-white w3-padding-large" style="max-width:{max_width}px;background-color:{accent_color1};margin-left:-220px">\n'
            html_buffer += f'<div id="{safe_title}" style="height: 100px; margin-top: -100px;"></div>'  ## offset hyperlink target
            # html_buffer += f'<h2 style="margin-left:200px">{section_title}</h2>\n'
            html_buffer += f"<h2>{section_title.upper()}</h2>\n"
            html_buffer += "</div>\n"
            html_buffer += "<br>\n"

            html_buffer += f'<div class="w3-content w3-padding-large" style="max-width:800px">{content}</div>\n'

    # end body
    html_buffer += "</div>\n"
    html_buffer += "</body>\n"

    # footer
    html_buffer += f'<footer class="w3-container" style="padding:32px;background-color:{accent_color1}">\n'

    # html_buffer += '<div class="margin-if-wide">\n'

    # html_buffer += f'<div class="w3-content w3-center w3-text-white w3-padding-large" style="max-width:{max_width}px;background-color:{accent_color1}">\n'
    html_buffer += f'<div class="w3-content w3-text-white w3-padding-large" style="max-width:800px">\n'
    # html_buffer += '<div class="w3-center w3-text-white">\n'

    html_buffer += '<table class="w3-table">\n'
    html_buffer += "<tr>\n"

    html_buffer += '<td style="text-align:center;vertical-align:middle">\n'
    html_buffer += (
        f'<p style="color:{accent_color2}"><strong>COOL BEANS BV</strong></p>\n'
    )
    html_buffer += f"<p>{address}</p>\n"
    html_buffer += f"<p>{contact}</p>\n"
    html_buffer += f'<a href="#" class="w3-button w3-padding w3-margin-bottom" style="background-color:{accent_color1};color:{accent_color3}"><i class="fa fa-arrow-up w3-margin-right"></i>Back to top</a>\n'
    html_buffer += "</td>\n"

    html_buffer += '<td style="text-align:center;vertical-align:middle">\n'
    html_buffer += f'<img src="assets/EU flag-Crea EU + MEDIA_neg [White] EN.png" alt="Creative Europe Logo" style="width:100%;max-width:200px">\n'
    # html_buffer += f'<img src="assets/EU flag-Crea EU + MEDIA_neg EN.png" alt="Creative Europe Logo" style="width:100%;max-width:200px">\n'
    html_buffer += "<br>\n"
    html_buffer += "<br>\n"
    html_buffer += "</td>\n"

    html_buffer += "</tr>\n"
    html_buffer += "</table>\n"

    # html_buffer += "</div>\n"
    html_buffer += "</div>\n"
    html_buffer += "</footer>\n"
    html_buffer += "</html>\n"

    return html_buffer


def write_buffer(html_buffer, subdir=None):
    # write buffer
    if subdir:
        f = open(f"{subdir}/index.html", "wt")
    else:
        f = open("index.html", "wt")
    f.write(html_buffer)


def push_changes():
    print(f"push_changes()")
    import os

    os.system(
        f'git add *.py assets/* */index.html; git commit -m "auto-generated"; git push'
    )


def add_changes():
    print(f"add_changes()")
    import os

    os.system(f"git add *.py assets/* index.html style.css")


def add_links(text, lookup):
    for name in lookup:
        if name in text:
            link = lookup[name]
            text = text.replace(name, f'<a href="{link}">{name}</a>')
    return text


if __name__ == "__main__":
    main()
