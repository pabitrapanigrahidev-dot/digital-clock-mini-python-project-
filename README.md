
# 🕒 Python Digital Clock

A simple and elegant **Digital Clock** built using **Python** and the **Tkinter** GUI library. The clock displays the current system time in **HH:MM:SS** format and updates every second.

---

## 📸 Screenshot

> Add your screenshot inside a folder named **images**

```text
images/
└── digital-clock.png
```

Then display it using:

```markdown
![Digital Clock](images/digital-clock.png)
```

---

## 🚀 Features

- ⏰ Live Digital Clock
- 🖥️ Tkinter GUI
- 🔄 Updates every second
- 🎨 Yellow background with bold black text
- ⚡ Lightweight and beginner-friendly
- 💻 Cross-platform (Windows, Linux, macOS)

---

## 🛠️ Technologies Used

- Python 3.x
- Tkinter
- time module

---

## 📁 Project Structure

```
Digital-Clock/
│
├── clock.py
├── README.md
└── images/
    └── digital-clock.png
```

---

## ▶️ How to Run

### 1. Clone Repository

```bash
git clone https://github.com/your-username/Digital-Clock.git
```

### 2. Go to Project Folder

```bash
cd Digital-Clock
```

### 3. Run the Program

```bash
python clock.py
```

---

## 💻 Source Code

```python
import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("DIGITAL CLOCK")
root.geometry("500x200")

def clock():
    current_time = strftime("%H:%M:%S")
    label.config(text=current_time)
    label.after(1000, clock)

label = tk.Label(
    root,
    font=("Calibri", 50, "bold"),
    background="yellow",
    foreground="black"
)

label.pack(expand=True)

clock()

root.mainloop()
```

---

## 📚 How It Works

- Imports the Tkinter GUI library.
- Uses `strftime()` from the `time` module to get the current system time.
- Updates the label every 1000 milliseconds using `after()`.
- Displays the current time continuously until the window is closed.

---

## 📦 Requirements

Install Python 3 or later.

Check version:

```bash
python --version
```

No external libraries are required.

---

## 🎯 Output

```
10:48:18
```

The time updates every second automatically.

---

## 🌟 Future Improvements

- 🌙 Dark Mode
- 📅 Date Display
- 🌍 Multiple Time Zones
- 🔔 Alarm Feature
- ⏱ Stopwatch
- ⏳ Countdown Timer
- Custom Themes
- Fullscreen Mode

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit changes

```bash
git commit -m "Added new feature"
```

4. Push

```bash
git push origin feature-name
```

5. Create a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Pabitra Panigrahi**

- Python Developer
- Java Full Stack Learner
- DevOps Enthusiast
- Open Source Contributor

---

⭐ If you like this project, don't forget to **Star** the repository.
