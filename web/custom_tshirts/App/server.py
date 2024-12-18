from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return '''
       <html>
    <head>
        <title>Personnalisation de T-shirts</title>
        <style>
            body {
                font-family: 'Roboto', sans-serif;
                background: linear-gradient(120deg, #fdfbfb 0%, #ebedee 100%);
                color: #333;
                margin: 0;
                padding: 20px;
                text-align: center;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
            h1 {
                color: #333;
                font-size: 2.5em;
                margin-bottom: 20px;
                letter-spacing: 1px;
            }
            form {
                background-color: #fff;
                padding: 30px;
                border-radius: 12px;
                box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15);
                max-width: 400px;
                width: 100%;
            }
            label {
                font-size: 1.2em;
                color: #555;
                margin-bottom: 10px;
                display: block;
                text-align: left;
            }
            input[type="text"] {
                width: 100%;
                padding: 12px;
                margin: 10px 0 20px;
                border-radius: 8px;
                border: 1px solid #ccc;
                font-size: 1em;
                box-sizing: border-box;
                transition: border 0.3s ease;
            }
            input[type="text"]:focus {
                border-color: #4CAF50;
                outline: none;
            }
            input[type="submit"] {
                background-color: #4CAF50;
                color: white;
                padding: 12px 20px;
                border: none;
                border-radius: 8px;
                cursor: pointer;
                font-size: 1em;
                transition: background-color 0.3s ease;
            }
            input[type="submit"]:hover {
                background-color: #45a049;
            }
            .container {
                max-width: 600px;
                width: 100%;
                padding: 20px;
                box-sizing: border-box;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Bienvenue sur notre site de personnalisation de t-shirts</h1>
            <form action="/preview" method="get">
                <label for="user_text">Entrez le texte à afficher sur le t-shirt:</label>
                <input type="text" id="user_text" name="user_text" required>
                <input type="submit" value="Prévisualiser">
            </form>
        </div>
    </body>
</html>
    '''

@app.route('/preview', methods=['GET'])
def preview():
    user_text = request.args.get("user_text") or None

    template = '''
        <html>
        <head>
            <title>Prévisualisation de votre T-shirt</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f4;
                    color: #333;
                    margin: 0;
                    padding: 20px;
                    text-align: center;
                }}
                h1 {{
                    color: #333;
                }}
                .preview-container {{
                    background-color: #fff;
                    padding: 20px;
                    border-radius: 8px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                    display: inline-block;
                    position: relative;
                    text-align: center;
                }}
                .preview-container img {{
                    max-width: 100%;
                    border-radius: 8px;
                    display: block;
                }}
                .text-overlay {{
                    position: absolute;
                    top: 50%;
                    left: 50%;
                    transform: translate(-50%, -50%);
                    font-size: 24px;
                    color: white;
                    font-weight: bold;
                    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
                    white-space: nowrap;
                }}
                .button {{
                    margin-top: 20px;
                    display: inline-block;
                    background-color: #4CAF50;
                    color: white;
                    padding: 10px 20px;
                    text-decoration: none;
                    border-radius: 4px;
                }}
                .button:hover {{
                    background-color: #45a049;
                }}
            </style>
        </head>
        <body>
            <div class="preview-container">
                <h1>Prévisualisation de votre t-shirt</h1>
                <div class="text-overlay">{}</div>
                <img src="/static/tshirt_template.jpg" alt="T-shirt"/>
                <br>
                <a href="/" class="button">Revenir</a>
            </div>
        </body>
        </html>
    '''.format(user_text)

    return render_template_string(template)

if __name__ == '__main__':
    app.run(debug=True)