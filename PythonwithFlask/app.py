from flask import Flask, render_template
app = Flask("app")

students_data = ['jatin', 'mandeep', 'harshita']
my_data = {
  "Name": "Jatin Katyal",
  "Fav Language": "Python",
  "Company": "Coding Blocks"
}

# abc.com/profile/7
# amazon.in/Apple-iPhone-XR-64GB-Black/dp/B07JWV47JW

@app.route('/')
def index():
  return render_template('index.html', info = my_data)

@app.route('/students/')
def students():
  return render_template('students.html', students = students_data, enumerate = enumerate)

@app.route('/students/<int:id>/')
def student(id):
  return render_template('student_detail.html', name = students_data[id - 1])

if __name__ == "__main__":
  app.run(port = 8000, debug = True)
