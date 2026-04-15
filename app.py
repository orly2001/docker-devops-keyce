from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Flask Docker App</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      font-family: 'Segoe UI', sans-serif;
      background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      color: white;
    }
    .card {
      background: rgba(255,255,255,0.07);
      border: 1px solid rgba(255,255,255,0.15);
      backdrop-filter: blur(12px);
      border-radius: 20px;
      padding: 50px 60px;
      text-align: center;
      max-width: 600px;
      box-shadow: 0 20px 60px rgba(0,0,0,0.4);
    }
    .emoji { font-size: 64px; margin-bottom: 20px; }
    h1 { font-size: 2rem; margin-bottom: 12px; color: #00d4ff; }
    p  { font-size: 1.1rem; line-height: 1.7; color: #cce7ff; margin-bottom: 8px; }
    .badge {
      display: inline-block;
      margin-top: 24px;
      padding: 8px 20px;
      border-radius: 50px;
      background: linear-gradient(90deg, #00d4ff, #007cf0);
      font-weight: bold;
      font-size: 0.95rem;
      letter-spacing: 1px;
    }
    .footer { margin-top: 30px; font-size: 0.8rem; color: rgba(255,255,255,0.4); }
  </style>
</head>
<body>
  <div class="card">
    <div class="emoji">🐳</div>
    <h1>Application Dockerisée</h1>
    <p>Bonjour à tous ! Ceci est une application Flask</p>
    <p>conteneurisée avec Docker par</p>
    <div class="badge">tchoudjidombouyvanjunior</div>
    <p class="footer">Keyce IIA — Conduite de Projet Agile/DevOps — 2026</p>
  </div>
</body>
</html>
"""

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
