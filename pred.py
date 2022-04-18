from flask import Flask, render_template, redirect, url_for, request
import statbotics

sb = statbotics.Statbotics()

def prediction(r1, r2, r3, b1, b2, b3):
	red_sum = sb.get_team(r1)['elo'] + sb.get_team(r2)['elo'] + sb.get_team(r3)['elo']
	blue_sum = sb.get_team(b1)['elo'] + sb.get_team(b2)['elo'] + sb.get_team(b3)['elo']

	red_win_prob = 1 / (1 + 10 ** ((blue_sum - red_sum) / 400))
	blue_win_prob = 1.00 - red_win_prob

	if (red_win_prob > blue_win_prob):
	    return "Red Alliance has a " + str(round(100*red_win_prob,2)) + "% chance of winning."
	else:
	    return "Blue Alliance has a " + str(round(100 * blue_win_prob, 2)) + "% chance of winning."

app = Flask(__name__)

@app.route('/', methods = ["GET", "POST"])
def home():
	if (request.method == "POST"):
		red1 = int(request.form.get("r1"))
		red2 = int(request.form.get("r2"))
		red3 = int(request.form.get("r3"))
		blue1 = int(request.form.get("b1"))
		blue2 = int(request.form.get("b2"))
		blue3 = int(request.form.get("b3"))
		return render_template("index.html", output=prediction(red1, red2, red3, blue1, blue2, blue3))
	else:
		return render_template("index.html")


if __name__ == "__main__":
	app.run()