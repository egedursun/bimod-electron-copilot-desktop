## BIMOD.IO - ELECTRON COPILOT - DESKTOP CLIENT

### INSTRUCTIONS AND DOCUMENTATION

#### **Author**: [Bimod.io AI as a Service](https://www.bimod.io)

---

**DJANGO ADMIN PANEL CREDENTIALS**

- **Username:** bimod

- **Password:** multimodal

---

**CREATING THE APPLICATION/BUILD:**
```bash
sudo npm run dist
```

---

**MIGRATING THE DATABASE:**

- Creating the Database Migrations:

```bash
python3 manage.py makemigrations
```

- Applying the Database Migrations:

```bash
python3 manage.py migrate
```

- Faking the Database Migrations:

```bash
python3 manage.py migrate --fake
```

---

**RUNNING THE APPLICATION BUILD/CREATION**

```bash
sudo npm run dist
  

---

**RUNNING THE APPLICATION:**

**Django Server:**

```bash
python3 manage.py runserver
```

**ElectronJS Native Application:**

```bash
sudo npx electron electron.js
```

---

### TODO LIST

- [ ] Design the web page to download the Electron Copilot (and marketing content)
- [ ] Develop Content on Main Landing Page + Connect the page with the main page. (MetaKanban, Project/Teams, MetaTempo)
- [ ] Push the changes in the main server.
- [ ] Create a label for version on GitHub
- [ ] Update the GitHub board.

---

**RELEASE 5**

---
