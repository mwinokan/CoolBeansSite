from html import escape
import mrich
from pathlib import Path


class Site:

    def __init__(self, title, output_dir="."):

        self.title = title
        self.output_dir = Path(".")
        self.content = []

        # self.setup_page()
        # self.write_html()

    def setup_page(self):
        """Create the yattag page content"""

        # yattag setup
        from yattag import Doc

        doc, tag, text, line = Doc().ttl()

        self.doc = doc
        self.tag = tag
        self.text = text
        self.line = line

        self.doc.asis("<!DOCTYPE html>")

        with self.tag("html"):

            self.header()

            with self.tag("body", klass="w3-content", style="max-width:none"):

                with self.tag("div", klass="w3-bar w3-teal"):
                    with self.tag("div", klass="w3-bar-item"):
                        src = "https://github.com/mwinokan/HIPPO/raw/main/logos/hippo_assets-02.png?raw=true"
                        self.doc.stag(
                            "img", src=src, style="max-height:75px"
                        )  # , klass="w3-image")

                    with self.tag("div", klass="w3-bar-item"):
                        with self.tag("h1"):
                            self.text(self.title)

                if hasattr(self, "slideshow"):
                    self.slideshow()
                if hasattr(self, "about"):
                    self.about()
                if hasattr(self, "films"):
                    self.films()

                # self.get_content()

            self.footer()

            # with self.tag("div", klass="w3-container w3-dark-gray w3-padding"):
            #     self.section(self.sec_targets)
            #     self.section(self.sec_hits)

            # # placeholders
            # if self.scaffolds:
            #     self.section(self.sec_scaffolds)
            # if self.scaffolds:
            #     self.section(self.sec_elaborations)
            # if self.quoting: self.section(self.sec_quoting)
            # if self.product_pool: self.section(self.sec_product_pool)
            # if self.route_pool: self.section(self.sec_route_pool)
            # if self.rgen:
            #     self.section(self.sec_rgen)
            # if self.scorer:
            #     self.section(self.sec_scorer)
            # if self.proposals:
            #     self.section(self.sec_proposals)

    def footer(self):
        with self.tag("div", klass="w3-container w3-teal w3-padding"):
            with self.tag("div", klass="w3-center"):
                src = "https://github.com/mwinokan/HIPPO/raw/main/logos/hippo_logo_tightcrop.png?raw=true"
                self.doc.stag("img", src=src, style="max-height:150px")

    def write_html(self) -> None:
        """Write the index.html file"""

        from yattag import indent

        path = self.index_path

        with open(path, "wt") as f:
            mrich.writing(path)
            f.writelines(indent(self.doc.getvalue()))

    def header(self) -> None:
        """Create the page header"""

        with self.tag("head"):

            with self.tag("title"):
                self.text(self.title)

            self.doc.stag("meta", charset="UTF-8")
            self.doc.stag(
                "meta", name="viewport", content="width=device-width, initial-scale=1"
            )
            self.doc.stag(
                "link",
                rel="stylesheet",
                href="https://www.w3schools.com/w3css/4/w3.css",
            )
            self.doc.stag(
                "link",
                rel="stylesheet",
                href="https://fonts.googleapis.com/css?family=Oswald",
            )
            self.doc.stag(
                "link",
                rel="stylesheet",
                href="https://fonts.googleapis.com/css?family=Open Sans",
            )
            self.doc.stag(
                "link",
                rel="stylesheet",
                href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css",
            )

            # with self.tag("script", src="https://cdn.plot.ly/plotly-latest.min.js"):
            #     ...

            # with self.tag("script", src="https://3Dmol.org/build/3Dmol-min.js"):
            #     ...

            # with self.tag("script", src="https://3Dmol.org/build/3Dmol.ui-min.js"):
            #     ...

            self.style()

    def style(self) -> None:
        """Create the page style"""

        # change to a .css file and use doc.stag("link", rel="stylesheet", href="style.css")

        with self.tag("style"):
            self.doc.asis(
                """h1,h2,h3,h4,h5,h6 {font-family: "Oswald"}body {font-family: "Open Sans"}"""
            )
            self.doc.asis(""".mySlides {display:none}\n""")
            self.doc.asis(""".w3-left, .w3-right, .w3-badge {cursor:pointer}\n""")
            self.doc.asis(""".w3-badge {height:13px;width:13px;padding:0}\n""")

    @property
    def index_path(self) -> "Path":
        """index.html Path"""
        return self.output_dir / "index.html"

    # def get_content(self):
    #     for function in self.content:
    #         function()

    def get_text_chapter(self, title, text):

        def text_content():
            with self.tag("h1"):
                self.doc.asis(title)
            for t in text.split("\n"):
                with self.tag("p"):
                    self.doc.asis(t.strip())

        return text_content

        # self.content.append(text_content)

    def get_films_chapter(self, data):

        def film_content():
            for name, content in data.items():
                with self.tag("h1"):
                    self.doc.asis(name)

                for type, subcontent in content.items():

                    match type:
                        case "text":
                            for t in subcontent.split("\n"):
                                with self.tag("p"):
                                    self.doc.asis(escape(t.strip()))

                        # case "list":
                        #     for t in subcontent.split("\n"):
                        #         with self.tag("p"):
                        #             self.doc.asis(t.strip())

                        case "table":
                            with self.tag("table"):
                                for cell1, cell2 in subcontent.items():
                                    with self.tag("tr"):
                                        with self.tag("td"):
                                            self.doc.asis(escape(cell1.strip()))
                                        with self.tag("td"):
                                            self.doc.asis(escape(cell2.strip()))

        return film_content
