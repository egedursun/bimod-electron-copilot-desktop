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

- [ ] Take the first build of the application.
- [ ] Put the updated version on the website.

**RELEASE 5**

---
