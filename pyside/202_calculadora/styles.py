# styles.py
PRIMARY_COLOR = "#007BFF"
DARKER_PRIMARY_COLOR = "#0056b3"
DARKEST_PRIMARY_COLOR = "#003d82"

qss = f"""

    QPushButton[cssClass="specialButton"] {{
        color: #fff;
        background: {PRIMARY_COLOR};
    }}
    
    QPushButton[cssClass="specialButton"]:hover {{
        color: #fff;
        background: {DARKER_PRIMARY_COLOR};
    }}
    
    QPushButton[cssClass="specialButton"]:pressed {{
        color: #fff;
        background: {DARKEST_PRIMARY_COLOR};
    }}
"""