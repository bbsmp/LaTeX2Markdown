from distutils.core import setup

setup(
        name='latex2markdown-bbsmp',
        author="Andrew Tulloch",
        author_email="andrew@tullo.ch",
        version='0.0.1',
        py_modules=['latex2markdown-bbsmp'],
        scripts=['bin/converted_latex_sample.md', 'bin/latex_sample.tex', 'config/charmap.xml'],
        url="https://github.com/bbsmp/LaTeX2Markdown.git",
        description="Thanks Andrew Tulloch, This project is forked from Andrew's masterpiece：https://github.com/ajtulloch/LaTeX2Markdown,  An AMS-LaTeX compatible converter that maps a subset of LaTeX to Markdown/MathJaX.",
        classifiers=[
            "Development Status :: Alpha",
            "Environment :: Console",
            "Programming Language :: Python",
            "Topic :: Scientific/Engineering :: Mathematics",
            "Topic :: Software Development :: Documentation",
            "Topic :: Text Processing :: Markup",
            "Topic :: Text Processing :: Markup :: LaTeX",
            "Topic :: Text Processing :: Markup :: HTML"
            ],
        long_description=open("README.txt").read()
        )
