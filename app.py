from flask import Flask, request, redirect
import sqlite3

app = Flask(__name__)

def get_alerts():
    conn = sqlite3.connect("cyberguard.db")
    cursor = conn.cursor()

    cursor.execute("SELECT alert_type, severity FROM alerts")
    alerts = cursor.fetchall()

    conn.close()
    return alerts

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        alert_type = request.form["alert_type"]
        severity = request.form["severity"]

        conn = sqlite3.connect("cyberguard.db")
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO alerts(alert_type,severity) VALUES (?,?)",
            (alert_type, severity)
        )

        conn.commit()
        conn.close()

        return redirect("/")

    alerts = get_alerts()

    rows = ""

    for alert in alerts:
        rows += f"""
        <tr>
            <td>{alert[0]}</td>
            <td>{alert[1]}</td>
        </tr>
        """

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>CyberGuard Dashboard</title>

        <style>

        body {{
            font-family: Arial;
            background-color: #0f172a;
            color: white;
            padding: 40px;
            text-align:center;
        }}

        input, select {{
            padding:10px;
            margin:5px;
        }}

        button {{
            padding:10px 20px;
            cursor:pointer;
        }}

        table {{
            margin:auto;
            width:70%;
            border-collapse: collapse;
            background:#1e293b;
        }}

        th, td {{
            border:1px solid #334155;
            padding:12px;
        }}

        th {{
            background:#38bdf8;
            color:black;
        }}

        h1 {{
            color:#38bdf8;
        }}

        </style>
    </head>

    <body>

        <h1>CyberGuard Security Dashboard</h1>

        <h2>Add Security Alert</h2>

        <form method="POST">

            <input
                type="text"
                name="alert_type"
                placeholder="Alert Type"
                required>

            <select name="severity">

                <option>Low</option>
                <option>Medium</option>
                <option>High</option>
                <option>Critical</option>

            </select>

            <button type="submit">
                Add Alert
            </button>

        </form>

        <br>

        <table>

            <tr>
                <th>Alert Type</th>
                <th>Severity</th>
            </tr>

            {rows}

        </table>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)
