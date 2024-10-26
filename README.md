## BIMOD.IO - ELECTRON COPILOT - DESKTOP CLIENT

### INSTRUCTIONS AND DOCUMENTATION

#### **Author**: [Bimod.io AI as a Service](https://www.bimod.io)

---

**DEPENDENCIES:**

- These will be needed to installed by an Bash script for the functions to work properly.

```bash
brew install sox
```

---

**DJANGO ADMIN PANEL CREDENTIALS**

- **Username:** bimod

- **Password:** multimodal

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

- [ ] If it is working, start working on the MEETING project (KANBAN) on mainframe (bimod.io)
- [ ] Test the functionality (dashboard kanban topic creation, description creation, task assignment)
- [ ] Take the fourth build of the application.
- [ ] Put the updated version on the website.

**RELEASE 4**

- [ ] Create the automated process to take screenshots and interpret it to understand daily works (Tempo Project)
- [ ] Create the services and protocols to communicate the tempo.
- [ ] If working, start working on the TEMPO project, on mainframe (bimod.io).
- [ ] Test the functionality (tempo inspection, people task summarization, meta-reporting, performance analysis,
  kanban comparison analysis, etc.)
- [ ] Take the fifth build of the application.
- [ ] Put the updated version on the website.

**RELEASE 5**


---
