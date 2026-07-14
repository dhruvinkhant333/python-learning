# Python Learning Projects - Graphics & Image Processing

> **Study Repository:** Educational projects created with AI assistance to learn Python graphics programming and image processing concepts.

## 📚 Projects

### 1. **character_coverage.py** - ASCII Art Character Analysis
Measures how "dark" or "dense" each character appears when rendered at a given size.

**Use case:** Determine which characters are best for ASCII art shading/gradient mapping.

```python
# Darkest to lightest (FreeSans, 100pt)
@WMBQNGRDO$&S%... → ...':,-`.
```

**Concepts:** PIL image processing, functional programming, pixel manipulation

---

### 2. **sphere_gradient.py** - Red/Purple Sphere Visualization
Creates an inverted sphere visualization with alternating red/purple coloring using sine wave brightness.

**Features:**
- ✓ Reduced flashing through buffering
- ✓ Graceful window closing (no crashes)
- ✓ Mathematical gradient using sine wave
- ✓ Responsive to mouse clicks

**Concepts:** tkinter/graphics.py, mathematical visualization, error handling, optimization

---

### 3. **practice.py** - Active Learning Workspace
Empty file reserved for future Python practice exercises.

---

## 🎯 Learning Goals

**Why I created this repo:**
- Study graphics programming in Python
- Understand functional programming patterns
- Learn image processing with PIL
- Practice error handling and code refactoring
- Learn how to read, understand, and improve existing code

**Honest context:**
- ❌ I did NOT write all this code from scratch
- ✓ I studied code from StackExchange and improved it with AI assistance
- ✓ I documented everything to better understand concepts
- ✓ I'm using this for active learning (not claiming as original work)

---

## 📖 Documentation

- **[LEARNING_NOTES.md](LEARNING_NOTES.md)** - My learning journey and study notes
- **[COMMIT_MESSAGES.md](COMMIT_MESSAGES.md)** - Suggested Git commit messages
- **[character_coverage.py](character_coverage.py)** - Fully documented with docstrings and examples
- **[sphere_gradient.py](sphere_gradient.py)** - Fully documented with improvements explained

---

## 🚀 How to Run

### Setup
```bash
# Create virtual environment
python -m venv .venv

# Activate it
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install Pillow graphics.py
```

### Run Projects
```bash
# Character coverage analysis
python character_coverage.py

# Sphere gradient visualization
python sphere_gradient.py
```

---

## 📦 Dependencies

```
Pillow>=9.0.0      # Image processing
graphics.py>=5.0   # Graphics (tkinter wrapper)
```

Install with:
```bash
pip install Pillow graphics.py
```

---

## 🔗 Sources & Attribution

### Code Sources
- **StackExchange Code Review #229448** - Character coverage & sphere gradient
  - Authors: Programming is fun, community contributors
  - License: CC BY-SA 4.0

### Key Improvements Made
| Issue | Solution | Learned |
|-------|----------|---------|
| Window close crash | Try/except GraphicsError | Error handling |
| Intense flashing | Buffering (batch rendering) | Optimization |
| Poor documentation | Added docstrings & comments | Technical writing |

### AI Assistance
- **GitHub Copilot** - Code documentation, bug fixes, explanations

---

## 📋 What I'm Learning

### ✓ Understand Well
- Basic graphics window creation
- Drawing shapes (circles)
- Color manipulation (RGB)
- Function definitions with type hints
- Basic error handling

### 🔄 Currently Learning
- tkinter event handling
- PIL pixel manipulation techniques
- Rendering performance optimization
- Mathematical visualization
- Complex error scenarios

### 📚 Want to Study Next
- Advanced PIL filters & transforms
- 3D graphics (from 2D foundation)
- Animation techniques
- Multiprocessing for performance
- GUI design patterns

---

## 🔄 Git Commits

### Recommended Commit History

```bash
# Initial setup
git add requirements.txt .gitignore
git commit -m "build: add Python dependencies and environment config"

# Character coverage project
git add character_coverage.py
git commit -m "feat: add ASCII art character darkness analyzer

- Measure pixel coverage for each printable character
- Use PIL for image rendering and pixel analysis
- Functional programming with predicates
- Useful for ASCII art gradient mapping

Co-authored-by: StackExchange community
Note: Refactored and documented with AI assistance (GitHub Copilot)"

# Sphere gradient project
git add sphere_gradient.py
git commit -m "feat: add improved sphere gradient visualization

Improvements:
- Fix crash on window close (graceful error handling)
- Reduce flashing via buffering (draw all circles at once)
- Support both mouse click and window close for exit

Concepts: graphics programming, optimization, error handling

Co-authored-by: StackExchange community  
Note: Refactored and documented with AI assistance (GitHub Copilot)"

# Documentation
git add LEARNING_NOTES.md
git commit -m "docs: add learning journey documentation

Record study process:
- What concepts each project teaches
- How AI assisted in understanding and improvement
- Honest reflection on current knowledge level
- Resources used and next steps"
```

---

## ⚖️ License

These projects contain code from **StackExchange** under **CC BY-SA 4.0 license**.

**Please note:**
- This is NOT original code
- It's created for educational purposes
- Used to study Python graphics and image processing
- Code has been refactored and documented
- AI (GitHub Copilot) was used in learning and improvement process

---

## 🙋 Questions About This Repo?

**Why did you use AI to help?**
- To understand confusing concepts better
- To learn best practices from suggested refactoring
- To improve documentation and code quality
- To practice reading and improving existing code

**Is this your original work?**
- No. The base code is from StackExchange community
- Yes, the documentation and improvements are my learning effort
- Partially, in understanding and explaining the code

**Can I use this code?**
- Yes, under CC BY-SA 4.0 license (credit StackExchange)
- It's here for learning, not as a library
- Feel free to study the patterns

---

## 📊 Repository Status

- **Last Updated:** 2026-07-08
- **Status:** 🔄 Active Learning
- **Main Focus:** Graphics Programming & Image Processing
- **Progress:** Beginner → Intermediate

---

*Created with ❤️ and 🧠 for learning Python better.*