class Ball:
    def __init__(self, canvas, paddle, score, color):
        self.canvas = canvas
        self.paddle = paddle
        self.score = score
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.x = 2
        self.y = -2
        self.hit_bottom = False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        
        if pos[0] <= 0 or pos[2] >= self.canvas.winfo_width():
            self.x = -self.x
        
        if pos[1] <= 0:
            self.y = -self.y
        
        if pos[3] >= self.canvas.winfo_height():
            self.hit_bottom = True
            
        if (pos[2] >= self.paddle.canvas.coords(self.paddle.id)[0] and
            pos[0] <= self.paddle.canvas.coords(self.paddle.id)[2] and
            pos[3] >= self.paddle.canvas.coords(self.paddle.id)[1]):
            self.y = -self.y
            self.score.hit()

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        start_positions = [40, 60, 90, 120, 150, 180, 200]
        random.shuffle(start_positions)
        self.starting_point_x = start_positions[0]
        self.canvas.move(self.id, self.starting_point_x, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.started = False
        self.canvas.bind_all('<KeyPress-Return>', self.start_game)

    def turn_right(self, event):
        self.x = 2

    def turn_left(self, event):
        self.x = -2

    def start_game(self, event):
        self.started = True

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)

        if pos[0] <= 0 or pos[2] >= self.canvas_width:
            self.x = 0

class Score:
    def __init__(self, canvas, color):
        self.score = 0
        self.canvas = canvas
        self.id = canvas.create_text(450, 10, text=self.score, font=('Courier', 15), fill=color)

    def hit(self):
        self.score += 1
        self.canvas.itemconfig(self.id, text=self.score)

score = Score(canvas, 'green')
paddle = Paddle(canvas, 'White')
ball = Ball(canvas, paddle, score, 'red')

while not ball.hit_bottom:
    if paddle.started:
        ball.draw()
        paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

time.sleep(3)
