import tkinter as tk
from tkinter import font
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk

questions = [
    ("Do you feel numbness or tingling?", ["Not at all", "Mildly,but it didn't bother me much", "Moderately,It wasn't pleasant", "Severely,it bothered me a lot"]),
    ("Have you been feeling hot flashed?", ["Not at all", "Mildly,but it didn't bother me much", "Moderately,It wasn't pleasant", "Severely,it bothered me a lot"]),
    ("Do you feel wobbliness in your legs?", ["Not at all", "Mildly,but it didn't bother me much", "Moderately,It wasn't pleasant", "Severely,it bothered me a lot"]),
    ("Are you unable to relax?(fustration,mind doesn't relax)", ["Not at all", "Mildly,but it didn't bother me much", "Moderately,It wasn't pleasant", "Severely,it bothered me a lot"]),
    ("Do you feel worst happening(losing something,death,accident)?", ["Not at all", "Mildly,but it didn't bother me much", "Moderately,It wasn't pleasant", "Severely,it bothered me a lot"]),
    ("Do you feel dizzy or lightheaded?", ["Not at all", "Mildly,but it didn't bother me much", "Moderately,It wasn't pleasant", "Severely,it bothered me a lot"]),
    ("Does your heart pound or race(while resting or in slight motion)?", ["Not at all", "Mildly,but it didn't bother me much", "Moderately,It wasn't pleasant", "Severely,it bothered me a lot"]),
    ("Do you feel unbalanced?", ["Not at all", "Mildly,but it didn't bother me much", "Moderately,It wasn't pleasant", "Severely,it bothered me a lot"]),
    ("Do you feel terrified(without knowing the reason)?", ["Not at all", "Mildly,but it didn't bother me much", "Moderately,It wasn't pleasant", "Severely,it bothered me a lot"]),
    ("Do you feel nervous?", ["Not at all", "Mildly,but it didn't bother me much", "Moderately,It wasn't pleasant", "Severely,it bothered me a lot"]),
    ("Do you have a choking feeling?", ["Not at all", "Mildly,but it didn't bother me much", "Moderately,It wasn't pleasant", "Severely,it bothered me a lot"]),
    ("Does your hand tremble?", ["Not at all", "Mildly,but it didn't bother me much", "Moderately,It wasn't pleasant", "Severely,it bothered me a lot"]),
    ("Do you feel shaky/shiver?", ["Not at all", "Mildly,but it didn't bother me much", "Moderately,It wasn't pleasant", "Severely,it bothered me a lot"]),
    ("Do you fear of losing control(it maybe action or feeling) ?", ["Not at all", "Mildly,but it didn't bother me much", "Moderately,It wasn't pleasant", "Severely,it bothered me a lot"]),
    ("Do you have difficulty in breathing?", ["Not at all", "Mildly,but it didn't bother me much", "Moderately,It wasn't pleasant", "Severely,it bothered me a lot"]),
    ("Do you have a fear of dying?", ["Not at all", "Mildly,but it didn't bother me much", "Moderately,It wasn't pleasant", "Severely,it bothered me a lot"]),
    ("Do you feel panicked?", ["Not at all", "Mildly,but it didn't bother me much", "Moderately,It wasn't pleasant", "Severely,it bothered me a lot"]),
    ("Do you have indigestion(after passing medical criteria)?", ["Not at all", "Mildly,but it didn't bother me much", "Moderately,It wasn't pleasant", "Severely,it bothered me a lot"]),
    ("Do you faint often?", ["Not at all", "Mildly,but it didn't bother me much", "Moderately,It wasn't pleasant", "Severely,it bothered me a lot"]),
    ("Do you have face flushed(redening of face)?", ["Not at all", "Mildly,but it didn't bother me much", "Moderately,It wasn't pleasant", "Severely,it bothered me a lot"]),
    ("Do you have Hot/cold sweats(while in rest or in light motion)?", ["Not at all", "Mildly,but it didn't bother me much", "Moderately,It wasn't pleasant", "Severely,it bothered me a lot"])
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1000x750")
        self.root.minsize(800, 600)
        self.root.config(bg="#282c34")

        self.current_question = 0
        self.total_score = 0
        self.selected_option = None
        self.answers = {}  # Store answers for each question
        self.max_score = len(questions) * 3  # 0-3 points per question

        self.create_header()
        self.start_button = tk.Button(root, text="Start Quiz", command=self.start_quiz, bg="#1abc9c", fg="black", width=15, font=("Helvetica", 14), borderwidth=0)
        self.start_button.pack(pady=20)
        self.start_button.bind("<Enter>", lambda e: self.on_hover(self.start_button))
        self.start_button.bind("<Leave>", lambda e: self.off_hover(self.start_button))

    def create_header(self, show_progress=True):
        self.header_frame = tk.Frame(self.root, bg="#282c34")
        self.header_frame.pack(fill="x")

        self.exit_button = tk.Button(
            self.header_frame, text="X", command=self.root.quit, bg="#e74c3c",
            fg="black", font=("Helvetica", 12, "bold"), borderwidth=0
        )
        self.exit_button.place(relx=1.0, x=-15, y=12, anchor="ne")

        title_font = font.Font(self.root, family="Helvetica", size=24, weight="bold")
        self.title_label = tk.Label(
            self.header_frame, text="Beck Anxiety Calculator", font=title_font,
            fg="white", bg="#282c34"
        )
        self.title_label.pack(pady=(30, 12))

        self.progress_bar = None
        if show_progress:
            self.progress_bar = ttk.Progressbar(
                self.header_frame, length=300, mode="determinate",
                maximum=self.max_score
            )
            self.progress_bar.pack(pady=(0, 10))

    def on_hover(self, widget):
        widget.config(bg="#16a085")

    def off_hover(self, widget):
        widget.config(bg="#1abc9c")

    def start_quiz(self):
        self.start_button.pack_forget()
        self.ask_question()

    def ask_question(self):
        for widget in self.root.winfo_children():
            if widget is not self.header_frame:
                widget.destroy()

        if self.current_question < len(questions):
            question, options = questions[self.current_question]

            question_frame = tk.Frame(self.root, bg="black", padx=20, pady=10)
            question_frame.pack(expand=True, fill="both", padx=20, pady=20)

            question_label = tk.Label(question_frame, text=question, font=("Helvetica", 16), wraplength=700, bg="black", fg="white")
            question_label.pack(pady=20)

            self.selected_option = tk.IntVar(value=-1)
            self.option_buttons = []

            for idx, option in enumerate(options):
                button = tk.Button(
                    question_frame, text=option, font=("Helvetica", 12), width=40, pady=5,
                    relief="raised", bg="#ecf0f1",
                    command=lambda idx=idx: self.toggle_selection(idx)
                )
                button.pack(anchor="center", pady=5)
                button.bind("<Enter>", lambda e, b=button: self.on_option_hover(b))
                button.bind("<Leave>", lambda e, b=button: self.off_option_hover(b))
                self.option_buttons.append(button)
                
            nav_frame = tk.Frame(question_frame, bg="black")
            nav_frame.pack(pady=30)

            back_state = "disabled" if self.current_question == 0 else "active"
            self.back_button = tk.Button(nav_frame, text="Back", command=self.go_back, bg="#e67e22", fg="white", width=10, font=("Helvetica", 12), state=back_state)
            self.back_button.grid(row=0, column=0, padx=20)

            self.next_button = tk.Button(nav_frame, text="Next", command=self.next_question, bg="#3498db", fg="white", width=10, font=("Helvetica", 12))
            self.next_button.grid(row=0, column=1, padx=20)
            
            # Restore previous selection if returning to this question
            if self.current_question in self.answers:
                prev_idx = self.answers[self.current_question]
                self.selected_option.set(prev_idx)
                self.option_buttons[prev_idx].config(bg="#2ecc71")
            
            self.update_progress_bar()

        else:
            self.show_result()

    def on_option_hover(self, button):
        button.config(bg="#bdc3c7")

    def off_option_hover(self, button):
        if button.cget("bg") != "#2ecc71":
            button.config(bg="#ecf0f1")

    def toggle_selection(self, idx):
        if self.selected_option.get() == idx:
            self.selected_option.set(-1)
            self.option_buttons[idx].config(bg="#ecf0f1")
        else:
            for i, button in enumerate(self.option_buttons):
                button.config(bg="#ecf0f1")
            self.selected_option.set(idx)
            self.option_buttons[idx].config(bg="#2ecc71")

    def next_question(self):
        if self.selected_option.get() >= 0:
            # Store the answer for this question
            self.answers[self.current_question] = self.selected_option.get()
        self.current_question += 1
        self.ask_question()

    def go_back(self):
        if self.current_question > 0:
            self.current_question -= 1
            self.ask_question()

    def show_result(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.create_header(show_progress=False)

        # Calculate total score from stored answers
        self.total_score = sum(self.answers.values())
        percentage_score = (self.total_score / self.max_score) * 100

        if percentage_score <= 25:
            anxiety_level = "Low Anxiety"
            advice =  """Advice: Great news! Your results indicate a low level of anxiety. 
            Keep maintaining a healthy lifestyle, focusing on positive habits such as regular exercise, healthy eating, and a good sleep routine. 
            Continue practicing relaxation techniques like mindfulness and deep breathing to stay balanced and relaxed."""
        elif percentage_score <= 50:
            anxiety_level = "Moderate Anxiety"
            advice = """Advice: Your results indicate a moderate level of anxiety. Consider incorporating stress-reducing practices such as yoga, meditation, or spending time outdoors. If you find your anxiety interfering with daily activities,
            speaking to a mental health professional might help you better manage stress."""
        else:
            anxiety_level = "High Anxiety"
            advice = """Advice: Your results indicate a high level of anxiety, but there are steps you can take to manage it.Seek professional help,
            practice relaxation techniques like deep breathing, and engage in regular exercise to reduce stress. Prioritize sleep,
            limit stimulants, and build a support system to manage anxiety effectively. Be patient with yourself—progress takes time."""

        result_text = f"Your Score: {self.total_score} / {self.max_score} ({percentage_score:.2f}%)\n\nAnxiety Level: {anxiety_level}\n\n{advice}"

        result_label = tk.Label(self.root, text=result_text, font=("Helvetica", 14), bg="#282c34", fg="white", wraplength=700, justify="center")
        result_label.pack(pady=10)
        
        self.create_anxiety_graph(percentage_score)
        
        restart_button = tk.Button(self.root, text="Restart Quiz", command=self.restart_quiz, bg="#1abc9c", fg="white", width=20, font=("Helvetica", 14, "bold"), borderwidth=0, relief="raised", pady=10)
        restart_button.pack(pady=15)
        restart_button.bind("<Enter>", lambda e: restart_button.config(bg="#16a085"))
        restart_button.bind("<Leave>", lambda e: restart_button.config(bg="#1abc9c"))

    def create_anxiety_graph(self, percentage_score):
        anxiety_labels = ['Low\n(0-25%)', 'Moderate\n(26-50%)', 'High\n(51-100%)']
        anxiety_values = [25, 50, 100]
        colors = ['green', 'yellow', 'red']
        
        fig, ax = plt.subplots(figsize=(5, 3))
        ax.bar(anxiety_labels, anxiety_values, color=colors, alpha=0.3, edgecolor='black')
        
        # Add a horizontal line showing the user's actual score
        score_color = 'green' if percentage_score <= 25 else 'orange' if percentage_score <= 50 else 'red'
        ax.axhline(y=percentage_score, color=score_color, linestyle='--', linewidth=2, 
               label=f"Your Score: {percentage_score:.1f}%")

        ax.set_title("Anxiety Level Chart", fontsize=12, fontweight='bold') 
        ax.set_xlabel("Anxiety Level", fontsize=10)
        ax.set_ylabel("Percentage (%)", fontsize=10)
        ax.set_ylim(0, 100)
        ax.legend(fontsize=9)
        ax.grid(axis='y', alpha=0.3)
        
        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()
        canvas.get_tk_widget().pack(pady=10)

    def update_progress_bar(self):
        progress = (self.current_question / len(questions)) * self.max_score
        self.progress_bar['value'] = progress

    def restart_quiz(self):
        # Clear all widgets
        for widget in self.root.winfo_children():
            widget.destroy()
        self.create_header()
        
        # Reset quiz state
        self.total_score = 0
        self.current_question = 0
        self.answers = {}  # Clear stored answers
        
        self.ask_question()


def main():
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()