from flask import Flask, request
from datetime import datetime

app = Flask(__name__)


# Tageszeit bestimmen
def get_time_message():
    hour = datetime.now().hour

    if 4 <= hour < 9:
        return "Guten Morgen 🌅", "#f5f5f5", "black", "#ffffff"

    elif 9 <= hour < 13:
        return "Guten Vormittag 🌤️", "#f5f5f5", "black", "#ffffff"

    elif 13 <= hour < 16:
        return "Guten Mittag ☀️", "#f5f5f5", "black", "#ffffff"

    elif 16 <= hour < 18:
        return "Guten Nachmittag 🌇", "#f5f5f5", "black", "#ffffff"

    elif 18 <= hour < 21:
        return "Guten Abend 🌆", "#111111", "white", "#1f1f1f"

    else:
        return "Gute Nacht 🌙", "#111111", "white", "#1f1f1f"


@app.route("/")
def home():

    # Besucher-IP holen
    forwarded_ip = request.headers.get("X-Forwarded-For")

    if forwarded_ip:
        visitor_ip = forwarded_ip.split(",")[0]
    else:
        visitor_ip = request.remote_addr

    print("Neue Besucher-IP:", visitor_ip)

    greeting, bg_color, text_color, card_color = get_time_message()

    page = f"""
    <!DOCTYPE html>

    <html>

    <head>

        <title>Portfolio Shorty</title>

        <style>

            body {{
                margin: 0;
                padding: 0;
                font-family: Arial;
                background: {bg_color};
                color: {text_color};
                text-align: center;
                transition: 0.5s;
            }}

            .main {{
                margin-top: 70px;
                animation: fadeIn 1s ease;
            }}

            .profile {{
                width: 150px;
                height: 150px;
                border-radius: 50%;
                object-fit: cover;
                animation: popIn 1s ease;
            }}

            h1 {{
                margin-top: 20px;
                font-size: 50px;
                animation: slideUp 1s ease;
            }}

            h2 {{
                animation: slideUp 1.2s ease;
            }}

            .card {{
                width: 320px;
                margin: 20px auto;
                padding: 20px;
                border-radius: 20px;
                background: {card_color};
                cursor: pointer;
                transition: 0.3s;
                animation: slideUp 1.4s ease;
            }}

            .card:hover {{
                transform: scale(1.05);
            }}

            .hidden {{
                display: none;
                margin-top: 10px;
                color: gray;
            }}

            @keyframes fadeIn {{
                from {{
                    opacity: 0;
                }}

                to {{
                    opacity: 1;
                }}
            }}

            @keyframes slideUp {{
                from {{
                    opacity: 0;
                    transform: translateY(40px);
                }}

                to {{
                    opacity: 1;
                    transform: translateY(0);
                }}
            }}

            @keyframes popIn {{
                from {{
                    transform: scale(0);
                }}

                to {{
                    transform: scale(1);
                }}
            }}

        </style>

        <script>

            function showDiscord() {{

                let discord = document.getElementById("discordBox");

                if (discord.style.display === "block") {{
                    discord.style.display = "none";
                }}

                else {{
                    discord.style.display = "block";
                }}
            }}

        </script>

    </head>

    <body>

        <div class="main">

            <img
                class="profile"
                src="c:\Users\kosee\Downloads\1f6980742de5ed1798fbc6f69e46ba3f.png"
            >

            <h1>Shorty</h1>

            <h2>{greeting}</h2>

            <div class="card" onclick="showDiscord()">

                🎮 Discord

                <div class="hidden" id="discordBox">
                    Shorty#0000
                </div>

            </div>

            <div class="card">

                📌 About Me

                <div style="margin-top:10px;color:gray;">
                    Welcome to my portfolio website.
                </div>

            </div>

        </div>

    </body>

    </html>
    """

    return page


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
